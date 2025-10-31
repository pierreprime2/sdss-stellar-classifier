import joblib
import numpy as np
import sys
import pandas as pd

if len(sys.argv) != 7:
    print("Usage: python predict.py <u> <g> <r> <i> <z> <redshift>")
    sys.exit(1)

# Load model + encoder
model = joblib.load("notebooks/stellar_classifier.pkl")
encoder = joblib.load("notebooks/label_encoder.pkl")

# Expect 6 raw magnitudes + 1 redshift from CLI
u, g, r, i, z, redshift = map(float, sys.argv[1:7])

# Compute features same as training
u_g = u - g
g_r = g - r
r_i = r - i
i_z = i - z

X = pd.DataFrame([{
    "u": u,
    "g": g,
    "r": r,
    "i": i,
    "z": z,
    "redshift": redshift,
    "u_g": u_g,
    "g_r": g_r,
    "r_i": r_i,
    "i_z": i_z
}])

pred = model.predict(X)[0]
label = encoder.inverse_transform([pred])[0]

proba = model.predict_proba(X)[0]
classes = encoder.inverse_transform(model.classes_)

print(f"Prediction: {label}")
print("Probabilities:")
# zip function joins 2 tuples together
for c, p in zip(classes, proba):
    print(f" {c}: {p:.3f}")