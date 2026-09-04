from pathlib import Path

from dotenv import load_dotenv
import os


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")


class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://www.apple.com")
    BROWSER = os.getenv("BROWSER", "chromium").lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "15000"))

    SCREENSHOTS_DIR = ROOT_DIR / "screenshots"
    VIDEOS_DIR = ROOT_DIR / "videos"
    ALLURE_RESULTS_DIR = ROOT_DIR / "allure-results"


settings = Settings()
