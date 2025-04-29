from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ocr_utils import extract_text_from_image
from parser_utils import parse_lab_report_text

app = FastAPI()

@app.post("/get-lab-tests")
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        text = extract_text_from_image(image_bytes)
        lab_data = parse_lab_report_text(text)

        return JSONResponse(content={
            "is_success": True,
            "lab_tests": lab_data
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "is_success": False,
            "error": str(e)
        })
