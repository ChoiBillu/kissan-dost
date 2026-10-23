# 🌾 KisaanDost (کسان دوست) — AgriGemma

> **"Our app helps Pakistani farmers diagnose crop diseases and get instant, actionable spray remedies in Urdu and English using Gemma 4."**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Powered by Gemma 4](https://img.shields.io/badge/Powered%20by-Gemma%204%20(Apache%202.0)-blue)](https://ai.google.dev/gemma)
[![Streamlit App](https://img.shields.io/badge/Streamlit-UI-FF4B4B)](https://streamlit.io/)
[![Hackathon](https://img.shields.io/badge/Hacktoberfest-Hack%20Day%20Faisalabad%202026-green)](#)

---

## 📌 Submission Information
- **Event**: Hacktoberfest Hack Day Faisalabad 2026
- **Target Challenges**:
  - 🏆 **Best Open-Source AI Project**
  - 🌟 **Best Use of Gemma 4**
- **AI Model**: Google Gemma 4 (`gemma-4-26b-a4b-it`) via Google GenAI / Gemini API
- **Model License**: [Gemma License (Apache 2.0)](https://ai.google.dev/gemma/terms)
- **Application License**: [MIT License](LICENSE)

---

## 🎯 The Problem
Agriculture is the backbone of Pakistan’s economy, especially across Punjab and the Faisalabad division (known for wheat, cotton, sugarcane, and citrus). However:
1. Smallholder farmers often struggle to identify crop diseases (e.g. *Cotton Leaf Curl Virus*, *Wheat Yellow Rust*, *Sugarcane Red Rot*) before irreversible damage occurs.
2. Agricultural extension officers are not always reachable in remote villages.
3. Diagnostic literature and apps are predominantly in English and filled with complex scientific jargon, locking out local farmers who communicate in Urdu or Punjabi.

## 💡 The Solution: KisaanDost
**KisaanDost** leverages **Gemma 4** to provide an instant, bilingual (Urdu & English) agricultural diagnostic and advisory assistant:
- **Natural Language Input**: Farmers can describe symptoms in Roman Urdu, Nastaliq Urdu, or English.
- **Accurate Pathology**: Gemma analyzes symptoms, identifies both common and scientific names, and points out underlying causal vectors (e.g., whitefly).
- **Localized Spray Recommendations**: Delivers actionable chemical (active ingredients available in Pakistan) and organic treatments with recommended dosage.
- **Stage-Resilient Offline Mode**: Features pre-loaded regional presets for instant, zero-latency demonstration during pitches.

---

## 🏗️ Architecture

```
                       +-------------------------------+
                       |        Streamlit Web UI       |
                       | (Urdu & English Interfaces)   |
                       +---------------+---------------+
                                       |
                                       | Farmer Symptoms
                                       v
                       +---------------+---------------+
                       |     System Pathologist Prompt |
                       | (Agrarian Pathology Guidance) |
                       +---------------+---------------+
                                       |
                                       | Gemini API
                                       v
                       +---------------+---------------+
                       |       Google Gemma 4          |
                       |    (gemma-4-26b-a4b-it)       |
                       +---------------+---------------+
                                       |
                                       | Structured Bilingual Advice
                                       v
                       +---------------+---------------+
                       | Diagnosis | Sprays | Prevention|
                       +-------------------------------+
```

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/kisaan-dost.git
cd kisaan-dost
```

### 2. Install Dependencies
Ensure you have Python 3.10+ installed:
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the root directory (based on `.env.example`):
```bash
cp .env.example .env
```
Add your Gemini API key from [Google AI Studio](https://aistudio.google.com/):
```env
GEMINI_API_KEY=your_actual_api_key_here
```
*(Note: Your API key is safe — `.env` is ignored by `.gitignore` and never committed).*

### 4. Run the Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🎬 3-Minute Demo Guide (For Presenters)

| Section | Time | Talking Points |
| :--- | :---: | :--- |
| **Problem** | 20s | Over 60% of Pakistan's population relies on agriculture, yet crop diseases like cotton leaf curl virus destroy millions of rupees in yields every year because farmers can't get fast, localized advice in Urdu. |
| **Live Demo** | 90s | Click preset: *"کپاس کا پتہ مروڑ"* or type a symptom. Gemma diagnoses the viral infection, tags the whitefly vector, and prescribes Pyriproxyfen spray and preventive steps in both clear Urdu and English. |
| **How Gemma is Used** | 30s | We query Gemma 4 (`gemma-4-26b-a4b-it`) via the Gemini API using an agronomy system prompt to extract structured pathology and local treatment formulas. |
| **What's Next** | 20s | Expanding to WhatsApp voice note integration so farmers can simply speak in Punjabi/Urdu and receive audio advisory notes directly on their phones. |

---

## 📄 License & Attribution
- **Application Code**: Licensed under the [MIT License](LICENSE).
- **Underlying Model**: Built with [Gemma 4](https://ai.google.dev/gemma) released by Google under the **Apache 2.0 License**.
