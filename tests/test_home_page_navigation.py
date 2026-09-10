from pages.home_page import HomePage


def test_recorded_flow(page):
    home_page = HomePage(page)

    home_page.open_home_page()
    home_page.bring_page_to_front()
    home_page.click_apple_logo_link(force=True)
    home_page.click_apple_logo_link(force=True)
