"""
K3: Training untuk MLflow Project (dipanggil via `mlflow run` di GitHub Actions).
`mlflow run` sudah membuat run aktif, sehingga TIDAK memanggil start_run() sendiri.
"""
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.sklearn.autolog()

train = pd.read_csv("telco_preprocessing/telco_train.csv")
test = pd.read_csv("telco_preprocessing/telco_test.csv")

X_train = train.drop(columns=["Churn"]); y_train = train["Churn"]
X_test = test.drop(columns=["Churn"]);   y_test = test["Churn"]

model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
mlflow.log_metric("test_accuracy", acc)
print(f"Test accuracy: {acc:.4f}")
