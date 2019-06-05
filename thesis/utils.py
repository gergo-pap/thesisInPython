import os

from thesis import BASE_DIR


def get_path(*relative_path: str) -> str:
    return os.path.join(BASE_DIR, *relative_path)
