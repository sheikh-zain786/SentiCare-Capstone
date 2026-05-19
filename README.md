<div align="center">
  <h1>🧠 SentiCare</h1>
  <h3>Voice-Based AI for Mental Health Support</h3>

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
  ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
  ![Hugging Face](https://img.shields.io/badge/🤗_Spaces-Live_Demo-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
  ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
  ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
  ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

  <p>
    <strong>
      <a href="https://wajeehaijaz-senticare.hf.space/">🔗 Live Demo</a> •
      <a href="#-key-features">Key Features</a> •
      <a href="#-tech-stack">Tech Stack</a> •
      <a href="#-installation">Installation</a> •
      <a href="#-usage">Usage</a> •
      <a href="#-architecture">Architecture</a> •
      <a href="#-team--credits">Team</a>
    </strong>
  </p>
</div>

---

## 📖 About

SentiCare is a **capstone project** developed at the **University of Sargodha** (2025–2026). It is a **voice-first, multi-modal emotional support platform** that listens to *how* you speak not just what you say and provides empathetic, evidence-based mental health support.

The system combines three powerful signals:

1. **Acoustic voice biomarkers** (pitch, tone, rhythm)
2. **Text-based emotion classification** via a fine-tuned Transformer model
3. **Self-reported wellness scores** (mood, sleep, energy)

…and fuses them into a **single, coherent assessment** of anxiety, stress, and depression severity then responds through a supportive, CBT-informed therapeutic chatbot.

> ⚠️ **Important:** SentiCare is an **emotional support & self-assessment tool**. It does **not** diagnose mental illness, prescribe medication, or replace professional therapy.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎙️ **Voice Check-In** | Record up to 30 seconds of speech; emotions are extracted from acoustic features (pitch, tone, rhythm). |
| 🧠 **ML-Powered Fusion** | Combines voice biomarkers, text sentiment, and questionnaire answers to predict anxiety, stress & depression levels. |
| 💬 **Therapeutic Chatbot** | Empathetic, CBT-informed AI companion with conversation memory and intent-aware responses. |
| 📊 **Emotion Tracking** | Visual trend charts (Recharts) that help users monitor their emotional journey over time. |
| 🔊 **Bilingual Text-to-Speech** | Bot responses read aloud in **English** and **Urdu** via Microsoft Edge neural voices. |
| 🧘 **Therapy Cards** | Structured coping exercises (breathing, grounding) rendered as interactive UI cards. |
| 🔐 **Privacy-First** | No audio is permanently stored; session data lives only in memory (optional MongoDB logging). |

---

## 🛠️ Tech Stack

### 🎨 Frontend

![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![Recharts](https://img.shields.io/badge/Recharts-22b5bf?style=flat-square&logo=recharts&logoColor=white)

### ⚙️ Backend

![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Edge-TTS](https://img.shields.io/badge/Edge--TTS-0078D7?style=flat-square&logo=microsoft-edge&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)

### 🤖 Machine Learning

![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Hugging Face](https://img.shields.io/badge/🤗_Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Librosa](https://img.shields.io/badge/Librosa-1E3A5F?style=flat-square&logo=python&logoColor=white)

### 🚀 Deployment & Tools

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face_Spaces-FFD21E?style=flat-square&logo=huggingface&logoColor=black)

---

## 🌐 Live Demo

Experience SentiCare right now:

👉 **[wajeehaijaz-senticare.hf.space](https://wajeehaijaz-senticare.hf.space/)**

The live deployment includes **user authentication**, persistent session history, and the complete voice-to-therapy pipeline all hosted on **Hugging Face Spaces**.

---

## 📁 Repository Structure

```text
SentiCare-Capstone/
│
├── Datasets/                    # CSV datasets (anxiety, stress, depression)
├── Design Document/             # Detailed design document (Word + PDF)
├── Presentation/                # Final project presentation (PPTX)
├── SentiCare Diagrams/          # UML diagrams (Class, ER, Sequence, Use Case)
├── SentiCare SRS/               # Software Requirements Specification
├── artifacts/                   # Trained ML model pipelines (.joblib)
│   ├── anxiety_classification/
│   ├── depression_classification/
│   ├── stress_classification/
│   ├── anxiety_model.joblib
│   └── preprocessor.joblib
│
├── senticare-frontend/          # React application
│   ├── src/
│   │   ├── components/          # VoiceCheckIn, TherapyCards, ChatBot, Charts
│   │   └── App.jsx              # Main React entry point
│   └── package.json
│
├── backend/                     # Python Flask server
│   ├── app.py                   # API routes and server entry point
│   ├── emotion_analyzer.py      # Core fusion engine (voice + text + survey)
│   ├── conversation_engine.py   # Chatbot state, scoring, response generation
│   ├── nlu.py                   # Natural Language Understanding (intent, sentiment)
│   ├── logger.py                # Session logging utility
│   ├── chatbot/                 # Chatbot response logic
│   ├── components/              # Reusable backend modules
│   └── database/                # MongoDB integration
│
├── notebooks/                   # Jupyter notebooks (ML experimentation)
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container configuration
└── README.md                    # You are here!
```

---

## 🚀 Installation

### Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **Git**

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/sheikh-zain786/SentiCare-Capstone.git
cd SentiCare-Capstone

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python -m backend.app            # → http://localhost:5000
```

### Frontend Setup

```bash
cd senticare-frontend
npm install
npm start                        # → http://localhost:3000
```

> Make sure the backend is running **before** using the frontend.

---

## 📖 Usage

1. Open the frontend in your browser (`http://localhost:3000`).
2. **Allow microphone access** when prompted by the browser.
3. Click **Start Voice Check-In** and speak for up to 30 seconds, describe how you're feeling.
4. Answer the follow-up questionnaire about your **mood, sleep, and energy levels**.
5. The AI **fuses your voice emotion with your answers** and displays a preliminary assessment.
6. Continue the conversation in the chat, the bot **remembers your context** and offers personalised CBT-based support.
7. Use the **emotion trend chart** to track your well-being over time.

---

## 🏗️ Architecture

### High-Level Data Flow

```
┌─────────────────────────────────────────────────────────┐
│                     USER BROWSER                         │
│  ┌─────────────────┐          ┌───────────────────────┐  │
│  │  Voice Recorder  │          │  Questionnaire Form   │  │
│  │  (MediaRecorder) │          │  (Mood, Sleep, Energy)│  │
│  └────────┬────────┘          └───────────┬───────────┘  │
│           │                               │              │
│           └───────────┬───────────────────┘              │
│                       │                                  │
└───────────────────────┼──────────────────────────────────┘
                        │  POST /voice-intro
                        ▼
┌─────────────────────────────────────────────────────────┐
│                    FLASK API SERVER                       │
│  ┌─────────────────────────────────────────────────────┐ │
│  │                    app.py                            │ │
│  │  • /voice-intro   (voice check-in + fusion)         │ │
│  │  • /chat          (text-based conversation)          │ │
│  │  • /tts           (text-to-speech generation)        │ │
│  └──────────┬──────────────────────────────────────────┘ │
│             │                                             │
│  ┌──────────▼──────────────────────────────────────────┐ │
│  │               AI / ML Pipeline                       │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌───────────┐  │ │
│  │  │ Speech-to-   │  │ Text Emotion │  │  Voice     │  │ │
│  │  │ Text (STT)   │  │ Classifier   │  │  Emotion   │  │ │
│  │  │              │  │(DistilRoBERTa│  │  Analyzer  │  │ │
│  │  └──────┬───────┘  └──────┬───────┘  └─────┬─────┘  │ │
│  │         │                 │                │         │ │
│  │         └─────────┬───────┴────────────────┘         │ │
│  │                   ▼                                  │ │
│  │         ┌──────────────────┐                         │ │
│  │         │  FUSION LAYER    │                         │ │
│  │         │  (voice + text   │                         │ │
│  │         │   + survey)      │                         │ │
│  │         └────────┬─────────┘                         │ │
│  │                  ▼                                   │ │
│  │    ┌──────────────────────────┐                      │ │
│  │    │  Conversation Engine     │                      │ │
│  │    │  (CBT responses, memory) │                      │ │
│  │    └────────────┬─────────────┘                      │ │
│  │                 │                                    │ │
│  └─────────────────┼────────────────────────────────────┘ │
│                    ▼                                      │
│  ┌─────────────────────────────────────┐                 │
│  │  Edge-TTS (English & Urdu voices)    │                 │
│  └─────────────────────────────────────┘                 │
│                                                          │
│  ┌─────────────────────────────────────┐                 │
│  │  MongoDB (optional session storage)  │                 │
│  └─────────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────┘
```

### How the Fusion Works

The `EmotionAnalyzer` class in `backend/emotion_analyzer.py` is the heart of SentiCare. It:

1. Receives **text emotion scores** from the DistilRoBERTa model (anxious, sad, stressed, etc.).
2. Receives **voice biomarker scores** from acoustic analysis (voice-based anxiety, depression indicators).
3. Receives **self-reported questionnaire scores** (mood, sleep, energy on a 1–5 scale).
4. Applies a **weighted fusion algorithm** to combine all three modalities.
5. Outputs a **final severity score (Low / Medium / High)** for anxiety, stress, and depression.

> 🔧 **Bug Fix Highlight:** An earlier version of the code had a critical bug where the voice-based "depressed" signal was not being included in the final depression fusion score. This caused the frontend to always display **Depression: 0%** even when the user's voice clearly indicated depressive symptoms. The fix correctly maps `voice_scores['depressed_voice']` into the weighted depression calculation. See `emotion_analyzer.py` for details.

---

## 📊 Datasets Used

| Dataset | Purpose | Source |
|---|---|---|
| Student Mental Health Survey | Anxiety, stress, depression indicators | [Kaggle](https://www.kaggle.com/datasets/sonia22222/students-mental-health-assessments) |
| RAVDESS / TESS | Voice emotion training (acted speech) | Public academic datasets |

---

## 📚 Project Documentation

The repository includes comprehensive documentation:

| Document | Location | Description |
|---|---|---|
| **SRS Document** | `SentiCare SRS.pdf` | Software Requirements Specification |
| **Design Document** | `Design Document/` | Detailed architecture & design decisions |
| **UML Diagrams** | `SentiCare Diagrams/` | Class, ER, Sequence, Use Case, Activity diagrams |
| **Presentation** | `SentiCare_Presentation.pptx` | Final capstone defense presentation |

---

## 👥 Team & Credits

### Project Supervisor
- **Dr. Saad Razaq** – *University of Sargodha*

### Project Manager
- **Dr. Illyas** – *University of Sargodha*

### Developers

| Name | GitHub |
|---|---|
| **Esha Gulzar** | [@Esha-gulzar](https://github.com/Esha-gulzar) |
| **Wajeeha Ijaz** | [@WajeehaIjaz](https://github.com/WajeehaIjaz) |
| **Sheikh Zain** | [@sheikh-zain786](https://github.com/sheikh-zain786) |

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- **Hugging Face Spaces** – for providing free, accessible model hosting and cloud deployment
- **Microsoft Edge-TTS** – for high-quality, multilingual neural text-to-speech
- **Student Mental Health Survey (Kaggle)** – for the clinical screening dataset
- **RAVDESS & TESS** – for the voice emotion recognition datasets

---

<div align="center">
  <p>Made with ❤️ by the SentiCare Team</p>
  <p>University of Sargodha • 2025–2026</p>
</div>
