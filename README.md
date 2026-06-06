<div align="center">

<!-- Replace with your actual GIF — record with OBS or Streamlit's screen capture -->
<img src="assets/screenshot3-happy-webcam.png" alt="EmoSense AI Demo" width="800"/>

# 🎭 EmoSense AI

### Real-time Facial Emotion Detection using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/akash-dev-ai-brat/emosense-ai)

**EmoSense AI** detects human facial emotions in real time from webcam or video input using a CNN-based deep learning model. It classifies 7 emotions — angry, disgust, fear, happy, neutral, sad, and surprise — with live probability scores displayed on a Streamlit dashboard.

[Live Demo](#) · [Report Bug](https://github.com/akash-dev-ai-brat/emosense-ai/issues) · [Request Feature](https://github.com/akash-dev-ai-brat/emosense-ai/issues)

</div>

---

## 📌 Table of Contents
- [About the Project](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🧠 About the Project <a name="about"></a>

Emotion recognition is a core capability in human-computer interaction, mental health monitoring, and surveillance systems. EmoSense AI is a production-oriented proof-of-concept that demonstrates how a CNN trained on the FER-2013 dataset can be integrated into a real-time, interactive web application.

This project covers the full pipeline: data → model → deployment.

---

## ✨ Features <a name="features"></a>

- 📸 **Real-time webcam emotion detection** — processes each frame live using OpenCV
- 🧩 **7-class emotion classification** — Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- 📊 **Live probability bar chart** — see confidence scores per emotion update in real time
- 🖼️ **Image upload mode** — analyze emotions from a static image
- ⚡ **Lightweight & fast** — optimized for CPU inference, no GPU required

---

## 🛠️ Tech Stack <a name="tech-stack"></a>

| Layer | Technology |
|-------|-----------|
| Frontend / UI | Streamlit |
| Deep Learning | TensorFlow / Keras (CNN) |
| Face Detection | OpenCV Haar Cascade |
| Dataset | FER-2013 (Kaggle) |
| Language | Python 3.10+ |

---

## 📁 Project Structure <a name="project-structure"></a>

```
emosense-ai/
├── app.py                  # Streamlit app — main entry point
├── model/
│   └── emotion_model.h5    # Trained CNN model weights
├── utils/
│   └── detector.py         # Face detection + emotion inference logic
├── assets/
│   └── demo.gif            # Demo GIF for README
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start <a name="quick-start"></a>

**1. Clone the repository**
```bash
git clone https://github.com/akash-dev-ai-brat/emosense-ai.git
cd emosense-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` — allow camera access when prompted.

---

## ⚙️ How It Works <a name="how-it-works"></a>

```
Webcam Frame
     │
     ▼
OpenCV Face Detection (Haar Cascade)
     │
     ▼
Crop & Grayscale → Resize to 48×48px
     │
     ▼
CNN Model Inference (FER-2013 trained)
     │
     ▼
Softmax Output → 7 Emotion Probabilities
     │
     ▼
Streamlit UI — Live Overlay + Bar Chart
```

The CNN architecture uses 4 convolutional blocks followed by global average pooling and a softmax classifier, trained on the FER-2013 dataset (~35,887 labelled face images).

---

## 📸 Screenshots <a name="screenshots"></a>

### Upload Image Mode
![Upload Mode](assets/screenshot1-upload-mode.png)

### Emotion Detection Results
| Angry Detection | Happy — 100% Confidence | Surprise Detection |
|:-:|:-:|:-:|
| ![Angry](assets/screenshot2-angry-detection.png) | ![Happy](assets/screenshot3-happy-webcam.png) | ![Surprise](assets/screenshot4-surprise-webcam.png) |

### Webcam Capture Interface
![Webcam UI](assets/screenshot5-webcam-ui.png)

---

## 🔮 Future Improvements <a name="future-improvements"></a>

- [ ] Multi-face detection and tracking
- [ ] Emotion trend graph over time (for sessions)
- [ ] Fine-tune on AffectNet for higher accuracy
- [ ] Export emotion logs to CSV

---

## 📄 License <a name="license"></a>

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/akash-dev-ai-brat">Akash Nath</a> · 
  <a href="https://www.linkedin.com/in/akash-nath-5aa816293/">LinkedIn</a>
</div>
