# ❤️ Heart Disease Prediction — Supervised Machine Learning Classification

A fully **self-developed and self-deployed** end-to-end Machine Learning project that predicts whether a patient is likely to have heart disease, based on clinical and diagnostic parameters. The project covers the complete ML lifecycle — from raw data cleaning and exploratory data analysis, to model training/selection, and finally deployment as an interactive web application using **Streamlit**.

🔗 **Live App:** *[Add your Streamlit Cloud link here]*

---

## 👨‍💻 Developed By

**M. Rayyan Shehzad**

This project was independently conceptualized, built, trained, evaluated, and deployed — covering data preprocessing, model experimentation, and full-stack deployment of the final solution.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide, and early detection can significantly improve patient outcomes. This project uses a **Supervised Learning Classification** approach to predict the presence of heart disease based on 11 clinical features such as chest pain type, resting blood pressure, cholesterol level, ECG results, and more.

The final trained model is deployed as an interactive Streamlit web app, where users can input patient details through a simple UI (with built-in explanations for medical terms) and get an instant prediction.

---

## 🧠 Problem Statement

> Given a set of medical attributes about a patient, predict whether the patient has heart disease (`1`) or not (`0`).

This is a **binary classification problem**, solved using supervised machine learning algorithms trained on labeled patient data.

---

## 📊 Dataset

The dataset used is the **Heart Failure Prediction Dataset**, containing **918 patient records** with the following features:

| Feature | Description |
|---|---|
| `Age` | Age of the patient |
| `Sex` | Gender (M/F) |
| `ChestPainType` | Type of chest pain (ATA, NAP, ASY, TA) |
| `RestingBP` | Resting blood pressure (mm Hg) |
| `Cholesterol` | Serum cholesterol (mg/dl) |
| `FastingBS` | Fasting blood sugar > 120 mg/dl (1/0) |
| `RestingECG` | Resting electrocardiogram results (Normal, ST, LVH) |
| `MaxHR` | Maximum heart rate achieved |
| `ExerciseAngina` | Exercise-induced angina (Y/N) |
| `Oldpeak` | ST depression induced by exercise |
| `ST_Slope` | Slope of the peak exercise ST segment (Up, Flat, Down) |
| `HeartDisease` | **Target variable** — 1 = disease present, 0 = no disease |

The target class distribution was found to be well balanced, avoiding the need for resampling techniques.

---

## 🔍 Exploratory Data Analysis (EDA) & Data Cleaning

A key highlight of this project is that it goes **beyond surface-level cleaning** — the dataset had no missing or duplicate values on the surface, but a deeper investigation revealed **logically invalid entries**:

- **`RestingBP = 0`** → Physiologically impossible for a living patient. Identified as a data-entry placeholder for missing values, since these fields were mandatory during collection.
- **`Cholesterol = 0`** → Also flagged as invalid/missing-data placeholders (0 had the single highest frequency in the column, which is medically implausible).

### 🩺 How this was handled:
Instead of blindly dropping or ignoring these rows, invalid `0` values were replaced with the **mean of valid, non-zero entries** for that feature — since the remaining distribution was approximately normal, making the mean a statistically sound imputation choice.

This step reflects a core principle followed throughout the project:

> **A dataset can look "clean" (no NaNs, no duplicates) and still be logically incorrect. Understanding domain context is essential before preprocessing.**

Other EDA steps performed:
- Distribution analysis of numerical features (Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak)
- Categorical feature analysis (Sex, ChestPainType, FastingBS) against the target using count plots
- Boxplots & violin plots to study relationships between numeric features and `HeartDisease`
- Correlation heatmap to study inter-feature relationships

---

## ⚙️ Data Preprocessing

1. **One-Hot Encoding** — All categorical columns (`Sex`, `ChestPainType`, `RestingECG`, `ExerciseAngina`, `ST_Slope`) were converted into numeric dummy variables.
2. **Dummy Variable Trap Handling** — Dropped `Sex_F` column to avoid redundancy.
3. **Feature Scaling** — Applied `StandardScaler` to numerical columns (`Age`, `RestingBP`, `Cholesterol`, `MaxHR`) to standardize them for distance-based algorithms.
4. **Train-Test Split** — 80/20 split with `random_state=42` for reproducibility.

