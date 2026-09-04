import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class StorePage(BasePage):
    def main_content(self):
        return self.page.get_by_role("main")

    def store_heading(self):
        return self.main_content().get_by_role("heading", name=re.compile("store", re.I)).first

    def shopping_links(self):
        return self.main_content().get_by_role("link", name=re.compile("shop|buy", re.I))

    def bag_link(self):
        return self.page.get_by_role("link", name=re.compile("bag", re.I)).first

    def verify_store_page_loaded(self):
        self.verify_url_contains("store")
        expect(self.store_heading()).to_be_visible()

    def verify_shopping_links_visible(self):
        expect(self.shopping_links().first).to_be_visible()

    def get_shopping_link_count(self) -> int:
        return self.shopping_links().count()

    def verify_bag_link_available(self):
        expect(self.bag_link()).to_be_visible()
