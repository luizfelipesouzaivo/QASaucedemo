import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
HEADLESS = os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes", "sim"}
SLOW_MO = int(os.getenv("SLOW_MO", "0"))
DEFAULT_TIMEOUT = 10_000
