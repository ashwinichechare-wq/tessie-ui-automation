import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class IPhonePage(BasePage):
    DYNAMIC_PROMO_SECTION = '[data-unit-id], section, .module-content'

    def main_content(self):
        return self.page.get_by_role("main")

    def iphone_heading(self):
        return self.main_content().get_by_role("heading", name=re.compile("iphone", re.I)).first

    def buy_link(self):
        return self.page.get_by_role("link", name=re.compile("buy", re.I)).first

    def iphone_product_links(self):
        return self.main_content().get_by_role("link", name=re.compile("iphone", re.I))

    def verify_iphone_page_loaded(self):
        self.verify_url_contains("iphone")
        expect(self.iphone_heading()).to_be_visible()

    def verify_title_mentions_iphone(self):
        self.verify_title_contains("iPhone")

    def verify_buy_button_visible(self):
        expect(self.buy_link()).to_be_visible()

    def verify_dynamic_sections_exist(self):
        assert self.get_locator_count(self.DYNAMIC_PROMO_SECTION) > 0

    def get_iphone_link_count(self) -> int:
        return self.iphone_product_links().count()
