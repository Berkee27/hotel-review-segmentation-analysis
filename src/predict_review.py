from pathlib import Path
import sys

import joblib


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "sentiment_model.joblib"


def predict_sentiment(review_text):
    model = joblib.load(MODEL_PATH)

    prediction = model.predict([review_text])[0]
    probability = model.predict_proba([review_text])[0]

    class_names = model.classes_
    probability_dict = dict(zip(class_names, probability))

    return prediction, probability_dict


def main():
    if len(sys.argv) > 1:
        review_text = " ".join(sys.argv[1:])
    else:
        review_text = "Oda temizdi, personel ilgiliydi, genel olarak memnun kaldım."

    prediction, probability_dict = predict_sentiment(review_text)

    print("Review:")
    print(review_text)
    print()
    print(f"Predicted sentiment: {prediction}")
    print("Probabilities:")

    for class_name, probability in probability_dict.items():
        print(f"- {class_name}: {probability:.2f}")


if __name__ == "__main__":
    main()