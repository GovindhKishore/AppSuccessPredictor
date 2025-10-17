import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import joblib

df = pd.read_csv('data/preprocessed_data.csv')

X = df.drop(columns=["Installs"], axis=1)
y = np.log1p(df["Installs"]) # df["Installs"].map(np.log1p) works too

oh_encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)
ordinal_encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)

column_transformer = ColumnTransformer(transformers=[
    ("ohe", oh_encoder, ["Category"]),
    ("oe", ordinal_encoder, ["Content Rating"])
], remainder='passthrough', verbose=True, n_jobs=-1)

model = XGBRegressor(n_estimators=300, learning_rate=0.05, max_depth=6, random_state=42)

pipeline = Pipeline(steps=[
    ('preproc', column_transformer),
    ('model', model)
])

pipeline.fit(X, y)
print("fitted")

joblib.dump(pipeline, "models/xgboost_model.joblib")
print("model saved")
