# 🛡️ Intrusion Detection System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge)
![SHAP](https://img.shields.io/badge/SHAP-Explainable_AI-purple?style=for-the-badge)
![SMOTE](https://img.shields.io/badge/SMOTE-Imbalanced_Data-success?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge\&logo=streamlit)

---

# 🚀 Project Overview

An AI-powered Intrusion Detection System (IDS) designed to detect malicious network traffic using advanced Machine Learning techniques.

The project uses the **UNSW-NB15** cybersecurity dataset and incorporates modern preprocessing, feature engineering, explainable AI, and ensemble learning techniques to classify network attacks accurately.

The repository also contains a Streamlit web application for real-time intrusion prediction.

---

# 🌐 Live Demo

https://intrusion-detection-systems.streamlit.app

---

# 🎯 Objectives

* Detect malicious network traffic
* Classify multiple cyber attack categories
* Improve IDS performance using feature engineering
* Handle imbalanced datasets
* Explain model decisions using SHAP
* Deploy an interactive prediction dashboard

---

# 🏗️ Project Pipeline

```text
UNSW-NB15 Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Label Encoding
        │
        ▼
One-Hot Encoding
        │
        ▼
Feature Engineering
        │
        ▼
SMOTE Oversampling
        │
        ▼
SHAP Feature Selection
        │
        ▼
XGBoost Classifier
        │
        ▼
Model Evaluation
        │
        ▼
Streamlit Deployment
```

---

# 📊 Dataset

Dataset Used:

**UNSW-NB15 Dataset**

The dataset contains modern network traffic generated in realistic cyber attack scenarios.

### Attack Categories

* Analysis
* Backdoor
* DoS
* Exploits
* Fuzzers
* Generic
* Normal
* Reconnaissance
* Shellcode
* Worms

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* SHAP
* Imbalanced-Learn (SMOTE)
* Streamlit
* Plotly
* Jupyter Notebook

---

# 🧠 Machine Learning Pipeline

## Data Preprocessing

* Missing Value Handling
* Label Encoding
* One-Hot Encoding
* Feature Alignment

## Feature Engineering

* Derived Network Features
* Packet Ratio Features
* Byte Ratio Features
* Statistical Features

## Handling Imbalanced Data

* SMOTE Oversampling
* Class Distribution Balancing

## Explainable AI

* SHAP Feature Importance
* Top Feature Selection

## Model Training

* XGBoost Multi-Class Classifier
* Hyperparameter Tuning
* Model Evaluation

---

# 📈 Current Model Performance

| Metric   |      Value |
| -------- | ---------: |
| Accuracy | **76.18%** |
| Classes  |         10 |
| Dataset  |  UNSW-NB15 |

> **Note:** The project is under active development. Future versions will include advanced ensemble learning, Optuna optimization, and stacking models to improve performance.

---

# 🔥 Top Important Features

Examples of the most influential network features identified using SHAP:

* pkt_size_ratio
* sttl
* ct_dst_src_ltm
* sbytes
* smean
* ct_srv_dst
* byte_ratio
* service_dns
* proto_udp
* ct_srv_src
* ct_src_dport_ltm

---

# 🖥️ Streamlit Application

The application supports:

✅ Network traffic prediction

✅ Attack category classification

✅ Threat severity visualization

✅ Feature importance visualization

✅ Interactive prediction interface

---

# 📂 Project Structure

```text
Intrusion-Detection-System/
│
├── app.py
│
├── data/
│   └── UNSW-NB15/
│
├── models/
│   ├── xgboost_ids_v5.pkl
│   ├── feature_columns_xgb_v5.pkl
│   └── label_encoder_xgb_v5.pkl
│
├── notebooks/
│   ├── eda.ipynb
│   ├── ids_v2_unsw.ipynb
│   ├── ids_v3_xgboost_unsw.ipynb
│   ├── ids_v4_catboost_tuned.ipynb
│   ├── ids_v5_feature_selection.ipynb
│   ├── ids_v7_smote_xgboost.ipynb
│   ├── ids_v8_feature_engineering.ipynb
│   └── ids_v9_shap_optuna.ipynb
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/2303A52119/IntrusionDetection-System.git
```

Move into the project

```bash
cd IntrusionDetection-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🔮 Future Improvements

* Optuna Hyperparameter Optimization
* LightGBM Integration
* CatBoost + XGBoost Stacking
* Ensemble Learning
* Explainable AI Dashboard
* Real-Time Packet Monitoring
* Scapy Integration
* Docker Deployment
* AWS Deployment
* Bulk CSV Prediction API

---

# 👨‍💻 Author

**Rushik Pujari**

B.Tech Computer Science Engineering (2027)

### Interests

* Artificial Intelligence
* Machine Learning
* Explainable AI
* Cybersecurity
* Cloud Computing
* Data Science

---

⭐ If you found this project useful, consider giving it a star.
