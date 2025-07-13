import os
import pandas as pd

df = pd.read_csv("data/resumes/UpdatedResumeDataSet.csv")

os.makedirs("data/text", exist_ok=True)

labels = []

for i, row in df.iterrows():
    resume_text = row['Resume']
    label = row['Category']

    filename_txt = f"resume_{i}.txt"
    with open(f"data/text/{filename_txt}", "w", encoding="utf-8") as f:
        f.write(resume_text)

    labels.append([filename_txt.replace(".txt", ".pdf"), label])

labels_df = pd.DataFrame(labels, columns=["filename", "label"])
labels_df.to_csv("data/labels.csv", index=False)

print("Kaggle data converted to .txt files and labels.csv generated!")
