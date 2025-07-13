# 🤖 HireSense – AI-Powered Resume Classifier

[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?style=flat&logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> An intelligent resume classification system that predicts the best-fit job role from a given resume PDF using NLP + Machine Learning.

---

## Live Demo

**Try it here**:  
🔗 [https://hiresense-ops-9vcpskiru6pnfz9ehp.streamlit.app](https://hiresense-ops-9vcpskiru6pnfz9ehp.streamlit.app)

---

## Preview
![alt text](image.png)

---

## Features

- Upload a resume PDF  
- Extracts clean text using PyMuPDF  
- Predicts job role using Logistic Regression  
- Supports job categories like:
  - Data Scientist
  - Backend Developer
  - Frontend Developer
  - Full Stack Engineer
  - DevOps Engineer  
- Clean interactive UI powered by Streamlit

---

## 🛠 Tech Stack

| Area         | Tools & Libraries                                           |
|--------------|-------------------------------------------------------------|
| Language     | Python                                                      |
| ML/NLP       | `scikit-learn`, `pandas`, `joblib`, `TfidfVectorizer`       |
| PDF Parsing  | `PyMuPDF` (`fitz`)                                          |
| Web UI       | `Streamlit`                                                 |

---

## 📁 Folder Structure

```bash
HireSense/
├── app.py                # Streamlit App
├── requirements.txt      # Dependencies
├── model/                # Trained ML model + vectorizer
├── preprocess/           # Data processing scripts
├── data/                 # labels.csv, resume texts
├── .gitignore
└── README.md
