import pandas as pd
from pydantic import BaseModel, Field, ValidationError
from typing import List
from fastapi import HTTPException, status


class Terrorist(BaseModel):
    name: str
    location: str 
    rate_danger: int = Field(...,ge=1, le=10)


    

def csv_validate(file):
    if file is None:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "you didnt enter any CSV file")

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "invalid CSV file, gotta end with .csv",)
    try:
        df = pd.read_csv(file) # this is working without api, but with api its crashing, idk why
    except Exception:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "invalid CSV file")
    return df

def sort_by_danger_rate(df):
    print(df)
    df = df.sort_values(by='danger_rate',ascending=False)
    sorted = df.head(5)
    return sorted

def validation_pydantic(sorted):
    blueprint: List[Terrorist] = []

    try:
        for _, terrorist in sorted.iterrows(): 
            blueprint = Terrorist(  # according to stack overflow and pydantic, something like that should work, i didnt got here so im not sure
                name = str(terrorist["name"]),   
                location = str(terrorist["location"]),
                danger_rate = int(terrorist["danger_rate"]))  
            
            Terrorist.append(blueprint)
    except ValidationError:
        raise HTTPException(
            status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail = "not valid content")
    
    terrorists_list = []   
    for terrorist in sorted:
        terrorists_dict = {}
        terrorists_dict["name"] = terrorist.name
        terrorists_dict["location"] = terrorist.location
        terrorists_dict["danger_rate"] = terrorist.danger_rate
        terrorists_list.append(terrorists_dict)
    

        return terrorists_list









