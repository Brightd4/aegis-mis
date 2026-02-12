class ExplainabilityEngine:
    def generate_report(self, score, triggers):
        if score == 0:
            risk = "LOW"
        elif score <= 2:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        explanation = f"""
Risk Level: {risk}
Misinformation Score: {score}

Detected Patterns:
{', '.join(triggers) if triggers else 'None'}

Explanation:
The text contains language commonly associated with misinformation narratives.
Further verification is recommended.
"""

        return explanation.strip()
