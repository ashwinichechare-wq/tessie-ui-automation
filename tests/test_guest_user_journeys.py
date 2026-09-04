from pages.home_page import HomePage
from pages.iphone_page import IPhonePage
from pages.mac_page import MacPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


def test_homepage_validation(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.verify_home_page_loaded()
    home_page.verify_title_contains("Apple")


def test_navigation_menu_has_multiple_links(page):
    home_page = HomePage(page)

    home_page.open_home_page()

    assert home_page.get_navigation_link_count() >= 5


def test_hover_over_mac_navigation(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.hover_mac_navigation()

    home_page.verify_mac_navigation_visible()


def test_store_page_navigation_and_dropdown_style_links(page):
    home_page = HomePage(page)
    store_page = StorePage(page)

    home_page.open_home_page()
    home_page.open_store_page()

    store_page.verify_store_page_loaded()
    store_page.verify_shopping_links_visible()
    assert store_page.get_shopping_link_count() > 0


def test_search_functionality_for_iphone(page):
    home_page = HomePage(page)
    search_page = SearchPage(page)

    home_page.open_home_page()
    home_page.search_for_product("iPhone")

    search_page.verify_search_url()
    search_page.verify_results_are_displayed()


def test_keyboard_actions_clear_search_field(page):
    home_page = HomePage(page)
    search_page = SearchPage(page)

    home_page.open_home_page()
    home_page.open_search()
    home_page.search_input().fill("MacBook")
    search_page.clear_search_with_keyboard()

    search_page.verify_search_field_is_empty()


def test_scroll_to_footer_and_validate_footer(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.scroll_to_footer()

    home_page.verify_footer_visible()


def test_open_contact_apple_link_in_new_tab(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    new_tab = home_page.open_contact_apple_in_new_tab()

    assert "contact" in new_tab.url
    new_tab.close()


def test_mac_and_iphone_buy_button_validation(page):
    home_page = HomePage(page)
    mac_page = MacPage(page)
    iphone_page = IPhonePage(page)

    home_page.open_home_page()
    home_page.open_mac_page()
    mac_page.verify_mac_page_loaded()
    mac_page.verify_buy_button_visible()
    assert mac_page.get_mac_product_count() > 0

    home_page.open_iphone_page()
    iphone_page.verify_iphone_page_loaded()
    iphone_page.verify_title_mentions_iphone()
    iphone_page.verify_buy_button_visible()
    iphone_page.verify_dynamic_sections_exist()
    assert iphone_page.get_iphone_link_count() > 0


def test_mobile_menu_validation(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.open_mobile_menu()

    home_page.verify_mobile_menu_visible()


def test_negative_search_does_not_break_page(page):
    home_page = HomePage(page)
    search_page = SearchPage(page)

    home_page.open_home_page()
    home_page.search_for_product("zzzz_non_existing_apple_product_12345")

    search_page.verify_search_url()
    search_page.verify_negative_search_is_handled()
