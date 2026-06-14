import pandas as pd

def clean_total_charges(df):
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )
    df["TotalCharges"] = df["TotalCharges"].fillna(
        df["TotalCharges"].median()
    )
    return df


def encode_target(df):
    df["Churn"] = df["Churn"].map({
        "Yes":1,
        "No":0
    })
    return df