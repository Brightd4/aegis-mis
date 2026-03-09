# AEGIS-MIS System Overview

## Introduction

AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System) is a prototype hybrid detection platform designed to identify potentially misleading or manipulative text content using both rule-based logic and machine learning classification.

The project explores how explainable AI techniques can support analysts in detecting high-risk misinformation patterns while maintaining transparency and interpretability.

---

## System Design Philosophy

AEGIS-MIS was designed around three key principles:

1. **Hybrid Detection**
   Combining deterministic rule-based detection with statistical machine learning classification.

2. **Explainability**
   Providing clear explanations of why content was flagged instead of producing opaque predictions.

3. **Accessibility**
   Allowing both human analysts and automated systems to interact with the platform through a web interface and REST API.

---

## Core Components

### Flask Web Interface

A lightweight web interface built using Flask allows users to submit text and receive an analysis report.

---

### Rule-Based Detection Engine

The rule-based engine searches for known misinformation patterns and trigger phrases such as:

- conspiracy framing
- “secret cure” claims
- authority distrust language
- suppression narratives

Each detected pattern contributes to a misinformation risk score.

---

### Machine Learning Detector

The ML detector uses a natural language processing pipeline based on:

- **TF-IDF feature extraction**
- **Logistic Regression classifier**

The classifier produces:

- predicted label
- confidence score

---

### Hybrid Scoring Engine

The hybrid scoring engine combines:

- rule-based triggers
- machine learning predictions

to produce a final **misinformation risk score**.

---

### Explainability Engine

The explainability component generates analyst-readable reports explaining:

- which triggers were detected
- how the risk score was calculated
- why the system flagged the text

---

### REST API

The system exposes a REST API endpoint:
