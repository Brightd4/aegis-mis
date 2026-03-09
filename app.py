from flask import Flask, request, render_template_string, jsonify
from src.detector import MisinformationDetector
from src.explainer import ExplainabilityEngine
from src.ml_detector import AIMisinformationDetector
from datetime import datetime

app = Flask(__name__)

detector = MisinformationDetector()
explainer = ExplainabilityEngine()
ai_detector = AIMisinformationDetector()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AEGIS-MIS</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f4f4f4;
        }

        textarea {
            width: 100%;
            height: 120px;
        }

        button {
            padding: 10px 20px;
            margin-top: 10px;
        }

        .result {
            margin-top: 20px;
            background: white;
            padding: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

    <h2>AEGIS-MIS — Misinformation Detection System</h2>

    <form method="POST">
        <textarea name="text" placeholder="Paste text to analyze..."></textarea>
        <br>
        <button type="submit">Analyze</button>
    </form>

    {% if report %}
    <div class="result">
        <h3>Analysis Result</h3>
        <pre>{{ report }}</pre>

        {% if ai_label %}
        <p><strong>AI Model Label:</strong> {{ ai_label }}</p>
        <p><strong>AI Confidence:</strong> {{ ai_confidence }}</p>
        {% endif %}
    </div>
    {% endif %}

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    ai_label = None
    ai_confidence = None

    if request.method == "POST":
        user_text = request.form["text"].strip()

        result = detector.analyze(user_text)
        ai_result = ai_detector.predict(user_text)

        ai_label = ai_result["ai_label"]
        ai_confidence = round(ai_result["ai_confidence"], 3)

        if ai_result["ai_flag"]:
            result["misinformation_score"] += 2
            result["triggers_found"].append("AI_MODEL_FLAG")

        report = explainer.generate_report(
            result["misinformation_score"],
            result["triggers_found"]
        )

        with open("analysis_log.txt", "a", encoding="utf-8") as log:
            log.write(
                f"{datetime.now()} | "
                f"Score:{result['misinformation_score']} | "
                f"AI_Label:{ai_label} | "
                f"AI_Confidence:{ai_confidence} | "
                f"Text:{user_text}\n"
            )

    return render_template_string(
        HTML_TEMPLATE,
        report=report,
        ai_label=ai_label,
        ai_confidence=ai_confidence
    )

@app.route("/api/analyze", methods=["POST"])
def api_analyze():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    user_text = data["text"]

    result = detector.analyze(user_text)
    ai_result = ai_detector.predict(user_text)

    if ai_result["ai_flag"]:
        result["misinformation_score"] += 2
        result["triggers_found"].append("AI_MODEL_FLAG")

    return jsonify({
        "text": user_text,
        "misinformation_score": result["misinformation_score"],
        "triggers_found": result["triggers_found"],
        "ai_label": ai_result["ai_label"],
        "ai_confidence": round(ai_result["ai_confidence"], 3)
    })
if __name__ == "__main__":
    app.run(debug=True)