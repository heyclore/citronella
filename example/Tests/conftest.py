from selenium import webdriver
from citronella import SelfBrowser
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot = driver.get_screenshot_as_base64()
            extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.skip("previous test failed (%s)" %previousfailed.name)

@pytest.fixture(scope='class', autouse=True)
def browser(request):
    # if there's a way aside using global variable for hook to html report ?
    global driver
    driver = webdriver.Chrome()
    browser = SelfBrowser(driver)
    request.cls.browser = browser
    yield
    driver.quit()
