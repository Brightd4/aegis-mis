# AEGIS-MIS: A Hybrid Explainable Misinformation Detection System Using Rule-Based Analysis and Machine Learning

## Abstract

Misinformation presents growing risks to public trust, cybersecurity awareness, and digital information integrity. This paper presents AEGIS-MIS (Automated Explainable Guard for Information Security – Misinformation Identification System), a hybrid prototype for misinformation detection that combines deterministic rule-based analysis with machine learning-based text classification. The system integrates weighted trigger detection, a TF-IDF plus Logistic Regression classifier, a hybrid scoring engine, and an explainability module that generates analyst-readable reports. AEGIS-MIS is deployed through a Flask-based web interface and a REST API, enabling both interactive and programmatic use. Using a balanced synthetic dataset of 500 labeled examples, the baseline classifier achieved perfect performance on the current evaluation split, with accuracy, precision, recall, and F1-score all equal to 1.000. While these results demonstrate the feasibility of the proposed hybrid architecture, broader validation on more diverse real-world datasets is required. The project shows how explainable hybrid methods can support transparent misinformation detection workflows.

## Keywords

misinformation detection, explainable AI, natural language processing, machine learning, TF-IDF, logistic regression, hybrid detection, Flask API

## 1. Introduction

Digital misinformation has become a major challenge across public communication, online safety, political discourse, and health information environments. False or manipulative narratives can spread rapidly across digital platforms, often exploiting emotional language, distrust of institutions, and sensational framing. These dynamics create risks not only for public understanding but also for broader information security and social resilience.

Many automated misinformation detection approaches rely heavily on machine learning models that may provide strong classification performance but limited interpretability. In sensitive domains, systems that generate opaque predictions may be difficult to trust, audit, or operationalize. At the same time, purely rule-based systems can be transparent but brittle when language patterns vary.

This paper introduces AEGIS-MIS, a hybrid explainable misinformation detection prototype that combines rule-based detection with machine learning-based classification. The goal is to demonstrate a system architecture that is transparent, modular, and usable through both a web interface and an API. The project was designed as a prototype research platform to explore how hybrid scoring and explainability can support misinformation analysis.

The main contributions of this work are:

- a hybrid misinformation detection architecture combining rule-based and ML-based analysis,
- an explainability engine that produces analyst-readable reports,
- a Flask-based deployment with both web and REST API access,
- an initial experimental evaluation using a balanced labeled dataset.

## 2. Related Work

Misinformation detection has been studied using a wide range of natural language processing and machine learning approaches. Traditional text classification methods such as bag-of-words, TF-IDF feature extraction, Naive Bayes, Support Vector Machines, and Logistic Regression have long provided strong baselines for document and claim classification tasks. These methods remain attractive because they are lightweight, interpretable, and relatively easy to deploy.

More recent research has increasingly focused on deep learning and transformer-based architectures such as BERT, RoBERTa, and related pretrained language models. These systems often outperform classical models on complex benchmarks, but they can introduce challenges related to computational cost, explainability, and deployment complexity.

Parallel to model development, explainable AI has received increasing attention in high-stakes decision environments. In misinformation detection, explainability is especially important because analysts and users may need to understand why a specific text was flagged. Systems that combine explicit trigger patterns with probabilistic classifiers may offer a practical middle ground between transparency and adaptability.

The present work positions itself as a lightweight hybrid prototype rather than a large-scale benchmark model. Its emphasis is not only on classification but also on explainability, modularity, and accessible deployment.

## 3. Methodology

### 3.1 System Overview
![AEGIS-MIS System Architecture](exhibits/system_architecture.png)

Figure 1: Architecture of the AEGIS-MIS hybrid misinformation detection system. The system combines rule-based detection, machine learning classification, hybrid scoring, and explainability modules accessible through both a Flask web interface and a REST API.
AEGIS-MIS is composed of the following major components:

- Flask Web Interface
- Rule-Based Detector
- Machine Learning Detector
- Hybrid Scoring Engine
- Explainability Engine
- Logging System
- REST API Endpoint
- Offline Training Pipeline

The online inference pipeline begins when a user submits text through the web interface or the API. The input is processed in parallel by the rule-based detector and the machine learning detector. Their outputs are combined by the hybrid scoring engine, which produces a final misinformation risk score. The explainability engine then converts the result into a structured report for the user.

### 3.2 Rule-Based Detection

The rule-based module detects predefined trigger phrases and narrative patterns associated with misinformation. Each trigger is assigned a weight, allowing some phrases to contribute more strongly than others. This weighted design makes the score more realistic than a simple binary keyword count.

