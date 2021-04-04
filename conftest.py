import pytest
from src.main.api import ApiClient
from src.configs.config_manager import Config


@pytest.fixture(scope="class")
def api():
    config = Config("config.json")
    yield ApiClient(config)
