import pandas as pd
from pycaret.regression import *

model = load_model('model_for_dps')


def get_prediction(year,month):
    df = pd.DataFrame([[int(year), int(month)]], columns=['JAHR', 'MONAT'])
    prediction = predict_model(model, data=df)
    return int(prediction.values[0][2])

