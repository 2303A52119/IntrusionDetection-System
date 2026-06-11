# 🛡️ Intrusion Detection System using XGBoost

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

# 🚀 Project Overview

This project implements a Machine Learning-based Intrusion Detection System (IDS) capable of detecting malicious network activity using the NSL-KDD dataset.

The system uses an XGBoost Classifier to classify network traffic into five categories:

* Normal
* DoS
* Probe
* R2L
* U2R

An interactive Streamlit dashboard allows users to perform real-time intrusion prediction and view threat severity levels.

---

# 🎯 Objectives

* Detect malicious network traffic
* Classify attack categories
* Assist cybersecurity monitoring
* Provide real-time predictions
* Visualize prediction confidence

---

# 🏗️ Project Architecture

```text
NSL-KDD Dataset
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
XGBoost Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Streamlit Dashboard
```

---

# 📊 Dataset

Dataset Used: NSL-KDD Dataset

The NSL-KDD dataset is an improved version of the KDD Cup 99 dataset and is widely used for network intrusion detection research.

## Attack Categories

| Class  | Description                      |
| ------ | -------------------------------- |
| Normal | Legitimate network traffic       |
| DoS    | Denial of Service Attack         |
| Probe  | Surveillance and Scanning Attack |
| R2L    | Remote to Local Attack           |
| U2R    | User to Root Attack              |

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* XGBoost
* Scikit-Learn
* Streamlit
* Joblib
* Jupyter Notebook

---

# 🧠 Machine Learning Pipeline

## Data Preprocessing

* Data Cleaning
* Label Encoding
* Feature Engineering
* One-Hot Encoding

## Model Training

* XGBoost Classifier
* Train-Test Split
* Feature Importance Analysis
* Multi-Class Classification

---

# 📈 Model Performance

## Accuracy

77.76%

## Classification Metrics

| Metric             | Score  |
| ------------------ | ------ |
| Accuracy           | 77.76% |
| Weighted Precision | 0.83   |
| Weighted Recall    | 0.78   |
| Weighted F1 Score  | 0.74   |

---

# 🔥 Important Features

Top features identified by XGBoost:

* same_srv_rate
* is_guest_login
* service_ecr_i
* src_bytes
* service_http
* root_shell
* diff_srv_rate
* num_failed_logins
* num_compromised
* service_eco_i

---

# 🖥️ Streamlit Dashboard Features

The application provides:

✅ Attack Prediction

✅ Confidence Score

✅ Threat Severity Assessment

✅ Prediction History

✅ Real-Time Inference

✅ Interactive User Interface

---

# 📂 Project Structure

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
│   ├── xgboost_ids.pkl
│   ├── label_encoder_xgb.pkl
│   └── feature_columns_xgb.pkl
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

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/2303A52119/IntrusionDetection-System.git
```

Move into project:

```bash
cd IntrusionDetection-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
cd app
streamlit run app.py
```

---

# 📸 Results

Model Evaluation:

* Accuracy Score
* Classification Report
* Confusion Matrix
* Feature Importance Analysis

Dashboard Features:

* Real-Time Prediction
* Threat Severity
* Confidence Score
* Prediction History

---

# 🔮 Future Improvements

* Hyperparameter Optimization
* Deep Learning-Based IDS
* Real-Time Packet Monitoring
* Streamlit Cloud Deployment
* Network Traffic Visualization
* Threat Intelligence Integration

---

# 👨‍💻 Author

Rushik Pujari

Computer Science & Artificial Intelligence Student

Interests:

* Artificial Intelligence
* Machine Learning
* Cybersecurity
* Cloud Computing
* Data Science
