"""
====================================
 Model Training Module
====================================
Author: João
Date: 2025-08-20

Description:
------------
This module handles the process of inferencing with the model. 

Usage:
------
- Import as a module:
    from model_training import train_model

- Run as a script for quick automated tests:
    python -m training.model_training

Functions:
----------
- model_load() -> model
    Read the model from .pkl file.

- model_prediction(model, features) -> predictions
    Using the loaded model and the features makes the prediction.

"""

import pandas as pd
import joblib
from sklearn import tree

# Loading the best model
def model_load():

    model = joblib.load('deployment/model.pkl')
    return model

# Make the prediction
def model_prediction(model, features):

    # Applying scaler
    scaler = joblib.load('deployment/scaler.pkl')
    scaled_features = scaler.transform(features)

    predictions = model.predict(scaled_features)
    return predictions

     
# =================
# Standalone Script
# =================

"""
Functions:
----------
- Call other libs to read, clean, and create the feature store 
- Train the model using Ml Flow library to store model artifacts
- Train an decision tree, testing multiple parameters
"""

if __name__ == "__main__":

    try:
        best_model = model_load()
        print("✅ best model loaded")
    except ValueError as e:
        print("❌ failed load model")
        print(f"Error caught: {e}")

    test_features =  pd.DataFrame({
        "vehicle_type"           : [7],
        "fastagid"               : [1],
        "vehicle_dimensions"     : [1],
        "transaction_amount_cat" : [0],
        "discount"               : [0],
        "no_change"              : [1],
        "penalty"                : [0]    
        })

    try:
        test_predictions = model_prediction(model = best_model, features= test_features)
        print("✅ predictions made")
    except ValueError as e:
        print("❌ failed make predictions")
        print(f"Error caught: {e}")

    print()
    print("The tested prediction is: " + str(test_predictions))
