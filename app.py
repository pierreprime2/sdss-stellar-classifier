import gradio as gr
import joblib
import pandas as pd

# Load model and encoder
model = joblib.load("notebooks/stellar_classifier.pkl")
encoder = joblib.load("notebooks/label_encoder.pkl")

def classify_stellar(u, g, r, i, z, redshift):
    # Compute engineered features
    u_g = u - g
    g_r = g - r
    r_i = r - i
    i_z = i - z

    X = pd.DataFrame([{
        "u": u, "g": g, "r": r, "i": i, "z": z, "redshift": redshift,
        "u_g": u_g, "g_r": g_r, "r_i": r_i, "i_z": i_z
    }])

    pred = model.predict(X)[0]
    label = encoder.inverse_transform([pred])[0]
    proba = model.predict_proba(X)[0]

    # Output as dict: {"STAR": 0.95, "GALAXY": 0.04, "QSO": 0.01}
    return {encoder.inverse_transform(model.classes_)[i]: float(p) for i, p in enumerate(proba)}

inputs = [
    gr.Number(label="u magnitude"),
    gr.Number(label="g magnitude"),
    gr.Number(label="r magnitude"),
    gr.Number(label="i magnitude"),
    gr.Number(label="z magnitude"),
    gr.Number(label="redshift")
]

app = gr.Interface(
    fn=classify_stellar,
    inputs=inputs,
    outputs=gr.Label(),
    title="SDSS Stellar Classifier",
    description="Enter photometric magnitudes and redshift to classify the object as STAR, GALAXY, or QSO."
)

app.launch()