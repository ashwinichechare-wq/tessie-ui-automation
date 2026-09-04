from pages.home_page import HomePage
from pages.store_page import StorePage


def test_recorded_flow(page):
    home_page = HomePage(page)
    store_page = StorePage(page)

    # Open India-specific homepage
    home_page.open_india_home_page()

    # Navigate to Store from global navigation
    home_page.open_store_page()

    # From Store, go to AirPods category
    store_page.open_airpods_category()

    # Open specific AirPods 4 product (matching nth(5) from the script)
    store_page.open_specific_airpods_product()

    # Finally, navigate to the Support page via global navigation
    home_page.open_support_page()
