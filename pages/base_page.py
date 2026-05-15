from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url, wait_until="domcontentloaded", timeout=60000)

    def click(self, locator):
        self.page.locator(locator).click(timeout=60000)

    def fill(self, locator, text):
        self.page.locator(locator).fill(text, timeout=60000)

    def text_visible(self, text):
        expect(self.page.get_by_text(text)).to_be_visible(timeout=60000)

    def wait_for_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible(timeout=60000)