import os
import sys
from unittest.mock import patch

from fastapi.testclient import TestClient
from src.portkey.portkey_client import PortkeyClient

# Add the parent directory to the sys path to import the main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import main

client = TestClient(main.app)


@patch.dict(
    os.environ, {"PORTKEY_API_KEY": "test_key", "PORTKEY_CONFIG": "test_config"}
)
def test_create_completion_valid():
    response = client.post(
        "/v1/completions", json={"prompt": "Hello", "model": "gpt-3"}
    )
    assert response.status_code == 200

    response_json = response.json()
    # Verify response structure
    assert "choices" in response_json
    assert "id" in response_json
    assert "created" in response_json
    assert "model" in response_json

    # Verify choices array
    choices = response_json["choices"]
    assert isinstance(choices, list)
    assert len(choices) > 0

    # Verify first choice structure
    first_choice = choices[0]
    assert "text" in first_choice
    assert "index" in first_choice
    assert "finish_reason" in first_choice

    # Verify data types
    assert isinstance(first_choice["text"], str)
    assert isinstance(first_choice["index"], int)
    assert isinstance(response_json["created"], int)
    assert response_json["model"] == "gpt-3"


# Removed redundant test


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to StellarAgent AI Gateway"}
import pytest

@pytest.fixture
def portkey_client():
    return PortkeyClient()
