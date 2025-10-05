import streamlit as st
from transformers import pipeline

st.title("Tiny AI Text Summarizer")
text = st.text_area("Paste your article here")

if st.button("Summarize"):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length = 100,min_length=30, do_sample=False)
    st.subheader("Summary:")
    st.write(summary[0]['summary_text'])
