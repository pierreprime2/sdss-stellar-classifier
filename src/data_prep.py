import pandas as pd

def load_data(path="data/star_classification.csv"):
    df = pd.read_csv(path)

    df["u_g"] = df["u"] - df["g"]
    df["g_r"] = df["g"] - df["r"]
    df["r_i"] = df["r"] - df["i"]
    df["i_z"] = df["i"] - df["z"]

    features = ["u","g","r","i","z","redshift","u_g","g_r","r_i","i_z"]
    X = df[features]
    y = df["class"]

    return X, y