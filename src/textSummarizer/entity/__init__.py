from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen= True)
class DataIngestionConfig:       #From config.yaml file -> data_ingestion:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

