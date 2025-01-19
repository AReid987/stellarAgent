# Dependencies:
# uv add pytest-mock
# uv pip compile pyproject.toml
# uv pip install -r requirments.txt
import pytest


class TestPortkeyClient:

    # Fixture returns a valid PortkeyClient instance
    def test_portkey_client_fixture_returns_valid_instance(self, portkey_client):
        assert isinstance(portkey_client, PortkeyClient)
        assert hasattr(portkey_client, "portkey")
        assert portkey_client.portkey is not None

    # Missing environment variables for API key and config
    def test_portkey_client_missing_env_vars(self, mocker):
        mocker.patch.dict("os.environ", clear=True)
        with pytest.raises(TypeError):
            PortkeyClient()
