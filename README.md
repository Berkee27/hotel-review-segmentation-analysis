# Hotel Review Sentiment Analysis

This project classifies Turkish hotel reviews as positive or negative using basic NLP techniques.

## Purpose

The goal is to understand how text data can be cleaned, converted into numerical features, and used in a machine learning model.

## Technologies

- Python
- Pandas
- Scikit-learn
- NLTK
- Matplotlib
- Joblib

## Dataset Logic

The dataset contains hotel reviews.

Each row represents one hotel review.

Columns:

- `review`: The hotel review text
- `sentiment`: The target label, either `positive` or `negative`

## Machine Learning Approach

This is a supervised classification project.

Steps:

1. Create a small hotel review dataset
2. Clean text data
3. Tokenize Turkish text
4. Convert text into numerical vectors using TF-IDF
5. Train a Naive Bayes classifier
6. Evaluate the model with accuracy, precision, recall, F1-score, and confusion matrix
7. Save the trained model
8. Predict sentiment for new reviews

## How to Run

Create virtual environment:

```bash
python -m venv .venv
