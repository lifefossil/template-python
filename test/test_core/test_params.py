from src.core.params import pyproject_toml_params


def test_pyproject_toml_paras():
    assert pyproject_toml_params.project_name == "template-python"
