import tempfile

import streamlit as st
from dotenv import load_dotenv

from backend.pipeline import run_pipeline, LANGUAGE_SPEAKERS, PIPELINE_STEPS


load_dotenv()

st.set_page_config(
    page_title="Sunbird AI GenAI App",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 Sunbird AI GenAI Application")
st.write(
    "Provide text or upload audio, then generate a summary, translate it into a Ugandan local language, and listen to the translated audio."
)

input_type = st.radio(
    "Choose input type",
    ["Text", "Audio"],
    horizontal=True,
)

target_language = st.selectbox(
    "Choose target language",
    list(LANGUAGE_SPEAKERS.keys()),
)

text_input = None
audio_path = None

if input_type == "Text":
    text_input = st.text_area(
        "Enter or paste your text",
        height=200,
        placeholder="Paste text here...",
    )

else:
    uploaded_audio = st.file_uploader(
        "Upload an audio file",
        type=["mp3", "wav", "m4a", "ogg"],
    )

    if uploaded_audio is not None:
        suffix = uploaded_audio.name.split(".")[-1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as temp_file:
            temp_file.write(uploaded_audio.read())
            audio_path = temp_file.name

        st.success("Audio uploaded successfully.")


def _on_progress(step_index: int, step_name: str, detail: str):
    """Callback invoked by the pipeline on each step."""
    # Build a per-step status dict so Streamlit reruns show updates
    if "progress" not in st.session_state:
        st.session_state.progress = {}
    st.session_state.progress[step_index] = {"name": step_name, "detail": detail}


if st.button("Run Pipeline"):
    # Reset progress state
    st.session_state.progress = {}

    # Create one placeholder per step so the UI updates as each finishes
    step_placeholders = []
    for i, step_name in enumerate(PIPELINE_STEPS):
        ph = st.empty()
        step_placeholders.append(ph)
        ph.info(f"⏳ Step {i + 1}/{len(PIPELINE_STEPS)}: {step_name}…")

    overall_placeholder = st.empty()
    overall_placeholder.info("⏳ Pipeline running…")

    try:

        def progress_callback(step_index, step_name, detail):
            """Bridge callback: updates the right Streamlit placeholder."""
            _on_progress(step_index, step_name, detail)
            step_placeholders[step_index].success(
                f"✅ Step {step_index + 1}/{len(PIPELINE_STEPS)}: {step_name}"
                + (f" ({detail})" if detail else "")
            )
            # Mark all earlier completed steps
            for j in range(step_index):
                if j in st.session_state.progress:
                    step_placeholders[j].success(
                        f"✅ Step {j + 1}/{len(PIPELINE_STEPS)}: "
                        f"{st.session_state.progress[j]['name']}"
                    )

        result = run_pipeline(
            input_type=input_type,
            target_language=target_language,
            text_input=text_input,
            audio_path=audio_path,
            progress_callback=progress_callback,
        )

        overall_placeholder.success("✅ Pipeline complete! Rendering results…")

        st.subheader("Original Text")
        st.write(result["original_text"])

        if result["transcript"]:
            st.subheader("Transcript")
            st.write(result["transcript"])

        st.subheader("Summary")
        st.write(result["summary"])

        st.subheader(f"Translated Summary ({target_language})")
        st.write(result["translated_summary"])

        st.subheader("Generated Audio")
        st.audio(result["audio_url"])

    except Exception as error:
        overall_placeholder.error(str(error))