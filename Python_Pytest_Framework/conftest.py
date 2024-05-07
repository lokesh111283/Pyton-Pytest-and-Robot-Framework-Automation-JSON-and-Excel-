import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PythonSeleniumFramework.LoginData import LoginData

driver =None

#the below method is to pass parameters from command line for browser information
def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome"
    )

#the below method is to pick the browse dynamically it will pick based on the parameter passed (i.e. chrome or firefox)
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browsername")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="E:\\Selenium3\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\Selenium3\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/client")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

#the below method gets the return the JSON data wherever this fixture being used
@pytest.fixture(params=LoginData.testData)
def getdata(request):
    return request.param

#the below method is for generating screenshot
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
