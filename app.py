import torch
import streamlit as st
from transformers import pipeline
import textwrap

#title
st.title("Article Summarizer")
st.write("Paste any long article and get a short, clean summary.")

# Input box
text = st.text_area("Paste your article here", height=300)

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to split long text into smaller chunks
def split_text(text, max_words=500):
    sentences = text.split('. ')
    chunks, chunk = [], ""
    for sentence in sentences:
        if len((chunk + sentence).split()) <= max_words:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    if chunk:
        chunks.append(chunk.strip())
    return chunks

# Generate summary on button click
if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            chunks = split_text(text)
            summaries = []
            for chunk in chunks:
                summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
                summaries.append(summary)

            final_summary = " ".join(summaries)
            st.success("✅ Summary Generated:")
            st.write(final_summary)

