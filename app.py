from utils.cv_booster import cvBooster
from fastapi import FastAPI

app = FastAPI()

@app.post("/", status_code=200)
def main(data: dict):
    cv = cvBooster(data.get("path"))
    #cv.re_write(cv.education, "expand")
    return {"raw_text":cv.text}