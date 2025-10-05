# 🧠 Tiny AI Text Summarizer

A simple **AI-powered web app** that summarizes any article or paragraph into a few concise sentences.

Built using **Streamlit** for the interface and **Hugging Face Transformers** for natural language processing.

---

## 🚀 Tech Stack
- **Python**
- **Streamlit** – to build the web interface  
- **Hugging Face Transformers** – to load the summarization model  
- **Model Used:** [`facebook/bart-large-cnn`](https://huggingface.co/facebook/bart-large-cnn)

---

## 🧩 How It Works
1. The user pastes any article or paragraph.  
2. The app uses the **BART model** from Hugging Face to generate a short, meaningful summary.  
3. The summarized text is displayed instantly.

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py