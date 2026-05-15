import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
with sync_playwright() as p:
browser = p.chromium.launch(
headless=False,
slow_mo=300
)

        context = browser.new_context(
            ignore_https_errors=True
        )

        context.set_default_timeout(60000)
        context.set_default_navigation_timeout(60000)

        page = context.new_page()

        page.set_viewport_size({
            "width": 1440,
            "height": 900
        })

        yield page

        if request.node.rep_call.failed:
            screenshot_name = f"screenshots/{request.node.name}.png"
            page.screenshot(path=screenshot_name, full_page=True)

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
outcome = yield
rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)