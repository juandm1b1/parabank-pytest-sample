from playwright.sync_api import sync_playwright
import pytest
from screenpy import Actor
from screenpy_playwright import BrowseTheWebSynchronously


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