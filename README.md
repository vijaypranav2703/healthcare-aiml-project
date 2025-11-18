# 🏥 Healthcare AIML Project  
**EDA • Machine Learning • Anomaly Detection • AI Medical Recommendation System**

This project implements a full **end-to-end healthcare analytics pipeline** including data cleaning, exploratory data analysis, predictive modeling, anomaly detection, and an AI doctor-style recommendation generator.

---

## 📌 Project Features

### ✔ Data Cleaning  
- Handling missing values  
- Label encoding for categorical variables  
- Preparing dataset for ML  

### ✔ Exploratory Data Analysis (EDA)  
- Age distribution  
- Billing amount analysis  
- Medical condition frequency  
- Admission type & medication insights  
- Room number & hospital statistics  

### ✔ Supervised Machine Learning  
- Regression model using **Random Forest Regressor**  
- Predicts *Billing Amount*  
- Metrics used: MAE, RMSE, R²  

### ✔ Unsupervised Learning  
- **Isolation Forest** for anomaly detection in billing amounts  
- Detects unusually high/low bills  

### ✔ AI Doctor Recommendation System  
Generates custom recommendations based on:  
- Age  
- Medical condition  
- Medication  
- Predicted billing amount  

---

## 📁 Folder Structure

```
healthcare-aiml-project/
│
├── data/
│   ├── cleaned_healthcare.csv
│   └── DATASET_LINK.txt   ← (Google Drive download link)
│
├── models/
│   ├── rf_model_Billing_Amount.pkl
│   └── label_encoders.pkl
│
├── notebooks/
│   └── healthcare_analysis.ipynb
│
├── scripts/
│   ├── predict.py
│   └── ai_recommendation.py
│
└── README.md
```

---

## 📦 Dataset & Download Link (Important)

GitHub cannot store large files (>25 MB).  
Therefore, all data and ML models are available on **Google Drive**.

### 📥 Download from Google Drive:
🔗https://drive.google.com/drive/folders/1mn_dEBIL6ArEKozHDkvrp4gy-hZ3qJQ1?usp=drive_link

### Included in Drive:
- `cleaned_healthcare.csv`
- `rf_model_Billing_Amount.pkl`
- `label_encoders.pkl`
- All scripts & notebooks used in development

After downloading, place them inside the folders as shown in the folder structure.

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/healthcare-aiml-project.git
cd healthcare-aiml-project
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If missing, install manually:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3️⃣ Download Dataset + Models  
Download from Google Drive and place into:

```
data/
models/
```

### 4️⃣ Run the Notebook  
Open:
```
notebooks/healthcare_analysis.ipynb
```

Run all steps for:
- EDA  
- ML predictions  
- Anomaly detection  
- AI recommendation  

---

## 🤖 Prediction Script Usage

### Run:
```bash
python scripts/predict.py
```

Produces billing amount prediction based on sample or user-provided data.

---

## 🩺 AI Doctor Recommendation System

Run:
```bash
python scripts/ai_recommendation.py
```

### Example Output:
```
AI Doctor Recommendation
------------------------
Patient Age: 57
Medical Condition: Diabetes
Medication: Aspirin
Predicted Billing Amount: $29,403.14

Recommendation:
- Continue prescribed medication
- Monitor symptoms regularly
- Follow up in 2–4 weeks
- Seek urgent attention if symptoms worsen

Lifestyle:
- Balanced diet
- Increase physical activity
- Stay hydrated
```

---

## 📜 License
This project is released under the **MIT License**, allowing use and modification for any purpose.

---

## 🙌 Acknowledgements
- Dataset from Kaggle  
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn  

---

## ⭐ Support
If you found this project useful, please **star the repository** ⭐  
It helps support future enhancements!
