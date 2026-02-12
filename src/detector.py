import re


class MisinformationDetector:
    def __init__(self):
        # Weighted trigger phrases (more realistic than +1 scoring)
        self.trigger_weights = {
            "hoax": 2,
            "fake": 1,
            "conspiracy": 2,
            "rigged": 1,
            "secret cure": 3,
            "they don't want you to know": 3
        }

    def analyze(self, text: str):
        score = 0
        found_triggers = []

        lower_text = text.lower()

        for phrase, weight in self.trigger_weights.items():
            if re.search(re.escape(phrase), lower_text):
                score += weight
                found_triggers.append(phrase)

        return {
            "misinformation_score": score,
            "triggers_found": found_triggers
        }
