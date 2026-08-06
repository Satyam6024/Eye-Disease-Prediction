from EyeDiseaseClassifier import logger
from EyeDiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from EyeDiseaseClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from EyeDiseaseClassifier.pipeline.stage03_model_training import ModelTrainingPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"\n{'='*20}")
    logger.info(f"{STAGE_NAME} started ")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed\n")
except Exception as e:
    logger.exception(e) 
    raise e

STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"\n{'='*20}")
    logger.info(f"{STAGE_NAME} started ")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed\n")
except Exception as e:
    logger.exception(e) 
    raise e

STAGE_NAME = "Model Training"
try:
    logger.info(f"\n{'='*20}")
    logger.info(f"{STAGE_NAME} started ")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed\n")
except Exception as e:
    logger.exception(e) 
    raise e

