import joblib
import numpy as np

model = joblib.load("models/stellar_classifier.pkl")
encoder = joblib.load("models/label_encoder.pkl")

def predict(u, g, r, i, z, redshift):
    u_g = u - g
    g_r = g - r
    r_i = r - i
    i_z = i - z

    X = np.array([[u,g,r,i,z,redshift,u_g,g_r,r_i,i_z]])
    pred = model.predict(X)[0]
    return encoder.inverse_transform([pred])[0]