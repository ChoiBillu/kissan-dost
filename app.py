import os
import streamlit as st
from dotenv import load_dotenv

# Load local environment variables from .env
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="KisaanDost | کسان دوست - AgriGemma",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e5631;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4c6b54;
        margin-bottom: 1.5rem;
    }
    .badge-gemma {
        display: inline-block;
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #a5d6a7;
    }
    .urdu-text {
        direction: rtl;
        text-align: right;
        font-size: 1.1rem;
        line-height: 1.8;
    }
    .stCard {
        background-color: #f9fbf9;
        border-radius: 10px;
        padding: 18px;
        border: 1px solid #e0ede0;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Offline / Pre-computed fallback responses for bulletproof live demos
DEMO_RESPONSES = {
    "Cotton Leaf Curl Virus (CLCuV)": """### 🌾 تشخیص | Diagnosis & Cause
**بیماری:** کپاس کا پتہ مروڑ وائرس (Cotton Leaf Curl Virus - CLCuV)  
**وجہ:** یہ وائرس سفید مکھی (*Bemisia tabaci*) کے کاٹنے سے ایک پودے سے دوسرے پودے میں پھیلتا ہے۔

---

### 🩺 علامات | Symptoms Observed
* پتوں کے کنارے اوپر یا نیچے کی طرف مڑ جاتے ہیں۔
* پتوں کی رگیں موٹی اور ابھری ہوئی دکھائی دیتی ہیں۔
* شدید حملے میں پتے کے نچلے حصے پر چھوٹے چھوٹے پتے (Enations) بن جاتے ہیں اور پودے کا قد رک جاتا ہے۔

---

### 💊 فوری علاج اور اسپرے | Recommended Spray & Action
1. **سفید مکھی کا فوری خاتمہ:**
   - پائری پروکسی فن (Pyriproxyfen) یا ڈائی فینتھیوران (Diafenthiuron) کا اسپرے شام کے وقت کریں۔
   - یا ایسیفیٹ (Acephate) + ایسیٹامپرڈ (Acetamiprid) کا مخلوط اسپرے کریں۔
2. **پودوں کی قوت مدافعت:**
   - پوٹاش (SOP) اور زنک کا فولیر اسپرے کریں تاکہ پودا بحال ہو سکے۔

---

### 🛡️ احتیاطی تدابیر | Prevention & Best Practices
* کھیت کے ارد گرد سے جڑی بوٹیاں (خاص طور پر پپلی اور سوہانجنا) تلف کریں۔
* محکمہ زراعت پنجاب کی منظور شدہ وائرس کے خلاف قوتِ مدافعت رکھنے والی اقسام کاشت کریں۔""",

    "Wheat Yellow Rust": """### 🌾 تشخیص | Diagnosis & Cause
**بیماری:** گندم کی زرد / پیلی کنگی (Yellow Rust / Stripe Rust - *Puccinia striiformis*)  
**وجہ:** ٹھنڈا اور مرطوب موسم (10 تا 15 ڈگری سینٹی گریڈ) اور مسلسل دھند یا نمی۔

---

### 🩺 علامات | Symptoms Observed
* گندم کے پتوں پر رگوں کے ساتھ پیلے رنگ کی لکیریں (Stripes) بن جاتی ہیں۔
* ہاتھ لگانے پر زردی نما پاؤڈر ہاتھ پر چپک جاتا ہے۔
* ضیائی تالیف (Photosynthesis) رک جاتی ہے اور دانہ چھوٹا رہ جاتا ہے۔

---

### 💊 فوری علاج اور اسپرے | Recommended Spray & Action
1. **پھپھوندی کش اسپرے (Fungicide):**
   - ٹیبوکونازول (Tebuconazole) یا ایزوکسی سٹروبن + ڈائفینوکونازول 200 ملی لیٹر فی ایکڑ اسپرے کریں۔
   - بیماری کے ابتدائی پیچز (Hotspots) پر فوری فوکس کریں۔

---

### 🛡️ احتیاطی تدابیر | Prevention & Best Practices
* نائٹروجنی کھادوں (یوریا) کا غیر ضروری استعمال نہ کریں۔
* کنگی کے خلاف مزاحمتی اقسام جیسے کہ فیصل آباد 2008، اکبر 2019 وغیرہ کاشت کریں۔""",

    "Sugarcane Red Rot": """### 🌾 تشخیص | Diagnosis & Cause
**بیماری:** کماد کی سرخ سڑاند (Sugarcane Red Rot - *Colletotrichum falcatum*)  
**وجہ:** فنگل انفیکشن جو بیج یا مٹی اور آبپاشی کے پانی سے پھیلتا ہے۔

---

### 🩺 علامات | Symptoms Observed
* تنے کو بیچ سے چیرنے پر اندر سے گودا گہرا لال نکلتا ہے اور سفید دھبے نظر آتے ہیں۔
* تنے سے ترش اور الکوحل جیسی بو آتی ہے۔
* تیسرے اور چوتھے پتے اوپر سے سوکھنا شروع ہوتے ہیں۔

---

### 💊 فوری علاج اور اسپرے | Recommended Action
* متاثرہ پودوں کو جڑ سمیت اکھاڑ کر جلا دیں تاکہ بیماری کا پھیلاؤ روکا جا سکے۔
* کھیت میں پانی کھڑا نہ ہونے دیں اور نکاسی آب بہتر کریں۔

---

### 🛡️ احتیاطی تدابیر | Prevention & Best Practices
* متاثرہ فصل کا کماد بیج کے لیے ہرگز استعمال نہ کریں۔
* بیج کے ٹکڑوں کو کاشت سے قبل تھائیوفینیٹ میتھائل (Thiophanate-methyl) کے محلول میں ڈبوئیں۔"""
}

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/wheat.png", width=64)
    st.title("Settings & Controls")
    
    # Model Selection
    model_name = st.selectbox(
        "Gemma Model (Gemini API)",
        options=[
            "gemma-4-26b-a4b-it",
            "gemma-2-27b-it",
            "gemma-2-9b-it",
            "gemini-2.5-flash"
        ],
        index=0,
        help="Model specified in Hacktoberfest Faisalabad guidelines: Gemma 4 via Gemini API"
    )
    
    # API Key Input
    env_api_key = os.getenv("GEMINI_API_KEY", "")
    api_key_input = st.text_input(
        "Gemini API Key",
        value=env_api_key,
        type="password",
        help="Loads automatically from .env or paste here."
    )
    
    offline_toggle = st.checkbox("Offline / Demo Mode (Backup)", value=False, help="Uses instant local sample responses without Wi-Fi or API calls.")

    st.markdown("---")
    st.markdown("### 🏆 Hackathon Qualifications")
    st.caption("✅ **Track 1:** Best Open-Source AI Project")
    st.caption("✅ **Track 2:** Best Use of Gemma 4")
    st.caption("📜 **License:** Apache 2.0 (Gemma) / MIT (App)")
    st.caption("📍 **Venue:** Hack Day Faisalabad 2026")

# Header Section
st.markdown('<div class="main-header">🌾 KisaanDost | کسان دوست</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-header">AI-Powered Bilingual Crop Diagnostics & Advisory for Pakistani Farmers &bull; '
    '<span class="badge-gemma">Powered by Google Gemma 4</span></div>',
    unsafe_allow_html=True,
)

st.info("💡 **Our app helps Pakistani farmers diagnose crop diseases and get instant Urdu/English spray remedies using Gemma 4.**")

# One-Click Quick Demo Presets
st.markdown("##### ⚡ Quick Scenarios (Faisalabad & Punjab Region):")
col_p1, col_p2, col_p3 = st.columns(3)

preset_prompt = ""
with col_p1:
    if st.button("🌱 کپاس کا پتہ مروڑ (Cotton Leaf Curl)"):
        preset_prompt = "کپاس کے پتوں کے کنارے اوپر کی طرف مڑ رہے ہیں اور رگیں موٹی ہو گئی ہیں، سفید مکھی بھی نظر آ رہی ہے۔ کیا بیماری ہے اور کیا اسپرے کریں؟"
with col_p2:
    if st.button("🌾 گندم کی پیلی کنگی (Wheat Yellow Rust)"):
        preset_prompt = "Wheat crop leaves show yellow powdery stripes along the leaf blade during cool humid winter. Diagnose cause and treatment."
with col_p3:
    if st.button("🎋 کماد کی سرخ سڑاند (Sugarcane Red Rot)"):
        preset_prompt = "کماد کا تنا اندر سے لال نکل رہا ہے اور الکوحل جیسی بو آ رہی ہے۔ گنے سوکھ رہے ہیں۔ علاج بتائیں۔"

# Main Input Form
with st.form("farmer_query_form"):
    user_input = st.text_area(
        "Describe Crop Symptoms / فصل کی علامات بیان کریں:",
        value=preset_prompt,
        height=120,
        placeholder="مثال: گندم کے پتوں پر پیلے دھبے نظر آ رہے ہیں یا کپاس پر سفید مکھی کا حملہ ہے...",
    )
    
    col_btn, col_lang = st.columns([1, 3])
    with col_btn:
        submit_btn = st.form_submit_button("🔍 Diagnose with Gemma 4", type="primary")
    with col_lang:
        st.caption("Supports queries in **Roman Urdu**, **Nastaliq Urdu**, and **English**.")

# Inference Function
def call_gemma(prompt_text: str, key: str, chosen_model: str) -> str:
    system_instruction = (
        "You are 'KisaanDost' (کسان دوست), an expert agricultural scientist and crop pathologist tailored "
        "for farmers in Faisalabad and Punjab, Pakistan. "
        "When the user describes symptoms of any crop (Wheat, Cotton, Rice, Sugarcane, Maize, Mango, Vegetables): "
        "1. Identify the most probable disease or pest (both scientific and local names in Urdu and English). "
        "2. Detail the exact observed symptoms. "
        "3. Provide actionable, locally available chemical and organic remedies/sprays (e.g. active ingredients available in Pakistan). "
        "4. Provide practical preventive measures for subsequent seasons. "
        "Ensure the response is clear, respectful, easy to understand for a farmer, formatted with Markdown headers, "
        "and includes both English and clear Urdu explanations."
    )
    
    from google import genai
    client = genai.Client(api_key=key)
    
    full_prompt = f"{system_instruction}\n\nFarmer Query:\n{prompt_text}"
    response = client.models.generate_content(
        model=chosen_model,
        contents=full_prompt,
    )
    return response.text

# Execution & Presentation
if submit_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter crop symptoms or select one of the quick scenarios above.")
    else:
        with st.spinner("🌾 Gemma 4 is analyzing crop pathology and formulating remedies..."):
            # If offline toggle is active or no API key, use fallback gracefully
            if offline_toggle:
                # Match preset or generic fallback
                matched = None
                for key_name in DEMO_RESPONSES:
                    if key_name.split()[0].lower() in user_input.lower() or "کپاس" in user_input or "گندم" in user_input or "کماد" in user_input:
                        matched = DEMO_RESPONSES[key_name]
                        break
                result_text = matched or DEMO_RESPONSES["Cotton Leaf Curl Virus (CLCuV)"]
                st.caption("ℹ️ *Running in Stage Demo Mode (Zero-latency fallback)*")
            else:
                active_key = api_key_input.strip() or os.getenv("GEMINI_API_KEY", "")
                if not active_key:
                    st.error("❌ No Gemini API Key found. Please enter your key in the sidebar or create a `.env` file.")
                    st.stop()
                try:
                    result_text = call_gemma(user_input, active_key, model_name)
                except Exception as e:
                    st.error(f"Error querying Gemini API ({model_name}): {str(e)}")
                    st.info("💡 Pro-Tip for Demo: You can switch on 'Offline / Demo Mode' in the sidebar if Wi-Fi or API quota limits occur on stage.")
                    st.stop()

        # Display Structured Result
        st.success("✅ Analysis Complete!")
        st.markdown(f'<div class="stCard">{result_text}</div>', unsafe_allow_html=True)
        
        # Audio / Print Advice
        st.download_button(
            label="📥 Download Advisory Report (.txt)",
            data=result_text,
            file_name="kisaan_dost_crop_advisory.txt",
            mime="text/plain",
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #777; font-size: 0.85rem;">
    <b>KisaanDost</b> &bull; Built for Hacktoberfest Hack Day Faisalabad 2026 &bull; 
    Powered by <a href="https://ai.google.dev/gemma" target="_blank">Google Gemma 4</a> under Apache 2.0 &bull; 
    Source code licensed under MIT.
    </div>
    """,
    unsafe_allow_html=True,
)
