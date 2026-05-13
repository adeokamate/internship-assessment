---
title: Sunbird AI Multilingual Summariser
emoji: 🧠
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
--- 
 
 Sunbird AI Multilingual Summariser
 Project Description

This application is a Generative AI system built using Sunbird AI services. It allows users to input either text or audio, processes the input through an AI pipeline, and produces:

A summarized version of the content
A translation of the summary into selected Ugandan local languages
A synthesized audio output of the translated text

The system integrates Speech-to-Text, Large Language Model (Sunflower), and Text-to-Speech services into a single end-to-end workflow.

 Architecture Overview

The application follows this AI processing pipeline:

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
🔌 Sunbird AI Services Used
Speech-to-Text (STT) → Converts audio to text
Sunflower LLM → Used for summarization and translation
Text-to-Speech (TTS) → Converts translated text into audio
⚙️ Local Setup Instructions
1. Clone the repository
git clone https://github.com/<your-username>/internship-assessment.git
cd internship-assessment
2. Create virtual environment
python -m venv venv
3. Activate environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Configure environment variables

Create a .env file in the root directory:

SUNBIRD_API_TOKEN=your_token_here

Refer to .env.example for required variables.

6. Run the application
streamlit run app.py
🔐 Environment Variables
Variable	Description
SUNBIRD_API_TOKEN	API token used to authenticate requests to Sunbird AI services
🚀 Features
Accepts text and audio input
Speech-to-text transcription for audio files
AI-powered summarization using Sunflower LLM
Translation into Ugandan local languages:
Luganda
Runyankole
Ateso
Lugbara
Acholi
Text-to-speech audio generation
Displays all intermediate outputs clearly:
Original text
Transcript (if audio)
Summary
Translated summary
Audio playback
🧪 Usage Guide
Open the app in your browser
Choose input type: Text or Audio
If audio → upload file (max 5 minutes)
Select target language
Click Process
View results:
Original text
Summary
Translated text
Play audio output
🌍 Deployment

The application is publicly available at:

👉 [Insert your deployed link here]

Hosted using: Hugging Face Spaces / Vercel

⚠️ Known Limitations
Maximum audio length: 5 minutes
Requires stable internet connection (API-based system)
Response time depends on Sunbird AI API latency
Limited to supported Ugandan languages only
📁 Project Structure
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
👨‍💻 Author

Developed as part of the Sunbird AI Internship Assessment

🔗 Repository & Deployment
GitHub Repo: https://github.com/
<your-username>/internship-assessment
Live App: https://<your-deployment-link>