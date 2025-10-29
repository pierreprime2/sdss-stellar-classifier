# SDSS Stellar Classifier

Training project to get started in Python Machine Learning and Data management.

## Dependencies

pandas : Python data analysis toolkit.
numpy : Array computing in Python
matplotlib : Visualizations
seaborn : statistic data vizualization
scikit-learn : scientific toolkit
jupyter : data notebooks

### 📘 SDSS Dataset Column Reference

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

### 🧭 Overall Project Steps

| Step | Name | Goal |
|------|------|------|
| **1** | **Data Loading & Inspection** | Import CSV, explore shape, columns, and class distribution |
| **2** | **Data Cleaning & Preprocessing** | Remove useless columns, handle missing values, select useful features |
| **3** | **Exploratory Data Analysis (EDA)** | Visualize relationships (e.g. magnitudes vs redshift, class separation) |
| **4** | **Feature Engineering** | Build new features like color indices (`u-g`, `g-r`, …) |
| **5** | **Model Training** | Fit ML models (RandomForest, SVM, etc.) |
| **6** | **Evaluation & Tuning** | Check accuracy, confusion matrix, improve |
| **7** | **Documentation & Versioning** | Notebook cleanup, README, push to git |