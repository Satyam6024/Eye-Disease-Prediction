from EyeDiseaseClassifier import logger
from EyeDiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"\n{'='*20}")
        logger.info(f"{STAGE_NAME} started ")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed\n")
    except Exception as e:
        logger.exception(e) 