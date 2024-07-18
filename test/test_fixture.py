# test_fixture.py

import pytest


@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}


def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
