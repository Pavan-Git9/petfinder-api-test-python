import pytest
from utils.auth import get_access_token

@pytest.fixture(scope="session")
def access_token():
    return get_access_token()

@pytest.fixture(scope="session")
def headers(access_token):
    return {
        "Authorization": f"Bearer {access_token}"
    }
