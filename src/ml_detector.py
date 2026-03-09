import joblib


class AIMisinformationDetector:
    def __init__(self):
        self.model = joblib.load("models/misinformation_model.pkl")

    def predict(self, text: str):
        prediction = self.model.predict([text])[0]
        probabilities = self.model.predict_proba([text])[0]

        misinformation_confidence = float(probabilities[1])

        if prediction == 1:
            return {
                "ai_flag": True,
                "ai_label": "Potential Misinformation",
                "ai_confidence": misinformation_confidence
            }
        else:
            return {
                "ai_flag": False,
                "ai_label": "Likely Reliable",
                "ai_confidence": misinformation_confidence
            }