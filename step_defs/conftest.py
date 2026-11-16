import os
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import pytest
import allure
from screenpy import Actor
from screenpy_playwright import BrowseTheWebSynchronously


# Load variables from .env file
load_dotenv()

# 1. Hook to store the test result so fixtures can read it
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # Store the result in the test item object
    setattr(item, "rep_" + report.when, report)


# 2. Actor Fixture that brings the Screenplay Actor to life using Playwright, with Evidence Handling
@pytest.fixture
def actor(request: pytest.FixtureRequest):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context(record_video_dir="videos/")
        the_actor = Actor.named("Payer").who_can(BrowseTheWebSynchronously.using(None, context))
        yield the_actor

        # --- TEARDOWN PHASE ---
        # A. Take Screenshot BEFORE closing context
        try:
            page = the_actor.ability_to(BrowseTheWebSynchronously).current_page
            screenshot_bytes = page.screenshot()
            allure.attach(
                screenshot_bytes,
                name="Final_Screenshot",  # "Screenshot_on_Failure",
                attachment_type=allure.attachment_type.PNG
            )
            # Attach HTML
            allure.attach(
                page.content(),
                name="Final_Page_HTML",  # "Page_HTML_on_Failure",
                attachment_type=allure.attachment_type.HTML
            )
        except Exception as e:
            print(f"Could not capture screenshot: {e}")

        # B. Get video path BEFORE closing context
        video_path = None
        if context.pages and context.pages[0].video:
            video_path = context.pages[0].video.path()

        # C. Close context (This is when Playwright actually writes the video file)
        context.close()
        browser.close()

        # D. Attach Video AFTER context is closed
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name="Execution_Video",
                attachment_type=allure.attachment_type.WEBM
            )


# 3. Environment configuration
@pytest.fixture(scope="session")
def app_config():
    """Environment configuration for the application."""
    return {
        "url": os.getenv("PARABANK_URL", "https://parabank.parasoft.com"),
        "username": os.getenv("PARABANK_USER", "john"),
        "password": os.getenv("PARABANK_PASSWORD", "demo")
    }