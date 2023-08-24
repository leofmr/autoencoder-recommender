"""_download data module
"""

import tempfile
import zipfile

import requests
from tqdm import tqdm

URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
DOWNLOAD_PATH = "../downloads/"


def downlad_external_file(url: str, path: str):
    """Download external file from url into designed path

    Args:
        url (str): origin file url
        path (str): destiny path
    """
    response = requests.get(url, timeout=10, stream=True)
    with open(path, "wb") as file:
        for data in tqdm(response.iter_content()):
            file.write(data)


def unzip_file(zip_file_path: str, path: str):
    """Unzip file to designed path

    Args:
        zip_file (str): zip file path
        path (str): destiny path
    """
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall(path)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as temp_dir:
        file_name = URL.split("/", maxsplit=-1)[-1]
        file_path = f"{temp_dir}/{file_name}"

        downlad_external_file(url=URL, path=file_path)
        unzip_file(zip_file_path=file_path, path=DOWNLOAD_PATH)
