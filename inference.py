from pathlib import Path

import joblib

MODEL_PATH = Path("model.joblib")
IRIS_TARGET_NAMES = ["setosa", "versicolor", "virginica"]


def load_model(path: Path = MODEL_PATH):
    return joblib.load(path)


def predict(model, features: dict[str, float]) -> str:
    ordered_features = [
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"],
    ]
    prediction_idx = int(model.predict([ordered_features])[0])
    return IRIS_TARGET_NAMES[prediction_idx]
