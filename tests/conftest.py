import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

activities_backup = copy.deepcopy(activities)

@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(activities_backup))
    yield

@pytest.fixture
def client():
    return TestClient(app)
