```markdown
# HireSense – AI-Powered Resume Classifier

![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red?logo=streamlit&style=flat)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

An intelligent resume classification system that predicts the best-fit job role from a given resume PDF using NLP and machine learning. Upload a resume and instantly get its predicted career category.

---

## Live Demo

https://hiresense-peqy6gcp2srkufdpmh7mbp.streamlit.app/


---

## Preview

![alt text](image.png)


---

## Features

- Upload a resume PDF
- Extract text using PyMuPDF
- Classify into roles such as:
  - Data Scientist
  - Backend Developer
  - Frontend Developer
  - Full Stack Engineer
  - DevOps Engineer
- Built using Logistic Regression and TF-IDF
- Clean UI powered by Streamlit

---

## Tech Stack

| Area         | Tools & Libraries                                     |
|--------------|-------------------------------------------------------|
| Language     | Python                                                |
| ML/NLP       | `scikit-learn`, `pandas`, `joblib`, `TfidfVectorizer` |
| PDF Parsing  | `PyMuPDF` (`fitz`)                                    |
| UI           | `Streamlit`                                           |

---

## Folder Structure

```

HireSense/
├── app.py                # Streamlit UI
├── requirements.txt      # All dependencies
├── model/                # Trained model and vectorizer
├── preprocess/           # Scripts to process PDF/Kaggle data
├── data/                 # labels.csv and resume text
├── .gitignore
└── README.md

````

---

## How to Run Locally

### Install Requirements

```bash
pip install -r requirements.txt
````

### Launch the App

```bash
streamlit run app.py
```

---

## How to Train Your Own Model

If you want to retrain:

```bash
python preprocess/convert_kaggle_dataset.py
python model/train_model.py
```

---

## Deployment

You can deploy this app on:

* [Streamlit Cloud](https://streamlit.io/cloud)
* [Render](https://render.com)
* [HuggingFace Spaces](https://huggingface.co/spaces)


