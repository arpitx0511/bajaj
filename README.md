Report Extractor API
A FastAPI service that extracts lab test information (test name, value, reference range) from lab report images using OCR.
For Setup
```bash
git clone https://github.com/yourusername/lab-report-extractor.git
cd lab-report-extractor
pip install -r requirements.txt [here I've not added them but they include fastapi, uvicorn, pytesseract, pillow]
```
Also made a colab ML Model which can read/extract data from image and directly save it in a csv fromat post which we can work the extracted csv data using excel formulas. 
