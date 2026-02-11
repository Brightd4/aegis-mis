from detector import MisinformationDetector

def main():
    print("AEGIS-MIS system initialized.\n")

    sample_text = input("Enter text to analyze:\n> ")

    detector = MisinformationDetector()
    result = detector.analyze(sample_text)

    print("\n--- Analysis Result ---")
    print(f"Misinformation Score: {result['misinformation_score']}")
    print(f"Triggers Found: {result['triggers_found']}")

if __name__ == "__main__":
    main()
