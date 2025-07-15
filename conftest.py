import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


SUPPORTED_LANGUAGES = ['en', 'ru', 'es', 'fr', 'de']

def pytest_addoption(parser):
    parser.addoption(
        '--language', 
        action='store', 
        default='en',
        help='Choose language: en, ru, es, fr or de'
    )


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")

    if browser_language not in SUPPORTED_LANGUAGES:
        raise pytest.UsageError("--language should be one of: en, ru, es, fr, de")

    options = Options()
    #options.add_argument('headless')
    #options.add_argument('window-size=1920x935')
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)
    if browser:
        print("\nSuccess")
    else:
        raise pytest.UsageError("--language should be one of: en, ru, es, fr, de")
    yield browser
    print("\nquit browser..")
    browser.quit()