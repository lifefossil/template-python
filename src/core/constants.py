from pathlib import Path

# 项目根目录路径
PROJECT_ROOT_PATH: Path = Path(__file__).parent.parent.parent

# pyproject.toml 默认路径
PYPROJECT_TOML_PATH: Path = PROJECT_ROOT_PATH.joinpath("pyproject.toml")

if __name__ == '__main__':
    print(PROJECT_ROOT_PATH)