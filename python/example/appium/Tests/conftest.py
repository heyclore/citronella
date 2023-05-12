import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from citronella import WebPage


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

@pytest.fixture(autouse='true', scope='class')
def web(request):
    from logging import warning
    global driver
    options = UiAutomator2Options()
    options.platformName = 'Android'
    options.app = os.getcwd() + '/APK/ApiDemos-debug.apk'
    warning(options)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    yield WebPage(driver)
    driver.quit()