---

## 🤖 Model Building & Selection

Multiple supervised classification algorithms were trained and benchmarked on the same preprocessed & scaled data:

| Model | Notes |
|---|---|
| Logistic Regression | Baseline linear model |
| K-Nearest Neighbors (KNN) | Distance-based classifier |
| Naive Bayes (Gaussian) | Probabilistic classifier |
| Decision Tree Classifier | Non-linear, interpretable model |
| **Support Vector Machine (SVM)** | ✅ **Best performing model — selected for deployment** |

### 📈 Evaluation Metrics Used
Since this is a medical diagnosis use case, **Recall** was prioritized over Accuracy, following the principle:

> **Heart Disease → Recall > F1 ≈ Precision > Accuracy**

(Missing an actual heart disease case — a false negative — is far more costly than a false positive in a screening context.)

Metrics computed for each model:
- Accuracy Score
- Recall Score
- F1 Score

After comparison, the **Support Vector Machine (SVM)** classifier achieved the best overall performance and was selected as the final production model.

---

## 💾 Model Serialization

The final artifacts were exported using **Joblib** for deployment:

| File | Purpose |
|---|---|
| `SVM_heart.pkl` | Final trained SVM classification model |
| `scaler.pkl` | Fitted `StandardScaler` object — ensures new inputs are scaled identically to training data |
| `columns.pkl` | Ordered list of feature columns used during training — ensures correct column alignment during inference |

This ensures that any new, unseen input goes through the **exact same preprocessing pipeline** (encoding → column alignment → scaling) as the training data before being passed to the model.

---

## 🖥️ Web Application (Streamlit)

The trained model is deployed via a clean, user-friendly **Streamlit** interface that allows anyone — including users with no medical background — to input patient details and get an instant prediction.

### Key Features of the App:
- 🧾 Interactive input widgets (sliders, dropdowns, number inputs) for all 9 clinical parameters
- ℹ️ **Built-in tooltips (`help` parameter)** on every input field, explaining medical terms in plain language (e.g., what "ST Slope" or "Oldpeak" means) — making the tool accessible to non-technical/non-medical users
- ⚡ Real-time prediction on button click
- ✅ / ⚠️ Clear, color-coded result messages, along with a reminder to consult a healthcare professional (the tool is a decision-support aid, **not** a diagnostic replacement)

### App Workflow:
1. User enters patient details through the sidebar/form
2. Inputs are converted into a one-hot encoded feature vector matching the training schema
3. Missing expected columns are auto-filled with `0`
4. Feature vector is scaled using the saved `scaler.pkl`
5. Model (`SVM_heart.pkl`) predicts the outcome
6. Result is displayed to the user

---

## 📁 Project Structure

```
├── app.py                                       # Streamlit web application
├── Heart_Disease_Prediction_Data_Pipeline.ipynb # Full EDA, cleaning & model training notebook
├── SVM_heart.pkl                                # Trained SVM model
├── scaler.pkl                                   # Fitted StandardScaler
├── columns.pkl                                  # Feature column order
├── requirements.txt                             # Python dependencies
└── README.md                                    # Project documentation
```

---

## 🛠️ Tech Stack

- **Language:** Python
- **Data Handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (Logistic Regression, KNN, Naive Bayes, Decision Tree, SVM)
- **Model Persistence:** Joblib
- **Deployment / UI:** Streamlit
- **Hosting:** Streamlit Community Cloud

---

## 🚀 Running the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown in the terminal (usually `http://localhost:8501`) in your browser.

---

## ⚠️ Disclaimer

This application is developed for **educational and demonstrative purposes only**. It is **not** a certified medical diagnostic tool and should **never** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider regarding any medical condition.

---

## 🙋 About This Project

This entire project — from data cleaning and logical-consistency checks, to EDA, model experimentation, evaluation, and deployment — was **independently designed, built, and deployed** as a complete demonstration of the supervised classification workflow in real-world, imperfect data conditions.

If you find this project useful or interesting, feel free to ⭐ star the repository!
