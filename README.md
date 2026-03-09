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

## Current Evaluation

Using the current prototype dataset and a stratified train/test split, the baseline Logistic Regression + TF-IDF classifier achieved:

- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- F1 Score: 1.000

### Important Note
These results were obtained on a small synthetic prototype dataset and should be interpreted as an early validation signal rather than final real-world performance. Broader evaluation on larger and more diverse datasets is planned.

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

---

## Documentation

Additional project documentation:

- **Project Summary:** [project_summary.md](project_summary.md)
- **System Architecture:** [architecture.md](architecture.md)
- **Evaluation Results:** [evaluation_results.md](evaluation_results.md)

These documents describe the system design, experimental results, and overall project objectives for AEGIS-MIS.