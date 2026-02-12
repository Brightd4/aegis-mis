from detector import MisinformationDetector
from explainer import ExplainabilityEngine


def main():
    print("AEGIS-MIS system initialized.\n")

    sample_text = input("Enter text to analyze:\n> ")

    # 1️⃣ Run Detection
    detector = MisinformationDetector()
    result = detector.analyze(sample_text)

    # 2️⃣ Generate Explainable Report
    explainer = ExplainabilityEngine()
    report = explainer.generate_report(
        result["misinformation_score"],
        result["triggers_found"]
    )

    # 3️⃣ Output
    print("\n--- AEGIS-MIS REPORT ---\n")
    print(report)


if __name__ == "__main__":
    main()
