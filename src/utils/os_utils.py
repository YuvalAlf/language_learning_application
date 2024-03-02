import tempfile
from dataclasses import dataclass
from tempfile import TemporaryDirectory
from typing import ClassVar


class GlobalTemporaryDirectory:
    _instance = None
    _temp_dir = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._temp_dir = tempfile.TemporaryDirectory()
        return cls._instance

    @staticmethod
    def get_temporary_directory() -> str:
        if GlobalTemporaryDirectory._temp_dir:
            return GlobalTemporaryDirectory._temp_dir.name
        else:
            return GlobalTemporaryDirectory()._temp_dir.name
