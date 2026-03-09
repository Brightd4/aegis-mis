import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def main():
    # Load dataset
    df = pd.read_csv("data/training_data.csv")

    X = df["text"]
    y = df["label"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
        ("clf", LogisticRegression())
    ])

    model.fit(X, y)

    joblib.dump(model, "models/misinformation_model.pkl")

    print("Model trained successfully.")


if __name__ == "__main__":
    main()