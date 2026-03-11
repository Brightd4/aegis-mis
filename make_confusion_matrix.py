import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load dataset
df = pd.read_csv("data/training_data.csv")

X = df["text"]
y = df["label"]

# Same split logic as training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Load trained model
model = joblib.load("models/misinformation_model.pkl")

# Predict on test set
y_pred = model.predict(X_test)

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Reliable", "Misinformation"]
)

fig, ax = plt.subplots(figsize=(6, 5))
disp.plot(ax=ax, values_format="d")

plt.title("AEGIS-MIS Confusion Matrix")
plt.tight_layout()

# Save figure
plt.savefig("exhibits/confusion_matrix.png", dpi=300)
plt.show()

print("Saved confusion matrix to exhibits/confusion_matrix.png")