import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class MacPage(BasePage):
    def main_content(self):
        return self.page.get_by_role("main")

    def mac_heading(self):
        return self.main_content().get_by_text("Mac").first

    def buy_link(self):
        return self.page.locator("a").filter(has_text="Buy").first

    def compare_link(self):
        return self.page.locator("a").filter(has_text="Compare").first

    def mac_product_links(self):
        return self.main_content().locator("a").filter(has_text="MacBook")

    def verify_mac_page_loaded(self):
        self.verify_url_contains("mac")
        expect(self.mac_heading()).to_be_visible()

    def verify_buy_button_visible(self):
        expect(self.buy_link()).to_be_visible()

    def scroll_to_compare(self):
        self.compare_link().scroll_into_view_if_needed()

    def get_mac_product_count(self) -> int:
        return self.mac_product_links().count()
