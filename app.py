import streamlit as st
from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # device=-1 forces CPU
st.title(" AI Text Summarizer")
text = st.text_area("Enter your text:", height=200)

if st.button("Summarize"):
    summary = summarizer(text, max_length=60, min_length=30, do_sample=False)
    st.subheader(" Summary:")
    st.write(summary[0]['summary_text'])
