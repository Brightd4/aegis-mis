# AEGIS-MIS

**AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System)** is a hybrid AI-assisted misinformation detection platform designed to support information integrity, cybersecurity awareness, and public-interest defense.

## Abstract

AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System) is a hybrid misinformation detection prototype designed to identify potentially deceptive or manipulative textual content.

The system combines rule-based pattern detection with a machine learning classifier based on TF-IDF feature extraction and logistic regression. These components are integrated through a hybrid scoring engine that produces a unified misinformation risk score.

To support transparency and interpretability, AEGIS-MIS includes an explainability module that highlights the triggers and model signals contributing to each decision. The system is deployed through a lightweight Flask web interface and REST API, enabling interactive analysis and integration with other security tools.

## Features

- Rule-based misinformation trigger detection
- Machine learning NLP classifier
- Hybrid scoring logic
- Explainable analysis report
- Flask web interface
- REST API endpoint
- Analysis logging
- Model training pipeline

## Web Interface

![Web Interface](screenshots/web_interface.png)

## Example Analysis Result

![Analysis Result](screenshots/analysis_result.png)

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
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Train the Model

```bash
python train_model.py
```

## Run the Web App

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## API Usage

Endpoint:

```text
POST /api/analyze
```

Example PowerShell request:

```powershell
Invoke-RestMethod `
-Uri "http://127.0.0.1:5000/api/analyze" `
-Method Post `
-ContentType "application/json" `
-Body '{"text":"This is a secret cure they do not want you to know."}'
```

## Current Evaluation

Using the current prototype dataset and a stratified train/test split, the baseline Logistic Regression + TF-IDF classifier achieved:

- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- F1 Score: 1.000

### Important Note

These results were obtained on a small synthetic prototype dataset and should be interpreted as an early validation signal rather than final real-world performance. Broader evaluation on larger and more diverse datasets is planned.

## Documentation

Additional project documentation:

- **Project Summary:** [project_summary.md](project_summary.md)
- **System Architecture:** [architecture.md](architecture.md)
- **Evaluation Results:** [evaluation_results.md](evaluation_results.md)

These documents describe the system design, experimental results, and overall project objectives for AEGIS-MIS.

## Purpose

AEGIS-MIS is a hybrid misinformation detection and security defense prototype that combines transparent rule-based logic with machine learning-assisted text classification.

## Future Work

The current prototype demonstrates the feasibility of hybrid rule-based and machine learning approaches for misinformation detection. Future improvements may include:

- Expanding the training dataset with real-world misinformation corpora
- Integrating transformer-based NLP models such as BERT or RoBERTa
- Implementing automated feature importance explanations
- Adding credibility scoring for external sources
- Building a browser extension for real-time misinformation detection
- Deploying the system as a scalable cloud service
- Enhancing multilingual misinformation detection capabilities

## Status

Prototype under active development.