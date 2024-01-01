import pytest
from selenium import webdriver

from utilities import ReadConfiguration


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfiguration.read_config("basic", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Choose a browser between Chrome/Firefox/Edge")

    driver.implicitly_wait(10)
    driver.maximize_window()
    app_url = ReadConfiguration.read_config("basic", "url")
    driver.get(app_url)
    request.cls.driver = driver

    yield
    driver.quit()
