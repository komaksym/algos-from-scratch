"""Starter exercise for training a classifier on imbalanced data."""

from pathlib import Path

import numpy as np
from imblearn.pipeline import make_pipeline
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import LinearSVC


class ClassifierWithImbalanceClass:
    def __init__(self) -> None:
        self._pipeline = make_pipeline(LinearSVC(random_state=42))
        self.scalar = StandardScaler()
        self.scalar = MinMaxScaler()

    def train(self, x, y):
        x = self.scalar.fit_transform(x)
        self._pipeline.fit(x, y)

    def predict(self, x):
        return self._pipeline.predict(x)


def find_latest_train_set() -> Path:
    downloads = Path.home() / "Downloads"
    candidates = [
        path / "train_data.csv"
        for path in downloads.iterdir()
        if path.is_dir() and (path / "train_data.csv").is_file()
    ]
    if not candidates:
        raise FileNotFoundError("No Downloads folder contains train_data.csv")
    return max(candidates, key=lambda path: path.parent.stat().st_mtime)


def main() -> None:
    train_set = find_latest_train_set()
    data = np.loadtxt(train_set, delimiter=",", skiprows=1)
    x = data[:, :-1]
    y = data[:, -1].astype(np.int64)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )
    classifier = ClassifierWithImbalanceClass()

    classifier.train(x_train, y_train)
    predictions = classifier.predict(x_test)
    score = roc_auc_score(y_test, predictions)
    print(f"Dataset: {train_set}")
    print(f"ROC AUC: {score:.3f}")

    assert 0.0 <= score <= 1.0


if __name__ == "__main__":
    main()
