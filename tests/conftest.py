# Fixture api_client that provides a configured HTTP client

import pytest
import requests
import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

@pytest.fixture(scope="session")
def api_client():
    base_url = os.getenv("API_BASE_URL", "https://parabank.parasoft.com/parabank/services/bank")
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})

    #Attach the base URL to the session to avoid repeating it
    session.base_url = base_url

    yield session
    session.close()


@pytest.fixture
def load_json():
    def _load(schema_filename):
        BASE_DIR = Path(__file__).resolve().parent
        schema_path = BASE_DIR / schema_filename

        with open(schema_path) as schema_file:
            return json.load(schema_file)
    return _load