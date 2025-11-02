[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![ML Pipeline](https://img.shields.io/badge/Type-ML%20Classification-green)]()
[![Dataset](https://img.shields.io/badge/Data-SDSS%20DR17-orange)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

# SDSS Stellar Classifier

Training project to get started in Python Machine Learning and data pipelines using real astrophysical catalog data (SDSS DR17).

This repository builds a stellar classifier capable of distinguishing **STAR**, **GALAXY**, and **QSO** objects from photometric magnitudes and redshift.

📦 **Training data:**  
https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17

> ⚠️ **Requires Python 3.11**  
Gradio / pydantic-core are not yet compatible with Python 3.14.

## 🌐 Live Demo (HuggingFace)

Try the model in your browser:

👉 https://huggingface.co/spaces/<your-username>/<your-space-name>

Enter SDSS photometric magnitudes (`u, g, r, i, z`) and `redshift` → the app predicts **STAR**, **GALAXY**, or **QSO**.

Example input:
- u: 18.3  
- g: 17.9  
- r: 17.5  
- i: 17.3  
- z: 17.2  
- redshift: 0.002

## Dependencies

| Package | Purpose |
|--------|---------|
| **numpy** | numerical computing |
| **pandas** | tabular data manipulation |
| **matplotlib / seaborn** | visualization & EDA |
| **scikit-learn** | ML pipeline + RandomForest |
| **joblib** | saving model + label encoder |
| **jupyter** | notebook experimentation |
| **gradio** | small local web UI for inference |

Install with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python predict.py <u> <g> <r> <i> <z> <redshift>
```

## 📘 SDSS Dataset Column Reference

| Column | Type | Meaning | Keep for ML? | Notes |
|:--------|:------|:---------|:-------------|:------|
| **obj_ID** | int | Unique identifier of the object in the SDSS catalog | ❌ | Just an index; no physical meaning |
| **ra** | float | Right Ascension – celestial longitude (0–360°) | ✅ | Spatial coordinate on the sky |
| **dec** | float | Declination – celestial latitude (−90° to +90°) | ✅ | Spatial coordinate on the sky |
| **u** | float | Magnitude in ultraviolet band (355 nm) | ✅ | Used to compute colors (e.g. `u−g`) |
| **g** | float | Magnitude in green band (475 nm) | ✅ | — |
| **r** | float | Magnitude in red band (622 nm) | ✅ | — |
| **i** | float | Magnitude in near-infrared band (763 nm) | ✅ | — |
| **z** | float | Magnitude in infrared band (905 nm) | ✅ | — |
| **run_ID** | int | Observation run number | ❌ | Internal SDSS metadata |
| **rerun_ID** | int | Indicates reprocessing version | ❌ | Internal SDSS metadata |
| **cam_col** | int | Camera column (1–6) that captured the image | ❌ | Instrumental info only |
| **field_ID** | int | Field number on the sky in that run | ❌ | Technical metadata |
| **spec_obj_ID** | float | Spectroscopic observation ID | ❌ | Unique to that spectrum; no physical info |
| **fiber_ID** | int | Fiber number (1–640) used for spectroscopy | ❌ | Instrumental; not related to object type |
| **plate** | int | Spectroscopic plate identifier | ❌ | Internal observation metadata |
| **MJD** | int | Modified Julian Date — date of observation | ❌ | Temporal info; irrelevant to class |
| **redshift** | float | Measure of how much light is stretched (distance indicator) | ✅ | Key physical feature (galaxies, quasars → higher redshift) |
| **class** | string | Object type (`STAR`, `GALAXY`, `QSO`) | 🎯 | Target variable to predict |

✅ → keep as input feature  
❌ → drop before training  
🎯 → target (label)

**Features used (`X`):** `['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift']`  
**Target (`y`):** `['class']`

## 🧭 Overall Project Steps

| Step | Name | Goal |
|------|------|------|
| **1** | **Data Loading & Inspection** | Import CSV, explore shape, columns, and class distribution |
| **2** | **Data Cleaning & Preprocessing** | Remove useless columns, handle missing values, select useful features |
| **3** | **Exploratory Data Analysis (EDA)** | Visualize relationships (e.g. magnitudes vs redshift, class separation) |
| **4** | **Feature Engineering** | Build new features like color indices (`u-g`, `g-r`, …) |
| **5** | **Model Training** | Fit ML models (RandomForest, SVM, etc.) |
| **6** | **Evaluation & Tuning** | Check accuracy, confusion matrix, improve |
| **7** | **Documentation & Versioning** | Notebook cleanup, README, push to git |

## 🚀 Future Work

- Hyperparameter tuning & CV
- Add model confidence visualizations
- Deploy to Hugging Face Spaces
- Add support for FITS photometric input
- Try SVM / XGBoost / shallow neural net