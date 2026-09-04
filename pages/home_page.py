import re
from urllib.parse import urljoin

from playwright.sync_api import expect

from pages.base_page import BasePage


class HomePage(BasePage):
    GLOBAL_NAV = "#globalnav"
    FOOTER = "footer"
    MOBILE_MENU_BUTTON = ".globalnav-menutrigger-button"

    def open_home_page(self):
        self.open_url("/")

    def global_navigation(self):
        return self.page.locator(self.GLOBAL_NAV)

    def main_content(self):
        return self.page.get_by_role("main")

    def footer(self):
        return self.page.locator(self.FOOTER)

    def apple_logo_link(self):
        return self.global_navigation().get_by_role("link", name="Apple", exact=True)

    def store_nav_link(self):
        return self.global_navigation().get_by_role("link", name="Store", exact=True)

    def mac_nav_link(self):
        return self.global_navigation().get_by_role("link", name="Mac", exact=True)

    def iphone_nav_link(self):
        return self.global_navigation().get_by_role("link", name="iPhone", exact=True)

    def search_button(self):
        return self.global_navigation().get_by_role("button", name=re.compile("search", re.I))

    def search_input(self):
        return self.page.get_by_role("textbox", name=re.compile("search", re.I)).first

    def verify_home_page_loaded(self):
        expect(self.apple_logo_link()).to_be_visible()
        self.verify_url_contains("apple.com")

    def get_navigation_link_count(self) -> int:
        return self.global_navigation().get_by_role("link").count()

    def hover_mac_navigation(self):
        self.mac_nav_link().hover()

    def verify_mac_navigation_visible(self):
        expect(self.mac_nav_link()).to_be_visible()

    def open_store_page(self):
        self.store_nav_link().click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_mac_page(self):
        self.mac_nav_link().click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_iphone_page(self):
        self.iphone_nav_link().click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_search(self):
        self.search_button().click()
        expect(self.search_input()).to_be_visible()

    def search_for_product(self, product_name: str):
        self.open_search()
        search_input = self.search_input()
        search_input.fill(product_name)
        search_input.press("Enter")
        self.page.wait_for_url("**/search/**")
        self.page.wait_for_load_state("domcontentloaded")

    def scroll_to_footer(self):
        self.scroll_to_element(self.FOOTER)

    def verify_footer_visible(self):
        expect(self.footer()).to_be_visible()

    def get_buy_link_count(self) -> int:
        return self.main_content().get_by_role("link", name=re.compile("buy", re.I)).count()

    def open_contact_apple_in_new_tab(self):
        self.scroll_to_footer()
        contact_link = self.footer().get_by_role("link", name="Contact Apple", exact=True)
        contact_url = urljoin(self.page.url, contact_link.get_attribute("href"))
        new_page = self.page.context.new_page()
        new_page.goto(contact_url)
        new_page.wait_for_load_state("domcontentloaded")
        return new_page

    def open_mobile_menu(self):
        self.page.set_viewport_size({"width": 390, "height": 844})
        self.page.locator(self.MOBILE_MENU_BUTTON).click()

    def verify_mobile_menu_visible(self):
        expect(self.global_navigation()).to_be_visible()

    def open_india_home_page(self):
        self.open_url("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")

    def open_store_from_india_home(self):
        self.open_india_home_page()
        self.open_store_page()

    def open_support_page(self):
        support_link = self.global_navigation().get_by_role("link", name="Support", exact=True).first
        support_link.click()
        self.page.wait_for_load_state("domcontentloaded")
