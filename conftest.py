import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: en, ru, es, fr or de'
    )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_argument('--headless')  # убери, если хочешь видеть браузер
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print(f"\nLaunching Chrome with language: {language}")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuitting browser..")
    browser.quit()
