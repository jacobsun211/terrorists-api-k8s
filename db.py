# from csv_handeling import json_to_csv
import pandas as pd
from fastapi import FastAPI, File, UploadFile
import uvicorn
import csv
import codecs


app = FastAPI()


file = pd.read_csv('terrorists_data.csv')
df = pd.DataFrame(file)


app = FastAPI()
    
@app.post("/top-threats")
def upload_csv_threat(file: UploadFile = File(...)):
    csvReader = csv.DictReader(codecs.iterdecode(file.file))
    data = {}
    for rows in csvReader:             
        key = rows['name']  
        data[key] = rows  
    
    file.file.close()
    return data


if __name__ == '__main__':
        uvicorn.run(app, host="localhost", port=8000)