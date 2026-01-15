import pandas as pd
from fastapi import FastAPI, File, UploadFile
from db import csv_validate, sort_by_danger_rate, validation_pydantic
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="terrorists")

@app.post("/top-threats")   
def top_threats(file: UploadFile | None = File(default=None)):
    df = csv_validate(file)
    df = pd.DataFrame(df)   
    df = sort_by_danger_rate(df)
    return validation_pydantic(df)

    

    

if __name__ == '__main__':
        uvicorn.run(app, host="localhost", port=8000)

