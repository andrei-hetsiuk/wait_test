import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print(type(browser))
    browser.quit()
    
# def pytest_addoption(parser):
   
    # parser.addoption('--language', action='store', default=None,
                     # help="Choose the language")


# @pytest.fixture(scope="function")
# def browser(request):
    # user_language = request.config.getoption("language")
    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # browser = webdriver.Chrome(options=options)
    # yield browser
    # print("\nquit browser..")
    # browser.quit()

