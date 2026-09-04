from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str = "/"):
        self.page.goto(url)
        self.page.wait_for_load_state("domcontentloaded")

    def click_element(self, locator: str):
        self.page.locator(locator).click()

    def fill_text(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def hover_element(self, locator: str):
        self.page.locator(locator).hover()

    def press_key(self, key: str):
        self.page.keyboard.press(key)

    def scroll_to_element(self, locator: str):
        self.page.locator(locator).scroll_into_view_if_needed()

    def wait_for_element(self, locator: str):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        return element

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def verify_title_contains(self, expected_text: str):
        assert expected_text.lower() in self.page.title().lower()

    def verify_url_contains(self, expected_text: str):
        assert expected_text.lower() in self.page.url.lower()

    def is_element_visible(self, locator: str) -> bool:
        return self.page.locator(locator).first.is_visible()

    def get_locator_count(self, locator: str) -> int:
        return self.page.locator(locator).count()
