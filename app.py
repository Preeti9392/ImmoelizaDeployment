# app.py
from fastapi import FastAPI#, HTTPException
from pydantic import BaseModel
from typing import Optional, str,dict,int,float
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

app = FastAPI()

class input_data(BaseModel):
    type: str
    subtype: str
    bedroomCount: float
    toilet_and_bath: float
    province: str
    locality: str
    postcode: int
    habitableSurface: float
    buildingCondition: Optional[str] = None
    facedeCount: Optional[float] = None
    hasTerrace: bool
    epcScore: Optional[str] = None
    totalParkingCount: float

@ app.get("/")
def health():
    return{"status":"alive"}

@ app.get("/predict")
def data_format_predictions():
    return{"message":"The post request should be in json format"}

@ app.post("/predict")
def get_predictions(json_input:input_data):
    try:
        
        preprocessed_data=preprocess(json_input)
        price=predict(preprocessed_data:dict)
        return{"prediction":price, "status_code":200}
    except Exception as e:
            Raise ValueError(f"Error in predict: {e}")
        

