#from google.colab import files
#uploaded = files.upload()  //to upload zip files

!pip install pytesseract opencv-python-headless pandas
!apt-get install -y tesseract-ocr

import cv2
import pytesseract
import pandas as pd
import os
from google.colab import files
from PIL import Image

#upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]  # use the first uploaded file

image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
print("🔍 Raw OCR Text:\n", text[:500])  # print first 500 chars for preview

import re


lab_data = []
for line in text.split('\n'):
    line = line.strip()
    if not line or len(line.split()) < 3:
        continue

    match = re.match(r'(.+?)\s+([\d.]+)\s+([<>=\d.-]+\s*[-–toTO]*\s*[<>=\d.]+)', line, re.IGNORECASE)
    if match:
        test_name = match.group(1).strip()
        value = match.group(2).strip()
        reference = match.group(3).strip()
        lab_data.append({
            "lab_test_name": test_name,
            "lab_test_value": value,
            "bio_reference_range": reference
        })

df = pd.DataFrame(lab_data)
csv_filename = "extracted_lab_data.csv"
df.to_csv(csv_filename, index=False)
print("\n✅ CSV generated with", len(df), "rows.")

# to download csv
files.download(csv_filename)
