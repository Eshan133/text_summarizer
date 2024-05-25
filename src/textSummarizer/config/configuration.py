from textSummarizer.constant import *
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.utils.common import read_yaml, create_directories

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH, # from constant file
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath) # reads the yaml file 
        self.params = read_yaml(params_filepath)

        # creates the artifacts folder mentioned in config.yaml file
        create_directories([self.config.artifacts_root]) # Making use of ConfigBox insted of dict


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config