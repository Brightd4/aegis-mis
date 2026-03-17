# AEGIS-MIS

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Logistic%20Regression-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Prototype-yellow)

**AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System)** is a hybrid AI-assisted misinformation detection platform designed to support information integrity, cybersecurity awareness, and public-interest defense.

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

# Features

- Rule-based misinformation trigger detection
- Machine learning NLP classifier
- Hybrid scoring logic
- Explainable analysis report
- Flask web interface
- REST API endpoint
- Analysis logging
- Model training pipeline

---

# Web Interface

![Web Interface](screenshots/web_interface.png)

---

# Example Analysis Result

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