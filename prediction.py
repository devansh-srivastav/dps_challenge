import pandas as pd
from pycaret.regression import *

model = load_model('model_for_dps')


def get_prediction(year,month):
    df = pd.DataFrame([[int(year), int(month)]], columns=['JAHR', 'MONAT'])
    prediction = predict_model(model, data=df)
    prediction = prediction.astype({"Label": int})
    return pd.DataFrame([[prediction.iloc[:, 2].values[0]]], columns=['prediction'])

