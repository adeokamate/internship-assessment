import os
from typing import BinaryIO, Dict, Any
import mimetypes


import requests
from dotenv import load_dotenv


load_dotenv()


class SunbirdAPIError(Exception):
    """Custom error for Sunbird API failures."""
    pass


class SunbirdClient:
    def __init__(self):
        self.base_url = "https://api.sunbird.ai"
        self.token = os.getenv("SUNBIRD_API_TOKEN")

        if not self.token:
            raise SunbirdAPIError(
                "SUNBIRD_API_TOKEN is missing. Please add it to your .env file."
            )

        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        if not response.ok:
            raise SunbirdAPIError(
                f"Sunbird API error {response.status_code}: {response.text}"
            )

        return response.json()

    def transcribe_audio(self, audio_path: str) -> str:
        url = f"{self.base_url}/tasks/stt"

        file_name = os.path.basename(audio_path)
        mime_type, _ = mimetypes.guess_type(audio_path)

        if mime_type is None:
            mime_type = "audio/mpeg"

        with open(audio_path, "rb") as audio_file:
            files = {
                "audio": (file_name, audio_file, mime_type)
            }

            response = requests.post(url, headers=self.headers, files=files)

        data = self._handle_response(response)

        return (
            data.get("transcript")
            or data.get("text")
            or data.get("output", {}).get("text", "")
        )

    def sunflower_simple(self, instruction: str) -> str:
        url = f"{self.base_url}/tasks/sunflower_simple"

        headers = {
            **self.headers,
            "Content-Type": "application/x-www-form-urlencoded",
        }

        payload = {
            "instruction": instruction,
            "model_type": "qwen",
            "temperature": 0.2,
        }

        response = requests.post(url, headers=headers, data=payload)
        data = self._handle_response(response)

        return data.get("response", "")

    def summarize_text(self, text: str) -> str:
        url = f"{self.base_url}/tasks/summarise"

        headers = {
            **self.headers,
            "Content-Type": "application/json"
        }

        payload = {
            "text": text
        }

        response = requests.post(url, headers=headers, json=payload)
        data = self._handle_response(response)

        return data.get("summarized_text", "")

    def translate_text(self, text: str, target_language: str) -> str:
        instruction = f"""
Translate the following text into {target_language}.
Return only the translated text.

Text:
{text}
"""
        return self.sunflower_simple(instruction)

    def synthesize_speech(self, text: str, speaker_id: int) -> str:
        url = f"{self.base_url}/tasks/tts"

        headers = {
            **self.headers,
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "speaker_id": speaker_id
        }

        response = requests.post(url, headers=headers, json=payload)
        data = self._handle_response(response)

        return data["output"]["audio_url"]