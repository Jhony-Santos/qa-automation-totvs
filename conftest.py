import os
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def page(request):
    from playwright.sync_api import sync_playwright

    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)

    headless = os.getenv("HEADLESS", "true").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless
        )

        context = browser.new_context(
            ignore_https_errors=True,
            viewport={
                "width": 1440,
                "height": 900
            }
        )

        context.set_default_timeout(60000)
        context.set_default_navigation_timeout(60000)

        page = context.new_page()

        yield page

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            screenshot_name = screenshots_dir / f"{request.node.name}.png"
            page.screenshot(path=str(screenshot_name), full_page=True)

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)