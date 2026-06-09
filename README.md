# 🛡️ Intrusion Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 🚀 Project Overview

This project implements a **Machine Learning-based Intrusion Detection System (IDS)** capable of identifying different categories of network attacks using the **KDD Cup 99 Dataset**.

The system analyzes network traffic features and classifies them into various attack categories using a **Random Forest Classifier**.

A user-friendly **Streamlit Web Application** has also been developed to perform real-time intrusion prediction.

---

## 🎯 Objectives

- Detect malicious network activities.
- Classify attacks into different categories.
- Improve cybersecurity monitoring using Machine Learning.
- Provide a simple web interface for predictions.

---

## 🏗️ Project Architecture

```text
KDD Dataset
     │
     ▼
Data Preprocessing
     │
     ▼
Feature Engineering
     │
     ▼
One-Hot Encoding
     │
     ▼
Random Forest Model
     │
     ▼
Model Evaluation
     │
     ▼
Streamlit Deployment
```

---

## 📊 Dataset

**Dataset Used:** KDD Cup 99 Dataset

The dataset contains various network traffic records and attack patterns.

### Attack Categories

| Class | Description |
|---------|------------|
| Normal | Legitimate network traffic |
| DoS | Denial of Service Attack |
| Probe | Surveillance and Scanning Attack |
| R2L | Remote to Local Attack |
| U2R | User to Root Attack |

---

## ⚙️ Technologies Used

- 🐍 Python
- 📊 Pandas
- 🔢 NumPy
- 🤖 Scikit-Learn
- 📈 Matplotlib
- 🔥 Streamlit
- 📝 Jupyter Notebook

---

## 🧠 Machine Learning Pipeline

### Data Preprocessing
- Missing value handling
- Data cleaning
- Label encoding
- Feature engineering

### Feature Transformation
- One-Hot Encoding
- Numerical feature processing

### Model Training
- Random Forest Classifier
- Train-Test Split
- Feature Importance Analysis

---

## 📈 Model Performance

### Accuracy

```text
75.86%
```

### Classification Report Summary

| Metric | Score |
|----------|---------|
| Accuracy | 75.86% |
| Weighted Precision | 0.81 |
| Weighted Recall | 0.76 |
| Weighted F1-Score | 0.71 |

---

## 🔥 Important Features Identified

The Random Forest model found these features highly influential:

- src_bytes
- same_srv_rate
- dst_bytes
- count
- diff_srv_rate
- flag_SF
- srv_rate
- difficulty

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit web interface where users can:

✅ Select Protocol Type

✅ Select Service Type

✅ Select Connection Flag

✅ Enter Network Parameters

✅ Predict Network Attack Category

---

## 📂 Project Structure

```text
Intrusion-Detection-System/
│
├── app/
│   └── app.py
│
├── data/
│   ├── KDDTrain+.txt
│   └── KDDTest+.txt
│
├── models/
│   ├── random_forest.pkl
│   ├── label_encoder.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/2303A52119/IntrusionDetection-System.git
```

### Move into Project

```bash
cd IntrusionDetection-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
cd app
streamlit run app.py
```

---

## 📸 Results

### Model Evaluation

✅ Accuracy Score

✅ Classification Report

✅ Confusion Matrix

✅ Feature Importance Analysis

### Web Interface

✅ Real-Time Prediction

✅ Interactive UI

✅ Attack Classification

---

## 🔮 Future Improvements

- Hyperparameter Optimization
- XGBoost Integration
- Deep Learning Based IDS
- Real-Time Packet Monitoring
- Cloud Deployment
- Advanced Threat Intelligence Integration

---

## 👨‍💻 Author

**Rushik Pujari**

Computer Science & Artificial Intelligence Student

Passionate about:
- Artificial Intelligence
- Machine Learning
- Cybersecurity
- Cloud Computing

---