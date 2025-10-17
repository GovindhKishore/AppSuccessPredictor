import pandas as pd
import numpy as np
import joblib

pipeline = joblib.load("models/xgboost_model.joblib")
installs_and_weights = pd.read_csv("data/installs_and_weights.csv")

def get_weighted_percentile(install_prediction, installs=installs_and_weights["Installs"],
                            weights=installs_and_weights["weights"]):
    subset_installs = installs[installs <= install_prediction[0]] # install_prediction is a numpy array
    corresponding_weights = weights.loc[subset_installs.index]

    weighted_percentile = (corresponding_weights.sum() / weights.sum()) * 100

    return weighted_percentile

def predict(category, size, price, content_rating, year):
    input_data = {
        "Category": [category], "Size": [size],
        "Price": [price], "Content Rating": [content_rating],
        "year": [year]
    }

    input_df = pd.DataFrame(input_data)
    log_prediction = pipeline.predict(input_df)
    installs_pred = np.expm1(log_prediction)

    percentile_pred = get_weighted_percentile(installs_pred)

    return percentile_pred, installs_pred[0]



