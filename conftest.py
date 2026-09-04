from pathlib import Path

import allure
import pytest
from playwright.sync_api import sync_playwright

from config.settings import settings


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def create_allure_artifact_dirs():
    settings.ALLURE_RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    settings.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def page(request):
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, settings.BROWSER)
        browser = browser_type.launch(
            headless=settings.HEADLESS,
            slow_mo=settings.SLOW_MO,
        )
        context = browser.new_context(
            base_url=settings.BASE_URL,
            viewport={"width": 1440, "height": 900},
        )
        context.set_default_timeout(settings.DEFAULT_TIMEOUT)
        page = context.new_page()

        yield page

        test_failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
        if test_failed:
            screenshot_name = request.node.nodeid.replace("/", "_").replace("\\", "_").replace(":", "_").replace(" ", "_").replace("[", "").replace("]", "")
            screenshot_path = settings.SCREENSHOTS_DIR / f"{screenshot_name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
            allure.attach.file(
                str(screenshot_path),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

        context.close()
        browser.close()
