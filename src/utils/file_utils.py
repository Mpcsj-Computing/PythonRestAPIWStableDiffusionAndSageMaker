import tempfile
import os
from uuid import uuid4

TMP_FOLDER_NAME = "mpcsj_stable_diffusion_rest_api"


def create_if_not_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def get_tmp_folder_path():
    path = tempfile.gettempdir()
    path = os.path.join(path, TMP_FOLDER_NAME)
    create_if_not_exists(path)
    return path


def get_unique_tmp_file_path(file_format: str):
    file_path = os.path.join(get_tmp_folder_path(), f'{str(uuid4())}.{file_format}')
    return file_path
