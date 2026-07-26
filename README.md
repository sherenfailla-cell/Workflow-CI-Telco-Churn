# Telco Churn — CI Retraining Pipeline (MLflow Project + GitHub Actions)

Automated model retraining: every push (or manual trigger) re-trains a RandomForest churn model
via `mlflow run` inside GitHub Actions, with parameters, metrics, and model artifacts logged by MLflow autolog.
Each successful workflow stores the MLflow tracking directory as a downloadable GitHub Actions artifact.

- `MLProject/` — MLflow Project spec (`MLProject`, `conda.yaml`) + training script + preprocessed data
- `.github/workflows/ci.yml` — CI pipeline: checkout → Python 3.12.7 → dependencies → MLflow retraining → artifact upload

**Related repo:** experiment & preprocessing → `Eksperimen_SML_Sheren-Failla`
