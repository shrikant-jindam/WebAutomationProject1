from selenium import webdriver
import pytest
import pytest_html


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    elif browser == 'firebox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

################### html report###############

def pytest_configure(config):
    #config.option_metadata['Project Name'] = 'Web Automation Framework'
    #config.option_metadata['Module Name'] = 'Login'
    #config.option_metadata['Tester'] = 'Shrikant'

    config.option.metadata={
        'Project Name' : 'Web Automation Framework',
        'Module Name' : 'Login',
        'Tester' : 'Shrikant'
    }

#It is the hook for delete/modify environment info to html report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
