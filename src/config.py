from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"
REPORT_DIR = PROJECT_ROOT / "reports"
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"

# Reproducibility
RANDOM_STATE = 42