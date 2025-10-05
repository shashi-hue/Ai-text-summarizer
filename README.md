# 🧠 Tiny AI Text Summarizer

A simple **AI-powered web app** that summarizes any article or paragraph into a few concise sentences.

Built using **Streamlit** for the interface and **Hugging Face Transformers** for natural language processing.

---

## 🚀 Tech Stack
- **Python**
- **Streamlit** – for building the interactive web UI  
- **Hugging Face Transformers** – for NLP model integration  
- **Model Used:** [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)

---

## 🧩 How It Works
1. The user pastes any article or paragraph into the text box.  
2. The app uses the **BART (Bidirectional and Auto-Regressive Transformers)** model from Hugging Face to generate a concise summary.  
3. The summarized output appears instantly in the browser.

---

## 🌐 Live Demo  
👉 **Try it here:** [https://huggingface.co/spaces/shashi-hue/tiny-ai-text-summarizer](https://huggingface.co/spaces/shashi-hue/tiny-ai-text-summarizer)

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
