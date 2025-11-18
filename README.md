# 🏥 Healthcare AIML Project  
**EDA • Supervised Learning • Anomaly Detection • AI Doctor Recommendation**

This project performs a complete end-to-end data science pipeline on a Healthcare dataset.  
It includes Exploratory Data Analysis (EDA), supervised machine learning, anomaly detection, and an AI-generated medical recommendation system.

---

# 📌 Project Overview

This project demonstrates:

- ✔ Data Cleaning & Preprocessing  
- ✔ Exploratory Data Analysis (EDA)  
- ✔ Supervised Learning (Predict Billing Amount)  
- ✔ Unsupervised Anomaly Detection (Isolation Forest)  
- ✔ AI Doctor Recommendation using patient attributes  
- ✔ Model Saving + Prediction Script  
- ✔ Clean project folder structure  

The dataset used is publicly available on Kaggle.

---

# 📁 Folder Structure

```
healthcare-project/
│
├── data/
│     └── cleaned_healthcare.csv
│
├── models/
│     ├── rf_model_Billing_Amount.pkl
│     └── label_encoders.pkl
│
├── notebooks/
│     └── healthcare_analysis.ipynb
│
├── scripts/
│     ├── predict.py
│     └── ai_recommendation.py
│
└── README.md
```

---

# 📊 Task 1 — Exploratory Data Analysis (EDA)

### Numerical Distributions Analyzed:
- Age  
- Billing Amount  
- Room Number  

### Categorical Distributions Visualized:
- Medical Condition  
- Admission Type  
- Medication  

The dataset contained **no missing values**, and all fields were clean and usable.

---

# 🤖 Task 2 — Supervised Machine Learning  
### 🧪 Goal: Predict Billing Amount

The original target `Test Results` contained **0% non-missing values**, so predicting it was impossible.  
Therefore, the project used **Billing Amount** as a practical regression target.

### Model Used:
- **Random Forest Regressor (200 trees)**  
- Label Encoding for categorical variables  
- Train/Test Split: 80/20  

### 📈 Evaluation Results
- **MAE:** 11,229.38  
- **RMSE:** 13,348.44  
- **R² Score:** 0.104  

> These metrics are expected because billing amounts vary widely and depend on unobserved hospital factors.  
> The purpose is to demonstrate the workflow, not to achieve perfect prediction accuracy.

---

# 🔍 Task 3 — Anomaly Detection (Billing Amount)

### Method:
- **Isolation Forest**  
- Contamination: 2%  

### Output:
- Anomalies = *Top 2% unusual billing records*  
- These may indicate rare cases, long hospital stays, or potential billing irregularities.

The project visualizes anomalies on a scatter plot for easy review.

---

# 🧠 Task 4 — AI Doctor Recommendation

A lightweight AI generator produces a doctor-style recommendation using:

- Age  
- Medical Condition  
- Medication  
- Predicted Billing Amount  

### Example Output:
```
AI Doctor Recommendation
------------------------
Patient Age: 57
Medical Condition: Diabetes
Medication: Aspirin
Predicted Billing Amount: $29,403.14

Recommendation:
The predicted billing amount suggests moderate care intensity.
Advise the patient to continue medication, maintain lifestyle habits,
and schedule a follow-up check within 2–4 weeks.

If symptoms worsen — such as fatigue, breathing issues,
irregular blood sugar levels, or unexpected side effects —
seek immediate clinical attention.
```

---

# 🛠 How to Run the Project

### 1️⃣ Clone the Repository
```
git clone <your-repo-url>
cd healthcare-project
```

### 2️⃣ Install Dependencies
```
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3️⃣ Open the Notebook
Run this notebook for full analysis:
```
notebooks/healthcare_analysis.ipynb
```

### 4️⃣ Use the Prediction Script
```
python scripts/predict.py
```

### 5️⃣ Generate AI Doctor Recommendation
```
python scripts/ai_recommendation.py
```

---

# 📦 Requirements
```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

# 🎯 Final Notes
This project demonstrates a complete AIML workflow suitable for:

- Portfolio  
- Job Applications  
- Data Science Learning  
- ML Engineering Practice  

Feel free to extend the project with:
- Feature engineering  
- Better regression models  
- SHAP explainability  
- Flask / Streamlit app  

---

# 📬 Contact
For questions or collaboration, feel free to open an issue or connect.

