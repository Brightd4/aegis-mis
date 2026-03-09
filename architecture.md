# AEGIS-MIS System Architecture

## Overview

AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System) is a hybrid AI-assisted misinformation detection platform designed to detect and analyze potentially misleading information in digital text.

The system combines rule-based pattern detection with machine learning-based classification and produces explainable reports for analysts.

---

## Architecture Components

### 1. User Interface Layer
The system provides a lightweight Flask-based web interface that allows users to submit text for analysis.

Functions:
- Accept user text input
- Display analysis results
- Show explanation and AI confidence scores

---

### 2. API Layer

The system exposes a REST API endpoint:

```
POST /api/analyze
```

This allows external tools or applications to send text to the system for automated analysis.

---

### 3. Rule-Based Detection Engine

The rule-based engine scans text for predefined misinformation trigger patterns such as:

- hoax
- conspiracy
- secret cure
- rigged
- “they don't want you to know”

Each trigger phrase has an associated weight that contributes to a misinformation score.

---

### 4. Machine Learning Classification Engine

The AI component uses a Natural Language Processing pipeline built with:

- TF-IDF Vectorization
- Logistic Regression classifier

The model predicts whether the input text is:

```
0 → Normal Information
1 → Potential Misinformation
```

The model outputs:

- predicted label
- confidence score

---

### 5. Hybrid Scoring Engine

The system combines outputs from both detection approaches.

Rule-based score + AI flag results in a final misinformation score.

If the AI classifier detects misinformation, an additional risk weight is added to the final score.

---

### 6. Explainability Engine

The explainability module generates a structured report including:

- risk level
- misinformation score
- detected trigger patterns
- explanation of the classification

This ensures the system produces transparent and interpretable results.

---

### 7. Logging System

Each analysis request is logged to:

```
analysis_log.txt
```

Logged data includes:

- timestamp
- input text
- misinformation score
- AI label
- AI confidence

This allows auditing and monitoring of system behavior.

---

### 8. Model Training Pipeline

The system includes a training script:

```
train_model.py
```

This pipeline:

1. Loads the training dataset
2. Performs TF-IDF feature extraction
3. Trains the logistic regression model
4. Evaluates the model using accuracy, precision, recall, and F1 score
5. Saves the trained model

The trained model is stored as:

```
models/misinformation_model.pkl
```

---

## System Flow

1. User submits text
2. Flask API receives the request
3. Rule-based detector scans trigger patterns
4. AI classifier predicts misinformation probability
5. Hybrid scoring engine combines results
6. Explainability module generates report
7. Results returned to user
8. Analysis logged for monitoring

---

## Key Design Goals

- Explainable AI outputs
- Hybrid detection architecture
- Lightweight deployment
- API accessibility
- Extensible research platform