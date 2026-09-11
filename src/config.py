
import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID")

BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")

DATASET_BRONZE = "uber_bronze"

DATASET_SILVER = "uber_silver"

DATASET_GOLD = "uber_gold"

RAW_TABLE = "uber_raw"

CLEAN_TABLE = "uber_clean"
