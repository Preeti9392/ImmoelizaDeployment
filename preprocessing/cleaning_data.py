import pandas as pd

Columns = [
    "type", "subtype", "bedroomCount", "toilet_and_bath", "province", "locality",
    "postcode", "habitableSurface", "buildingCondition", "facedeCount",
    "hasTerrace", "epcScore", "totalParkingCount"
]
categorical_columns = ["type", "subtype", "province", "locality", "postCode", "buildingCondition", "epcScore"]
def preprocess(input_data:dict):
    try:
        df=pf.Dataframe([input_data])
        for col in Columns:
            if col not in df.columns:
                df[col]=None
        for col in categorical_columns:
            df[col] = df[col].astype(str)
        return df
    except Exception as e:
        raise valurError(f"Error in preprocessing: {e}")

