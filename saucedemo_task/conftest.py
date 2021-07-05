import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="firefox",
        help="browser can be: chrome or firefox",
    )
    parser.addoption(
        "--mode",
        action="store",
        default="normal",
        help="browser mode can be: headless or normal",
    )

@pytest.fixture(scope="session")
def driver(request):
    browser = request.config.getoption("--browser")
    mode = request.config.getoption("--mode")

    geckodriver_path = "./saucedemo_task/geckodriver"
    chromedriver_path = "./saucedemo_task/chromedriver"
    download_path = "/home/osachi/selenium/downloads"
    f_type = (
        "application/pdf"
        "vnd.ms-excel,"
        "application/vnd.ms-excel.addin.macroenabled.12,"
        "application/vnd.ms-excel.template.macroenabled.12,"
        "application/vnd.ms-excel.template.macapplication/vnd.ms-excel.sheet.binaryroenabled.12,"
        "application/vnd.ms-excel.sheet.macroenabled.12,"
        "application/octet-stream"
    )
    if browser == "firefox":
        options = FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("browser.download.useDownloadDir", True)
        profile.set_preference("browser.download.dir", download_path)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", f_type)
        options.add_argument("--" + mode)

        driver = webdriver.Firefox(
            profile, executable_path=geckodriver_path, options=options
        )
        driver.maximize_window()
        # driver.set_window_size(1920, 1080)
        yield driver
        driver.quit()

    elif browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--" + mode)
        prefs = {"download.default_directory": download_path}
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            executable_path=chromedriver_path, options=chrome_options
        )
        driver.maximize_window()
        # driver.set_window_size(1920, 1080)
        yield driver
        driver.quit()
    elif browser =='selenoid_firefox':
        capabilities = {
            "browserName": "firefox",
            "browserVersion": "88.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options = FirefoxOptions()

        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.alwaysAsk.force", False)
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.download.dir", download_path)
        options.set_preference("pdfjs.disabled", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", f_type)
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options)
        driver.maximize_window()
        yield driver

        driver.quit()
