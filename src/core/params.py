import tomllib
from pathlib import Path

from src.core.constants import PYPROJECT_TOML_PATH

class PyprojectTomlParams:
    def __init__(self, pyproject_toml_path: str | Path = PYPROJECT_TOML_PATH):
        self.pyproject_toml_path: str | Path = pyproject_toml_path
        self.project_name: str = ""
        self.description: str = ""
        self.version: str = ""
        self.pyproject_toml_dict: dict | None = None
        self.init()

    def init(self):
        with open(self.pyproject_toml_path, 'rb') as fb:
            self.pyproject_toml_dict = tomllib.load(fb)
            try:
                self.project_name = self.pyproject_toml_dict["tool"]["poetry"]["name"]
                self.description = self.pyproject_toml_dict["tool"]["poetry"]["description"]
                self.version = self.pyproject_toml_dict["tool"]["poetry"]["version"]
            except KeyError:
                pass


pyproject_toml_params: PyprojectTomlParams = PyprojectTomlParams()

if __name__ == '__main__':
    print(pyproject_toml_params.project_name)
    print(pyproject_toml_params.description)
    print(pyproject_toml_params.version)

