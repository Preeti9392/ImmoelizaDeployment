# predict/prediction.py
import pickle

with open('model/catboost_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

    def predict(preprocessed_data):
        try:
            with open('model/catboost_price_prediction_model.pkl', 'rb') as f:
                model = pickle.load(f)
            prediction= model.predict(preprocessed_data)
            return prediction
            
        except Exception as e:
            Raise ValueError(f"Error in predict: {e}")

