import re

class MisinformationDetector:
    def __init__(self):
        self.trigger_words = [
            "hoax",
            "fake",
            "conspiracy",
            "rigged",
            "secret cure",
            "they don't want you to know"
        ]

    def analyze(self, text):
        score = 0
        found_triggers = []

        for word in self.trigger_words:
            if re.search(word, text.lower()):
                score += 1
                found_triggers.append(word)

        return {
            "misinformation_score": score,
            "triggers_found": found_triggers
        }
