import os  # noqa: F401, F811
import zipfile  # noqa: F401
import gdown  # noqa: F401
from cvclassifier import logger  # noqa: F401
from cvclassifier.utils.common import get_size  # noqa: F401
from cvclassifier.entity.config_entity import DataIngestionConfig






class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Fetch data from the URL and download it as a zip file.
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]  # Extract Google Drive file ID
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix + file_id, zip_download_dir, quiet=False, fuzzy=True)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
            return zip_download_dir

        except Exception as e:
            raise e

    def extract_zip_file(self):
        """
        Extracts the downloaded zip file into the specified directory.
        """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            if not os.path.exists(self.config.local_data_file):
                raise FileNotFoundError(f"Zip file not found at {self.config.local_data_file}")

            logger.info(f"Extracting {self.config.local_data_file} to {unzip_path}")
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extraction completed to {unzip_path}")

        except Exception as e:
            raise e





