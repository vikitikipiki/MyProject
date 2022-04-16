import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language= ru, n, fi, de, en, fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language=request.config.getoption("language")
    options=Options()
    options.add_experimental_option ('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


#pytest -s -v --browser_name=chrome test_parser.py
#pytest -s -v --browser_name=firefox test_parser.py 