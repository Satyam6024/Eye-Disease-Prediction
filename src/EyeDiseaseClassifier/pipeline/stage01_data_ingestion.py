from EyeDiseaseClassifier.config.configuration import ConfigurationManager
from EyeDiseaseClassifier.components.data_ingestion import DataIngestion
from EyeDiseaseClassifier import logger

STAGE_NAME = "Data Ingestion"



class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"\n{'='*20}")
        logger.info(f"{STAGE_NAME} started ")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed\n")
    except Exception as e:
        logger.exception(e)