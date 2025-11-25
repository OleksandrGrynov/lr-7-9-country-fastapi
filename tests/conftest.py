import os

import pytest
from fastapi.testclient import TestClient

from src.main import app


os.environ["TESTING"] = "1"


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(app)
