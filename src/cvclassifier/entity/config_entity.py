from dataclasses import dataclass
from pathlib import Path  # noqa: F401
from dataclasses import dataclass  # noqa: F811

@dataclass
class DataIngestionConfig:
    root_dir: str
    source_URL: str
    local_data_file: str
    unzip_dir: str
