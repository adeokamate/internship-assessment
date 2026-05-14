from typing import Optional, Dict, Any, Callable

from mutagen import File as MutagenFile

from backend.sunbird_client import SunbirdClient


LANGUAGE_SPEAKERS = {
    "Luganda": 248,
    "Runyankole": 243,
    "Ateso": 242,
    "Lugbara": 245,
    "Acholi": 241,
}

# Pipeline step definitions for progress tracking
PIPELINE_STEPS = [
    "validating input",
    "transcribing audio",
    "summarizing text",
    "translating summary",
    "generating speech",
]


def get_audio_duration_seconds(audio_path: str) -> float:
    audio = MutagenFile(audio_path)

    if audio is None or not hasattr(audio.info, "length"):
        return 0

    return float(audio.info.length)


def validate_audio_duration(audio_path: str, max_minutes: int = 5) -> None:
    duration_seconds = get_audio_duration_seconds(audio_path)
    max_seconds = max_minutes * 60

    if duration_seconds > max_seconds:
        raise ValueError(
            f"Audio file is too long. Maximum allowed length is {max_minutes} minutes."
        )


def run_pipeline(
    input_type: str,
    target_language: str,
    text_input: Optional[str] = None,
    audio_path: Optional[str] = None,
    progress_callback: Optional[Callable[[int, str, str], None]] = None,
) -> Dict[str, Any]:
    """Run the full pipeline with optional progress callback.

    Args:
        progress_callback: Called as callback(step_index, step_name, detail)
            on each pipeline step.
    """
    # Validate target language before making any API calls
    speaker_id = LANGUAGE_SPEAKERS.get(target_language)
    if speaker_id is None:
        raise ValueError(
            f"Unsupported target language: {target_language}. "
            f"Supported languages: {list(LANGUAGE_SPEAKERS.keys())}"
        )

    client = SunbirdClient()

    def notify(step_index: int, detail: str = ""):
        if progress_callback:
            progress_callback(step_index, PIPELINE_STEPS[step_index], detail)

    # Step 0: validate input
    notify(0)

    transcript = None

    if input_type == "Audio":
        if not audio_path:
            raise ValueError("Please upload an audio file.")

        validate_audio_duration(audio_path)
        # Step 1: transcribe
        notify(1)
        original_text = client.transcribe_audio(audio_path)
        transcript = original_text

    else:
        if not text_input or not text_input.strip():
            raise ValueError("Please enter some text.")

        original_text = text_input.strip()

    # Step 2: summarize
    notify(2)
    summary = client.summarize_text(original_text)

    # Step 3: translate
    notify(3)
    translated_summary = client.translate_text(summary, target_language)

    # Step 4: synthesize speech
    notify(4, f"speaker_id={speaker_id}")
    audio_url = client.synthesize_speech(translated_summary, speaker_id)

    return {
        "original_text": original_text,
        "transcript": transcript,
        "summary": summary,
        "translated_summary": translated_summary,
        "audio_url": audio_url,
    }