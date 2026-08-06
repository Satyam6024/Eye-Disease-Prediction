from EyeDiseaseClassifier import logger
from EyeDiseaseClassifier.pipeline.stage01_data_ingestion import DataIngestionPipeline
from EyeDiseaseClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from EyeDiseaseClassifier.pipeline.stage03_model_training import ModelTrainingPipeline
from EyeDiseaseClassifier.pipeline.stage04_model_evaluation import ModelEvaluationPipeline
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
    except RuntimeError as e:
        print(e)

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


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"\n{'='*20}")
    logger.info(f"{STAGE_NAME} started ")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed\n")
except Exception as e:
    logger.exception(e) 
    raise e