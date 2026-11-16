import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import pytest
from screenpy import Actor
from screenpy_playwright import BrowseTheWebSynchronously


# Load variables from .env file
load_dotenv()

@pytest.fixture
def actor():
    #Fixture that brings the Screenplay Actor to life using Playwright.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context(record_video_dir="videos/")
        the_actor = Actor.named("Payer").who_can(BrowseTheWebSynchronously.using(None, context))
        yield the_actor
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def app_config():
    """Environment configuration for the application."""
    return {
        "url": os.getenv("PARABANK_URL", "https://parabank.parasoft.com"),
        "username": os.getenv("PARABANK_USER", "john"),
        "password": os.getenv("PARABANK_PASSWORD", "demo")
    }