### 3.3 Machine Learning Detection

The machine learning component uses a standard natural language processing pipeline consisting of:

- TF-IDF vectorization
- Logistic Regression classification

This classifier predicts whether an input text is likely to represent normal information or potential misinformation. It also outputs a confidence score.

### 3.4 Hybrid Scoring

The hybrid scoring engine combines the rule-based score with the machine learning output. When the AI classifier flags a text as potential misinformation, an additional weight is added to the final score. This produces a unified risk value rather than two disconnected results.

### 3.5 Explainability

The explainability engine generates a readable report containing:

- risk level,
- misinformation score,
- detected patterns,
- explanatory text.

This design helps users understand which features influenced the decision and supports transparent analyst review.

## 4. Experimental Setup

### 4.1 Dataset

For the prototype evaluation, a balanced synthetic dataset of 500 labeled text samples was generated. The dataset included examples related to political conspiracy framing, alien/UFO narratives, anti-Muslim misinformation narratives, anti-LGBTQ misinformation narratives, and health misinformation patterns, alongside reliable informational examples across similar topics.
#### Dataset Statistics

The dataset used in this prototype experiment contains 500 labeled examples balanced between misinformation and reliable information.

| Class | Label | Number of Samples |
|------|------|------------------|
| Reliable Information | 0 | 250 |
| Misinformation | 1 | 250 |
| **Total** | — | **500** |

The dataset includes examples across multiple thematic categories to simulate diverse misinformation narratives, including:

- political conspiracy framing
- alien/UFO narratives
- health misinformation
- anti-Muslim conspiracy narratives
- anti-LGBTQ conspiracy narratives
- general misinformation patterns

Reliable examples were constructed to resemble fact-based informational statements across the same domains in order to provide balanced training data for the classifier.

The class distribution was:

- 250 misinformation samples
- 250 reliable information samples

### 4.2 Training Pipeline

The dataset was processed using a TF-IDF vectorizer and a Logistic Regression classifier implemented in scikit-learn. The dataset was split into training and testing subsets using a stratified train/test split to preserve class balance.

### 4.3 Evaluation Metrics

The following standard classification metrics were used:

- Accuracy
- Precision
- Recall
- F1-score

## 5. Results and Discussion

The baseline classifier achieved the following results on the current evaluation split:

- Accuracy: 1.000
- Precision: 1.000
- Recall: 1.000
- F1-score: 1.000

These results show that the classifier was able to perfectly separate the current synthetic test examples. This suggests that the hybrid prototype successfully captures the dominant patterns encoded in the current dataset.

However, these results should be interpreted with caution. Because the dataset is synthetic and template-based, the perfect performance likely reflects the structured regularity of the generated examples. Real-world misinformation is noisier, more ambiguous, and often stylistically diverse. Therefore, the present results should be understood as a feasibility demonstration rather than a final claim of real-world effectiveness.

From a systems perspective, the more important outcome is that AEGIS-MIS successfully integrates explainability, rule-based analysis, machine learning classification, web deployment, and API access into a unified architecture.

## 6. Limitations

This work has several limitations.

First, the dataset is synthetic and relatively small compared with real-world misinformation corpora. Second, the machine learning model is a lightweight baseline rather than a transformer-based architecture. Third, the rule-based detector depends on manually curated trigger patterns, which may not generalize to evolving narratives. Fourth, the current evaluation does not yet include adversarial or multilingual examples.

These limitations define a clear roadmap for future development.

## 7. Conclusion

This paper presented AEGIS-MIS, a hybrid explainable misinformation detection prototype that combines rule-based pattern analysis with machine learning classification. The system includes a weighted trigger detector, TF-IDF plus Logistic Regression classifier, hybrid scoring engine, explainability module, Flask web interface, REST API, and offline training pipeline.

Experimental results on a balanced synthetic dataset showed perfect baseline performance on the current split, demonstrating feasibility for the prototype architecture. At the same time, broader evaluation on larger and more diverse real-world datasets remains necessary. Future work will focus on richer datasets, transformer-based models, stronger explainability mechanisms, and more deployment-ready infrastructure.

## References

1. Shu, K., Sliva, A., Wang, S., Tang, J., & Liu, H. Fake news detection on social media: A data mining perspective.
2. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. BERT: Pre-training of deep bidirectional transformers for language understanding.
3. Pedregosa, F., et al. Scikit-learn: Machine learning in Python.
4. Ribeiro, M. T., Singh, S., & Guestrin, C. “Why Should I Trust You?” Explaining the predictions of any classifier.
5. Vaswani, A., et al. Attention is all you need.