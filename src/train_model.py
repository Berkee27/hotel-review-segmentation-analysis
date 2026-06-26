from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from text_utils import clean_text, turkish_tokenizer


RANDOM_SEED = 42

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "hotel_reviews.csv"
MODEL_PATH = BASE_DIR / "models" / "sentiment_model.joblib"
REPORT_PATH = BASE_DIR / "reports" / "confusion_matrix.png"

LABEL_ORDER = ["negative", "positive"]


def load_dataset():
    df = pd.read_csv(DATA_PATH)

    X = df["review"]
    y = df["sentiment"]

    return X, y


def build_model():
    model = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    preprocessor=clean_text,
                    tokenizer=turkish_tokenizer,
                    token_pattern=None,
                    ngram_range=(1, 2),
                    min_df=1
                )
            ),
            (
                "naive_bayes",
                MultinomialNB(alpha=0.7)
            )
        ]
    )

    return model


def save_confusion_matrix(y_test, y_pred):
    matrix = confusion_matrix(y_test, y_pred, labels=LABEL_ORDER)

    display = ConfusionMatrixDisplay(
        confusion_matrix=matrix,
        display_labels=LABEL_ORDER
    )

    display.plot(values_format="d")
    plt.title("Hotel Review Sentiment Confusion Matrix")
    plt.tight_layout()
    plt.savefig(REPORT_PATH)
    plt.close()


def main():
    X, y = load_dataset()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=RANDOM_SEED,
        stratify=y
    )

    model = build_model()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print("Model training completed.")
    print(f"Train row count: {len(X_train)}")
    print(f"Test row count: {len(X_test)}")
    print(f"Accuracy: {accuracy:.2f}")
    print()
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, MODEL_PATH)
    save_confusion_matrix(y_test, y_pred)

    print(f"Model saved to: {MODEL_PATH}")
    print(f"Confusion matrix saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()