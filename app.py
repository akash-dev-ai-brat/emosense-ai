# import streamlit as st
# from PIL import Image
# import numpy as np
# import cv2
# from deepface import DeepFace

# # ─── Page Config ───────────────────────────────────────────────
# st.set_page_config(
#     page_title="Emotion Detector | Akash Nath",
#     page_icon="🎭",
#     layout="centered"
# )

# # ─── Header ────────────────────────────────────────────────────
# st.title("🎭 Emotion Detector")
# st.markdown("**Built by Akash Nath** | AI & Data Science Project")
# st.markdown("Upload a photo and the AI will detect the emotions on every face!")
# st.divider()

# # ─── Emotion colors for display ────────────────────────────────
# EMOTION_COLORS = {
#     "happy":     ("#FFD700", "😄"),
#     "sad":       ("#6495ED", "😢"),
#     "angry":     ("#FF4500", "😠"),
#     "surprise":  ("#FF69B4", "😲"),
#     "fear":      ("#9370DB", "😨"),
#     "disgust":   ("#32CD32", "🤢"),
#     "neutral":   ("#A9A9A9", "😐"),
# }

# # ─── Upload Section ────────────────────────────────────────────
# uploaded_file = st.file_uploader(
#     "Upload an image (JPG or PNG)",
#     type=["jpg", "jpeg", "png"]
# )

# if uploaded_file is not None:
#     image = Image.open(uploaded_file).convert("RGB")
#     img_array = np.array(image)

#     st.subheader("📸 Your Image")
#     st.image(image, use_column_width=True)

#     # ─── Run Detection ─────────────────────────────────────────
#     with st.spinner("🤖 Analyzing emotions... (first run may take 30 sec to download model)"):
#         try:
#             img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
#             results = DeepFace.analyze(
#                 img_bgr,
#                 actions=['emotion'],
#                 enforce_detection=False,
#                 silent=True
#             )

#             # DeepFace returns list or dict — normalize to list
#             if isinstance(results, dict):
#                 results = [results]

#             st.divider()
#             st.subheader(f"✅ Detected {len(results)} face(s)")

#             for i, face in enumerate(results):
#                 emotions = face["emotion"]
#                 dominant = face["dominant_emotion"]
#                 score = emotions[dominant]

#                 color, emoji = EMOTION_COLORS.get(dominant.lower(), ("#FFFFFF", "🙂"))

#                 st.markdown(f"### Face {i+1} {emoji}")

#                 # Dominant emotion highlight box
#                 st.markdown(
#                     f"""
#                     <div style="background-color:{color}22; border-left: 5px solid {color};
#                     padding: 12px; border-radius: 8px; margin-bottom: 10px;">
#                         <h3 style="margin:0; color:{color}">
#                             {emoji} {dominant.upper()} &nbsp;
#                             <span style="font-size:16px; color:#333">
#                                 ({score:.1f}% confidence)
#                             </span>
#                         </h3>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#                 # All emotion scores as progress bars
#                 st.markdown("**All emotion scores:**")
#                 sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
#                 for emotion, conf in sorted_emotions:
#                     _, emo_emoji = EMOTION_COLORS.get(emotion.lower(), ("", ""))
#                     st.progress(min(conf / 100, 1.0), text=f"{emo_emoji} {emotion.capitalize()}: {conf:.1f}%")

#                 if i < len(results) - 1:
#                     st.divider()

#         except Exception as e:
#             st.error(f"❌ Error: {str(e)}")
#             st.info("💡 Try a clearer photo with a visible face and good lighting.")

# # ─── Footer ────────────────────────────────────────────────────
# st.divider()
# st.markdown(
#     "<p style='text-align:center; color:gray'>Made with ❤️ using Python, DeepFace & Streamlit</p>",
#     unsafe_allow_html=True
# )

import streamlit as st
from PIL import Image
import numpy as np
import cv2
from deepface import DeepFace

# ─── Page Config ───────────────────────────────────────────────
st.set_page_config(
    page_title="EmoSense AI | Akash Nath",
    page_icon="🎭",
    layout="wide"
)

