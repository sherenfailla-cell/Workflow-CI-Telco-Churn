# Telco Churn — CI Retraining Pipeline (MLflow Project + GitHub Actions)

Automated model retraining: every push (or manual trigger) re-trains a RandomForest churn model
via `mlflow run` inside GitHub Actions, with parameters, metrics, and model artifacts logged by MLflow autolog.
Each successful workflow stores the MLflow tracking directory as a downloadable GitHub Actions artifact.
When the two Docker Hub repository secrets are configured, the same workflow builds the serving image
with `mlflow models build-docker` and pushes immutable commit and `latest` tags to Docker Hub.

- `MLProject/` — MLflow Project spec (`MLProject`, `conda.yaml`) + training script + preprocessed data
- `.github/workflows/ci.yml` — CI pipeline: checkout → Python 3.12.7 → dependencies → retraining → artifact upload → MLflow Docker build → Docker Hub push
- `MLProject/DockerHub.txt` — public image link and reproducible pull commands

Public image: [`iqbalrahardjo/telco-churn-mlflow`](https://hub.docker.com/r/iqbalrahardjo/telco-churn-mlflow)

Required GitHub Actions repository secrets for the Advanced pipeline:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

**Related repo:** experiment & preprocessing → `Eksperimen_SML_Sheren-Failla`
