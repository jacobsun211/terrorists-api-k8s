import pandas as pd
from fastapi import FastAPI, File, UploadFile
from db import csv_validate, sort_by_danger_rate, validation
import uvicorn

from fastapi import FastAPI

app = FastAPI(title="terrorists")


@app.post("/top-threates")
def upload_file(file: UploadFile = File(...)):
    df = csv_validate(file)
    df = pd.DataFrame(df)   
    df = sort_by_danger_rate(df)
    return validation

    

    

if __name__ == '__main__':
        uvicorn.run(app, host="localhost", port=8000)

