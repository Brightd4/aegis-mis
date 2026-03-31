# AEGIS-MIS

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

**AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System)** is a hybrid explainable misinformation detection system that combines rule-based analysis with machine learning techniques to provide accurate and interpretable classification of text content.

The system is designed to address the growing challenge of misinformation by balancing performance with transparency.

---
## 🔍 Overview

Misinformation spreads rapidly across digital platforms, making automated detection essential. However, many machine learning models operate as black boxes, limiting trust and interpretability.

AEGIS-MIS solves this by integrating:

- Rule-based analysis for interpretability  
- Machine learning (TF-IDF + Logistic Regression) for accuracy  
- Explainability mechanisms for transparency  

---
## ⚙️ Key Features

- Hybrid detection (rule-based + machine learning)  
- TF-IDF feature extraction  
- Logistic Regression classification  
- Explainable outputs for decision transparency  
- Lightweight and efficient architecture  
- Flask web interface and API support  

---

# 🌐 Live Demo

Access the deployed system here:

👉 https://aegis-mis.onrender.com

---

# Abstract

AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System) is a hybrid misinformation detection prototype designed to identify potentially deceptive or manipulative textual content.

The system combines rule-based pattern detection with a machine learning classifier based on TF-IDF feature extraction and logistic regression. These components are integrated through a hybrid scoring engine that produces a unified misinformation risk score.

To support transparency and interpretability, AEGIS-MIS includes an explainability module that highlights the triggers and model signals contributing to each decision. The system is deployed through a lightweight Flask web interface and REST API, enabling interactive analysis and integration with other security tools.

---
## 🧠 How It Works

The system processes input text through two main components:

---
### 1. Rule-Based Engine
Analyzes:
- suspicious keywords  
- misleading patterns  
- exaggerated or sensational language  

---
### 2. Machine Learning Model
- Converts text into TF-IDF features  
- Uses Logistic Regression for classification
  
---
### Final Decision
The outputs from both components are combined to produce:
- Final classification (Real / Misinformation)  
- Confidence score
- Explanation of contributing factors
---

---
## 🖥️ System Architecture

The system consists of:

- Data preprocessing module  
- Rule-based analysis engine  
- Feature extraction (TF-IDF)  
- Machine learning classifier  
- Explainability module  
- Flask web application

---  
# Web Interface

![Web Interface](screenshots/web_interface.png)

---
# 📊 Example Analysis Result 

Input:

![Analysis Result](screenshots/analysis_result.png)

---

# Project Structure

```text
AEGIS-MIS
├── data/
│   └── training_data.csv
├── models/
├── screenshots/
│   ├── web_interface.png
│   └── analysis_result.png
├── src/
│   ├── detector.py
│   ├── explainer.py
│   ├── ml_detector.py
│   └── main.py
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
