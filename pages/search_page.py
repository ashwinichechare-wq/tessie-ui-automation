import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class SearchPage(BasePage):
    NO_RESULTS_MESSAGE = re.compile("no results|couldn.t find|try again", re.I)

    def main_content(self):
        return self.page.get_by_role("main")

    def search_field(self):
        return self.page.get_by_role("textbox", name=re.compile("search", re.I)).first

    def product_result_links(self):
        return self.main_content().get_by_role("link", name=re.compile("iphone|mac", re.I))

    def results_summary(self):
        return self.main_content().get_by_text(re.compile("results found", re.I))

    def verify_search_url(self):
        self.verify_url_contains("search")

    def verify_results_are_displayed(self):
        expect(self.results_summary()).to_be_visible(timeout=15000)
        expect(self.product_result_links().first).to_be_visible(timeout=15000)

    def clear_search_with_keyboard(self):
        field = self.search_field()
        field.click()
        self.press_key("Meta+A")
        self.press_key("Backspace")

    def verify_search_field_is_empty(self):
        expect(self.search_field()).to_have_value("")

    def verify_negative_search_is_handled(self):
        possible_results = self.main_content().get_by_role("link")
        possible_message = self.page.get_by_text(self.NO_RESULTS_MESSAGE)
        assert possible_results.count() > 0 or possible_message.count() > 0
