class ExplainabilityEngine:
    def generate_report(self, score, triggers):
        # Risk classification
        if score == 0:
            risk = "LOW"
        elif score <= 2:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        # Dynamic explanation logic
        if triggers:
            trigger_list = ", ".join(triggers)
            explanation_text = f"The text contains high-risk phrases such as: {trigger_list}."
        else:
            explanation_text = "No known misinformation trigger phrases were detected."

        # Build report
        explanation = f"""
Risk Level: {risk}
Misinformation Score: {score}

Detected Patterns:
{', '.join(triggers) if triggers else 'None'}

Explanation:
{explanation_text}
Further verification is recommended.
"""

        return explanation.strip()
