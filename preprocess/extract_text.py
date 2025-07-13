import os
import fitz
import pandas as pd


def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def extract_all_texts(resume_folder="data/resumes", output_folder="data/text", label_csv="data/labels.csv"):
    os.makedirs(output_folder, exist_ok=True)
    df = pd.read_csv(label_csv)

    for filename in df['filename']:
        pdf_path = os.path.join(resume_folder, filename)
        out_path = os.path.join(
            output_folder, filename.replace(".pdf", ".txt"))

        if os.path.exists(pdf_path):
            text = extract_text_from_pdf(pdf_path)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
        else:
            print(f"File not found: {pdf_path}")


if __name__ == "__main__":
    extract_all_texts()
