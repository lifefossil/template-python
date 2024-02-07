import logging

from src.core.params import pyproject_toml_params, PYPROJECT_TOML_PATH
import tomllib


class TestGetPyprojectTomlConfig:
    """
    测试未在配置文件配置的参数使用默认值
    """
    def test_get_not_listed_params(self):
        pyproject_dict: dict | None
        unlisted: str = ""
        with open(PYPROJECT_TOML_PATH, 'rb') as fb:
            pyproject_dict = tomllib.load(fb)

        try:
            unlisted = pyproject_dict.get("project", {}).get("unlisted", "unlisted")
        except KeyError as e:
            logging.warning("解析 pyproject.toml 参数失败, 将使用默认值.", e)

        assert unlisted == "unlisted"


class TestPyprojectTomlParas:
    """
    测试 src.core.params:PyprojectTomlParams 获得配置文件参数
    """

    def test_pyproject_toml_paras(self):
        assert pyproject_toml_params.project_name == "template-python"