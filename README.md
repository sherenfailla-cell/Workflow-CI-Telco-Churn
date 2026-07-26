# Telco Churn — CI Retraining Pipeline (MLflow Project + GitHub Actions)

Automated model retraining: every push (or manual trigger) re-trains a RandomForest churn model
via `mlflow run` inside GitHub Actions, with parameters, metrics, and model artifacts logged by MLflow autolog.

- `MLProject/` — MLflow Project spec (`MLProject`, `conda.yaml`) + training script + preprocessed data
- `.github/workflows/ci.yml` — CI pipeline: checkout → Python 3.12.7 → deps → `mlflow run . --env-manager=local`

**Related repo:** experiment & preprocessing → `Eksperimen_SML_Telco-Churn`
