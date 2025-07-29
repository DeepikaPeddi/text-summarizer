import streamlit as st
from transformers import pipeline

# Title
st.title(" Article Summarizer")
st.subheader("Summarize long articles using AI-powered NLP models!")

# Load the summarization model from Hugging Face (DistilBART)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Function to divide long text into smaller chunks that the model can handle
def split_text_into_chunks(text, max_words=500):
    words = text.split()
    return [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

# Text input area 
input_text = st.text_area(" Paste your article or paragraph below:", height=300)

# If user enters input and click summarize button
if st.button("Generate Summary"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        # Split the text into chunks
        chunks = split_text_into_chunks(input_text)

        final_summary = ""
        # summarizes each chunk by loop
        for part in chunks:
            summarized_part = summarizer(part)[0]['summary_text']
            final_summary += summarized_part + " "

        # summary display
        st.markdown(" Summary Output:")
        st.write(final_summary.strip())