# ─── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main { background-color: #0f0f1a; }

    .hero-box {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid #ffffff15;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    .hero-title {
        font-size: 3em;
        font-weight: 700;
        background: linear-gradient(90deg, #e94560, #0f3460, #533483);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .hero-sub {
        color: #aaaacc;
        font-size: 1.1em;
        margin-top: 10px;
    }

    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #e94560, #533483);
        color: white;
        padding: 4px 14px;
        border-radius: 20px;
        font-size: 0.8em;
        font-weight: 600;
        margin-top: 12px;
    }

    .card {
        background: #1a1a2e;
        border-radius: 16px;
        padding: 24px;
        border: 1px solid #ffffff15;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        margin-bottom: 16px;
    }

    .emotion-card {
        border-radius: 16px;
        padding: 20px 24px;
        margin: 12px 0;
        border: 1px solid #ffffff20;
    }

    .dominant-label {
        font-size: 2em;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .confidence-text {
        font-size: 0.95em;
        opacity: 0.8;
        margin-top: 4px;
    }

    .bar-container {
        background: #ffffff15;
        border-radius: 10px;
        height: 10px;
        margin: 6px 0 12px 0;
        overflow: hidden;
    }

    .bar-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.5s ease;
    }

    .emotion-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2px;
    }

    .emotion-label { font-size: 0.88em; color: #ccccee; }
    .emotion-pct   { font-size: 0.88em; color: #aaaacc; }

    .tab-section {
        background: #1a1a2e;
        border-radius: 16px;
        padding: 6px;
        display: flex;
        gap: 8px;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: #555577;
        font-size: 0.85em;
        padding: 30px 0 10px 0;
    }

    .stButton > button {
        background: linear-gradient(90deg, #e94560, #533483) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 28px !important;
        font-weight: 600 !important;
        font-size: 1em !important;
        width: 100% !important;
        transition: all 0.3s !important;
    }

    .stButton > button:hover {
        opacity: 0.85 !important;
        transform: translateY(-1px) !important;
    }

    div[data-testid="stFileUploader"] {
        background: #1a1a2e;
        border: 2px dashed #533483;
        border-radius: 16px;
        padding: 20px;
    }

    .tip-box {
        background: #0f3460;
        border-radius: 12px;
        padding: 14px 18px;
        color: #aaaacc;
        font-size: 0.88em;
        border-left: 4px solid #e94560;
        margin-top: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ─── Emotion config ────────────────────────────────────────────
EMOTIONS = {
    "happy":    {"emoji": "😄", "color": "#FFD700", "bar": "#FFD700"},
    "sad":      {"emoji": "😢", "color": "#6495ED", "bar": "#6495ED"},
    "angry":    {"emoji": "😠", "color": "#FF4500", "bar": "#FF4500"},
    "surprise": {"emoji": "😲", "color": "#FF69B4", "bar": "#FF69B4"},
    "fear":     {"emoji": "😨", "color": "#9370DB", "bar": "#9370DB"},
    "disgust":  {"emoji": "🤢", "color": "#32CD32", "bar": "#32CD32"},
    "neutral":  {"emoji": "😐", "color": "#A9A9A9", "bar": "#A9A9A9"},
}

def get_emotion_info(name):
    return EMOTIONS.get(name.lower(), {"emoji": "🙂", "color": "#ffffff", "bar": "#ffffff"})

def run_analysis(img_bgr):
    return DeepFace.analyze(
        img_bgr,
        actions=['emotion'],
        enforce_detection=False,
        silent=True
    )

def render_results(results):
    if isinstance(results, dict):
        results = [results]

    st.markdown(f"<div class='card'><b style='color:#e94560'>✅ {len(results)} face(s) detected</b></div>", unsafe_allow_html=True)

    for i, face in enumerate(results):
        emotions   = face["emotion"]
        dominant   = face["dominant_emotion"].lower()
        info       = get_emotion_info(dominant)
        score      = emotions[dominant]

        # Dominant emotion card
        st.markdown(f"""
        <div class='emotion-card' style='background:{info["color"]}18; border-color:{info["color"]}44;'>
            <div class='dominant-label' style='color:{info["color"]}'>{info["emoji"]} {dominant.upper()}</div>
            <div class='confidence-text' style='color:{info["color"]}'>Confidence: {score:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

        # All emotion bars
        sorted_em = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
        bars_html = ""
        for emo, val in sorted_em:
            ei = get_emotion_info(emo)
            bars_html += f"""
            <div class='emotion-row'>
                <span class='emotion-label'>{ei["emoji"]} {emo.capitalize()}</span>
                <span class='emotion-pct'>{val:.1f}%</span>
            </div>
            <div class='bar-container'>
                <div class='bar-fill' style='width:{min(val,100)}%; background:{ei["bar"]};'></div>
            </div>
            """
        st.markdown(f"<div class='card'>{bars_html}</div>", unsafe_allow_html=True)

        if i < len(results) - 1:
            st.markdown("---")

# ─── HERO ──────────────────────────────────────────────────────
st.markdown("""
<div class='hero-box'>
    <div class='hero-title'>🎭 EmoSense AI</div>
    <div class='hero-sub'>Real-time Facial Emotion Detection powered by Deep Learning</div>
    <div class='badge'>Built by Akash Nath · AI & Data Science</div>
</div>
""", unsafe_allow_html=True)

# ─── TABS ──────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["📁  Upload Image", "📷  Webcam Capture"])

# ══════════════════════════════════════════════════════════════
# TAB 1 — Upload
# ══════════════════════════════════════════════════════════════
with tab1:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("#### 📤 Upload a Photo")
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        st.markdown("""
        <div class='tip-box'>
            💡 <b>Tips for best results:</b><br>
            • Use a clear, well-lit photo<br>
            • Face should be facing forward<br>
            • Works with multiple faces too!
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if uploaded_file:
            image     = Image.open(uploaded_file).convert("RGB")
            img_array = np.array(image)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            with st.spinner("🤖 Analyzing emotions..."):
                try:
                    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                    results = run_analysis(img_bgr)
                    render_results(results)
                except Exception as e:
                    st.error(f"❌ {str(e)}")
        else:
            st.markdown("""
            <div class='card' style='text-align:center; padding:60px 20px; color:#555577;'>
                <div style='font-size:3em'>🖼️</div>
                <div style='margin-top:10px'>Upload an image to see results</div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# TAB 2 — Webcam
# ══════════════════════════════════════════════════════════════
with tab2:
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("#### 📷 Webcam Emotion Scan")
        st.markdown("<p style='color:#aaaacc; font-size:0.9em'>Click the button below to capture from your webcam and analyze your emotion!</p>", unsafe_allow_html=True)

        webcam_img = st.camera_input("", label_visibility="collapsed")

        st.markdown("""
        <div class='tip-box'>
            💡 <b>How to use:</b><br>
            • Allow camera access when prompted<br>
            • Look at the camera and click capture<br>
            • Try different expressions!
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if webcam_img:
            image     = Image.open(webcam_img).convert("RGB")
            img_array = np.array(image)
            st.image(image, caption="Captured Photo", use_column_width=True)

            with st.spinner("🤖 Reading your emotion..."):
                try:
                    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
                    results = run_analysis(img_bgr)
                    render_results(results)
                except Exception as e:
                    st.error(f"❌ {str(e)}")
        else:
            st.markdown("""
            <div class='card' style='text-align:center; padding:60px 20px; color:#555577;'>
                <div style='font-size:3em'>📷</div>
                <div style='margin-top:10px'>Capture a photo to detect your emotion</div>
            </div>
            """, unsafe_allow_html=True)

# ─── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class='footer'>
    🎭 EmoSense AI &nbsp;·&nbsp; Built with Python, DeepFace & Streamlit &nbsp;·&nbsp;
    <b style='color:#e94560'>Akash Nath</b> · AI & Data Science
</div>
""", unsafe_allow_html=True)