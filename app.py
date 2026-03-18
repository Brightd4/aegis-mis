from flask import Flask, request, render_template_string, jsonify
from src.detector import MisinformationDetector
from src.explainer import ExplainabilityEngine
from src.ml_detector import AIMisinformationDetector
from datetime import datetime
import os

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
            margin: 0;
            background: #f4f7fb;
            color: #1f2937;
        }

        .container {
            max-width: 950px;
            margin: 40px auto;
            background: white;
            padding: 32px;
            border-radius: 14px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        }

        h1 {
            margin-top: 0;
            color: #0f172a;
        }

        .subtitle {
            color: #475569;
            margin-bottom: 24px;
        }

        textarea {
            width: 100%;
            height: 140px;
            padding: 14px;
            border: 1px solid #cbd5e1;
            border-radius: 10px;
            font-size: 15px;
            resize: vertical;
            box-sizing: border-box;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 22px;
            margin-top: 14px;
            border-radius: 10px;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .result {
            margin-top: 30px;
            background: #f8fafc;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
        }

        .badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            font-weight: bold;
            margin-bottom: 18px;
        }

        .high {
            background: #fee2e2;
            color: #b91c1c;
        }

        .medium {
            background: #fef3c7;
            color: #b45309;
        }

        .low {
            background: #dcfce7;
            color: #15803d;
        }

        .card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 16px;
            margin-top: 14px;
        }

        .label {
            font-weight: bold;
            color: #0f172a;
        }

        .mono {
            white-space: pre-wrap;
            font-family: Consolas, monospace;
            line-height: 1.6;
        }

        .footer {
            margin-top: 28px;
            font-size: 13px;
            color: #64748b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AEGIS-MIS</h1>
        <p class="subtitle">
            Automated Explainable Guard for Information Security – Misinformation Identification System
        </p>

        <form method="POST">
            <textarea name="text" placeholder="Paste text to analyze..."></textarea>
            <br>
            <button type="submit">Analyze Text</button>
        </form>

        {% if report %}
        <div class="result">
            <div class="badge {{ risk_class }}">{{ risk_level }} Risk</div>

            <div class="card">
                <div class="label">Analysis Report</div>
                <div class="mono">{{ report }}</div>
            </div>

            {% if ai_label %}
            <div class="card">
                <div><span class="label">AI Model Label:</span> {{ ai_label }}</div>
                <div style="margin-top:8px;"><span class="label">AI Confidence:</span> {{ ai_confidence }}</div>
            </div>
            {% endif %}
        </div>
        {% endif %}

        <div class="footer">
            AEGIS-MIS prototype — hybrid rule-based and machine learning misinformation analysis.
        </div>
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    ai_label = None
    ai_confidence = None
    risk_level = None
    risk_class = None

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

        if result["misinformation_score"] >= 5:
            risk_level = "High"
            risk_class = "high"
        elif result["misinformation_score"] >= 3:
            risk_level = "Medium"
            risk_class = "medium"
        else:
            risk_level = "Low"
            risk_class = "low"

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
        ai_confidence=ai_confidence,
        risk_level=risk_level,
        risk_class=risk_class
    )


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    user_text = data["text"].strip()

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)