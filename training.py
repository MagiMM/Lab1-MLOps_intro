from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = Path("model.joblib")


def load_data():
    iris = load_iris()
    return iris.data, iris.target, iris.target_names


def train_model():
    features, targets, _ = load_data()
    model = LogisticRegression(max_iter=500)
    model.fit(features, targets)
    return model


def save_model(model, path: Path = MODEL_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path
