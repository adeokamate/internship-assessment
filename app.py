import tempfile

import streamlit as st
from dotenv import load_dotenv

from backend.pipeline import run_pipeline, LANGUAGE_SPEAKERS


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

if st.button("Run Pipeline"):
    try:
        with st.spinner("Processing with Sunbird AI..."):
            result = run_pipeline(
                input_type=input_type,
                target_language=target_language,
                text_input=text_input,
                audio_path=audio_path,
            )

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
        st.error(str(error))