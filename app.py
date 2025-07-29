import streamlit as st
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Function to split long text into smaller chunks
def split_text(text, max_words=500):
    words = text.split()
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

# Streamlit UI
st.title("Text Summarizer")
st.write("Enter a long article below to get a summary.")

# Text input
input_text = st.text_area("Enter your article here:")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Split text into chunks
        chunks = split_text(input_text)

        # Generate summary chunk by chunk
        summary = ""
        for chunk in chunks:
            summary += summarizer(chunk)[0]['summary_text'] + " "

        # Display the final summary
        st.subheader("Summary:")
        st.write(summary.strip())
