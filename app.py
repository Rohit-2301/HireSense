import streamlit as st
import fitz
import joblib


model = joblib.load("model/resume_classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def extract_text(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text


st.set_page_config(page_title="HireSense: AI Resume Classifier", page_icon="🤖")

st.title("HireSense: AI-Powered Resume Classifier")
st.markdown("Upload a resume PDF and get the predicted job role using NLP + ML ")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Reading and analyzing resume..."):
        resume_text = extract_text(uploaded_file)
        vector = vectorizer.transform([resume_text])
        prediction = model.predict(vector)[0]

    st.success(f"Predicted Role: **{prediction}**")
