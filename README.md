# Apple UI Automation Framework

This project is a beginner-friendly, real-world UI automation framework for guest user journeys on `https://www.apple.com`.

It uses:

- Python
- Playwright
- PyTest
- Page Object Model
- python-dotenv

## 1. Folder Structure

```text
apple_ui_framework/
├── .env
├── README.md
├── conftest.py
├── pytest.ini
├── requirements.txt
├── config/
│   ├── __init__.py
│   └── settings.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── iphone_page.py
│   ├── mac_page.py
│   ├── search_page.py
│   └── store_page.py
├── tests/
│   ├── __init__.py
│   └── test_guest_user_journeys.py
```

## 2. File-by-File Explanation

### `.env`

What it is: A local environment configuration file.

Why it is needed: Test execution settings should not be hardcoded in test files. This lets you switch browser, headless mode, slow motion, and base URL without changing framework code.

How it works:

```env
BASE_URL=https://www.apple.com
BROWSER=chromium
HEADLESS=false
SLOW_MO=500
DEFAULT_TIMEOUT=15000
```

Real-world importance: In companies, the same tests often run against QA, staging, production, different browsers, and CI pipelines. `.env` makes that flexible.

### `requirements.txt`

What it is: The dependency list for the project.

Why it is needed: A new engineer or CI server can install the exact tools needed to run the framework.

How it works:

```bash
pip install -r requirements.txt
```

### `pytest.ini`

What it is: PyTest configuration.

Why it is needed: It centralizes test discovery rules and default command options.

How it works:

- `testpaths = tests` tells PyTest where tests live.
- `addopts = -v` runs tests in verbose mode by default.

### `config/settings.py`

What it is: A single place to load and expose configuration.

Why it is needed: Tests and fixtures should read settings from one clean source instead of calling `os.getenv()` everywhere.

How it works:

- Loads `.env` using `python-dotenv`.
- Converts text values into useful Python values.
- Defines settings that are used by the Playwright fixture.

### `conftest.py`

What it is: The fixture center of the framework.

Why it is needed: PyTest automatically discovers `conftest.py`, so fixtures can be reused by every test without imports.

How it works:

- `page`: Starts Playwright, opens the selected browser, creates one browser context, creates one page, gives that page to the test, then closes the context and browser after the test.

Real-world importance: Even with one simple fixture, tests stay clean because browser setup and teardown are not repeated inside every test.

### `pages/base_page.py`

What it is: The parent class for all page objects.

Why it is needed: Common Playwright actions should be written once and reused everywhere.

Methods:

- `open_url(url)`: Opens a URL and waits for the DOM to load.
- `click_element(locator)`: Clicks an element by locator.
- `fill_text(locator, text)`: Types text into an input.
- `hover_element(locator)`: Performs mouse hover.
- `press_key(key)`: Sends keyboard input such as `Enter` or `Meta+A`.
- `scroll_to_element(locator)`: Scrolls until an element is in view.
- `wait_for_element(locator)`: Waits until an element is visible.
- `get_text(locator)`: Returns visible text from an element.
- `verify_title_contains(text)`: Checks browser title text.
- `verify_url_contains(text)`: Checks current URL text.
- `is_element_visible(locator)`: Returns true or false for visibility.
- `get_locator_count(locator)`: Counts matching elements.

Real-world importance: Base page methods reduce duplicate code and give the framework a consistent interaction style.

### Page Object Files

Each page class inherits from `BasePage`.

#### `pages/home_page.py`

Covers homepage guest actions:

- Open Apple homepage.
- Validate logo and URL.
- Count navigation links.
- Hover Mac navigation.
- Open Store, Mac, and iPhone pages.
- Use search.
- Scroll to footer.
- Open a link in a new tab.
- Validate mobile menu.

#### `pages/search_page.py`

Covers search behavior:

- Validate search URL.
- Validate search results.
- Clear search input with keyboard shortcuts.
- Validate negative search handling.

#### `pages/mac_page.py`

Covers Mac page guest behavior:

- Validate Mac page URL and page content.
- Validate Buy button.
- Count Mac product/navigation tiles.
- Scroll to Compare.

#### `pages/iphone_page.py`

Covers iPhone page guest behavior:

- Validate URL and title.
- Validate Buy button.
- Count iPhone product links.
- Validate dynamic promotional sections.

#### `pages/store_page.py`

Covers Store page guest behavior:

- Validate Store page.
- Validate shopping links.
- Validate bag link.

### `tests/test_guest_user_journeys.py`

What it is: The test suite for Apple guest user scenarios.

Why it is needed: This is where business-readable tests live.

How it works:

- Each test creates page object instances.
- Tests call page object methods instead of raw Playwright code.
- Tests do not use decorators such as Allure labels or PyTest markers, keeping the test file beginner-friendly.

## 3. Test Case Explanations

1. `test_homepage_validation`
   Validates Apple homepage loads, title contains Apple, and logo is visible.

2. `test_navigation_menu_has_multiple_links`
   Counts navigation links to demonstrate multiple locator handling.

3. `test_hover_over_mac_navigation`
   Uses Playwright hover to validate navigation behavior.

4. `test_store_page_navigation_and_dropdown_style_links`
   Navigates to Store and validates shopping links.

5. `test_search_functionality_for_iphone`
   Opens search, enters `iPhone`, presses Enter, and validates results.

6. `test_keyboard_actions_clear_search_field`
   Demonstrates keyboard shortcuts using `Meta+A` and `Backspace`.

7. `test_scroll_to_footer_and_validate_footer`
   Uses scroll handling and footer visibility validation.

8. `test_open_support_link_in_new_tab`
   Uses `expect_popup()` to validate a new browser tab/window.

9. `test_mac_and_iphone_buy_button_validation`
   Validates product pages, URLs, titles, dynamic sections, counts, and Buy links.

10. `test_mobile_menu_validation`
    Resizes viewport and validates responsive mobile navigation.

11. `test_negative_search_does_not_break_page`
    Searches for an invalid product name and validates the page handles it gracefully.

## 4. Commands to Run

Create and activate a virtual environment:

```bash
cd /Users/vikashmishra/Desktop/Apple/apple_ui_framework
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Run all tests:

```bash
pytest
```

Run in headless mode:

```env
HEADLESS=true
```

Switch browser:

```env
BROWSER=firefox
```

Supported browser values:

- `chromium`
- `firefox`
- `webkit`


