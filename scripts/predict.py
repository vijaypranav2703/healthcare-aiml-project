import pickle
import pandas as pd
model_path = '/content/drive/MyDrive/healthcare-project/models/rf_model_Billing_Amount.pkl'
enc_path = '/content/drive/MyDrive/healthcare-project/models/label_encoders.pkl'

model = pickle.load(open(model_path, 'rb'))
encoders = pickle.load(open(enc_path, 'rb'))

def prepare_input(df):
    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col].astype(str))
    return df

def predict(filepath):
    df = pd.read_csv(filepath)
    df = prepare_input(df)
    preds = model.predict(df)
    return preds

if __name__ == "__main__":
    print("Predict script loaded successfully.")
