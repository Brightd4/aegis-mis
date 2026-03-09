from detector import MisinformationDetector
from explainer import ExplainabilityEngine
from datetime import datetime


def main():
    print("AEGIS-MIS system initialized.\n")

    # 1) Get user input
    sample_text = input("Enter text to analyze:\n> ").strip()

    if not sample_text:
        print("\nNo text entered. Exiting.")
        return

    # 2) Detect misinformation patterns
    detector = MisinformationDetector()
    result = detector.analyze(sample_text)

    score = result["misinformation_score"]
    triggers = result["triggers_found"]

    # Risk classification (needed for logging)
    if score == 0:
        risk = "LOW"
    elif score <= 2:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    # 3) Generate explainable report
    explainer = ExplainabilityEngine()
    report = explainer.generate_report(score, triggers)

    # 4) Log analysis event
    with open("analysis_log.txt", "a", encoding="utf-8") as log:
        log.write(
            f"{datetime.utcnow().isoformat()} | "
            f"Risk: {risk} | "
            f"Score: {score} | "
            f"Triggers: {triggers} | "
            f"Text: {sample_text}\n"
        )

    # 5) Print results
    print("\n--- AEGIS-MIS REPORT ---\n")
    print(report)


if __name__ == "__main__":
    main()
