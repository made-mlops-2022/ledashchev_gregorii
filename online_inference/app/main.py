from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import json
import joblib
import os


app = FastAPI()


class InputDataFrame(BaseModel):
    dataframe: str


@app.post("/predict")
async def create_item(input_data_frame: InputDataFrame):
    df = pd.DataFrame.from_dict(json.loads(input_data_frame.dataframe))
    path_to_model = os.path.join(
        os.getcwd(), r'app/models/linear_model_on_not_transformed.joblib'
    )
    model = joblib.load(path_to_model)
    prediction = model.predict(df)
    return ','.join(tuple(map(str, prediction)))


@app.post("/health")
def health():
    return 200
