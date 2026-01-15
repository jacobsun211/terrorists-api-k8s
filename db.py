import pandas as pd
from pydantic import BaseModel, Field, ValidationError
from typing import List
from fastapi import FastAPI, HTTPException, status


class Terrorist(BaseModel):
    name: str
    location: str 
    rate_danger: int = Field(...,ge=1, le=10)



app = FastAPI()
    

def csv_validate(file):
    if file is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No file provided",
        )

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid CSV file",
        )
    try:
        df = pd.read_csv(file)
        return df
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid CSV file",
        )


def sort_by_danger_rate(df):
    print(df)
    df = df.sort_values(by='danger_rate',ascending=False)
    sorted = df.head(5)
    return sorted

def validation():
    blueprint: List[Terrorist] = []

    try:
        for _, terrorist in sorted.iterrows():
            blueprint = Terrorist(
                name = str(terrorist["name"]),
                location = str(terrorist["location"]),
                danger_rate = int(terrorist["danger_rate"]),
            )   # not working...
            
            Terrorist.append(blueprint)
    except ValidationError as error:
        raise HTTPException(
            status_code = status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail = error.errors(),
        )
    
    # terrorists_list = []    
    # for terrorist in sorted:
    #     terrorists_dict = {}
    #     terrorists_dict["name"] = terrorist.name
    #     terrorists_dict["location"] = terrorist.location
    #     terrorists_dict["danger_rate"] = terrorist.danger_rate
    #     terrorists_list.append(terrorists_dict)
    

     








