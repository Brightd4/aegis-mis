# AEGIS-MIS

**AEGIS-MIS (Automated Explainable Guard for Information Security — Misinformation Identification System)** is a hybrid AI-assisted misinformation detection platform designed to support security analysis, information integrity, and public-interest defense.

## Features

- Rule-based misinformation trigger detection
- Machine learning NLP classifier
- Hybrid scoring logic
- Explainable analysis report
- Flask web interface
- REST API endpoint
- Analysis logging
- Model training pipeline

## Project Structure

```text
AEGIS-MIS
├── data/
│   └── training_data.csv
├── models/
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