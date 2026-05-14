---
title: Sunbird AI Multilingual Summariser
emoji: 🧠
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Sunbird AI Multilingual Summariser

## Project Description

This application is a Generative AI system built using Sunbird AI services. It allows users to input either text or audio, processes the input through an AI pipeline, and produces:

- A summarized version of the content
- A translation of the summary into selected Ugandan local languages
- A synthesized audio output of the translated text

The system integrates Speech-to-Text, Large Language Model (Sunflower), and Text-to-Speech services into a single end-to-end workflow.

## Architecture Overview

The application follows this AI processing pipeline:

```
Input (Text / Audio)
        ↓
Speech-to-Text (if audio input)
        ↓
Summarization (Sunflower LLM)
        ↓
Translation (Sunflower LLM)
        ↓
Text-to-Speech (Sunbird TTS)
        ↓
Final Output (Text + Audio)
```

## 🔌 Sunbird AI Services Used

- **Speech-to-Text (STT)**: Converts audio to text
- **Sunflower LLM**: Used for summarization and translation
- **Text-to-Speech (TTS)**: Converts translated text into audio

## ⚙️ Local Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/adeokamate/internship-assessment.git
   cd internship-assessment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```
   SUNBIRD_API_TOKEN=your_token_here
   ```
   Refer to `.env.example` for required variables.

6. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 🔐 Environment Variables

| Variable          | Description                                      |
|-------------------|--------------------------------------------------|
| SUNBIRD_API_TOKEN | API token used to authenticate requests to Sunbird AI services |

## 🚀 Features

- Accepts text and audio input
- Speech-to-text transcription for audio files
- AI-powered summarization using Sunflower LLM
- Translation into Ugandan local languages:
  - Luganda
  - Runyankole
  - Ateso
  - Lugbara
  - Acholi
- Text-to-speech audio generation
- Displays all intermediate outputs clearly:
  - Original text
  - Transcript (if audio)
  - Summary
  - Translated summary
  - Audio playback

## 🧪 Usage Guide

1. Open the app in your browser
2. Choose input type: Text or Audio
3. If audio → upload file (max 5 minutes)
4. Select target language
5. Click Process
6. View results:
   - Original text
   - Summary
   - Translated text
   - Play audio output

A sample `.ogg` audio file is included for testing speech transcription.

Location:

```
samples/test_audio.ogg
```

### Quick Test

1. Upload `samples/test_audio.ogg`
2. Choose a target language
3. Click **Run Pipeline**

## 🌍 Deployment

The application is publicly available at: [https://huggingface.co/spaces/adeokamate/multilingual-sunbird-assistant](https://huggingface.co/spaces/adeokamate/multilingual-sunbird-assistant)

Hosted using: Hugging Face Spaces

## ⚠️ Known Limitations

- Maximum audio length: 5 minutes
- Requires stable internet connection (API-based system)
- Response time depends on Sunbird AI API latency
- Limited to supported Ugandan languages only

## 📁 Project Structure

```
.
├── app.py
├── backend/
│   ├── sunbird_client.py
│   ├── pipeline.py
├── exercises/
│   ├── basics.py
├── requirements.txt
├── .env.example
└── README.md
```

## 👨‍💻 Author

Developed by ATUHIIRE DEO KAMATE
Computer Science Student, Makerere University

Built as part of the Sunbird AI Internship Assessment, focusing on multilingual AI workflows including speech transcription, summarization, translation, and text-to-speech generation using Sunbird AI APIs.

GitHub: https://github.com/adeokamate
Portfolio: https://adeokamate.github.io/portfolio/

## 🔗 Repository & Deployment

- **GitHub Repo**: [https://github.com/adeokamate/internship-assessment](https://github.com/adeokamate/internship-assessment)
- **Live App**: [https://huggingface.co/spaces/adeokamate/multilingual-sunbird-assistant](https://huggingface.co/spaces/adeokamate/multilingual-sunbird-assistant)

© 2026 ATUHIIRE DEO KAMATE. Developed for the Sunbird AI Internship Assessment.