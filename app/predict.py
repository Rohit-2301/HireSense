import fitz
import joblib

model = joblib.load("model/resume_classifier.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def predict_role(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]


if __name__ == "__main__":
    pdf_path = "data/resumes/22BCS13677_ROHIT_resume (1).pdf"
    role = predict_role(pdf_path)
    print(f"\nPredicted Job Role: {role}")
