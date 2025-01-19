import os
import sys
from unittest.mock import patch

from fastapi.testclient import TestClient

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
    assert "choices" in response.json()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to StellarAgent AI Gateway"}


client = TestClient(app)


@patch.dict(
    os.environ, {"PORTKEY_API_KEY": "test_key", "PORTKEY_CONFIG": "test_config"}
)
def test_create_completion_valid():
    response = client.post(
        "/v1/completions", json={"prompt": "Hello", "model": "gpt-3"}
    )
    assert response.status_code == 200
    assert "choices" in response.json()


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to StellarAgent AI Gateway"}
