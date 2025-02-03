import time
import os
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller # Auto-downloads correct ChromeDriver

@pytest.fixture(scope="class")
def driver(request):

    # Automatically download the matching chromedriver version"
    chromedriver_path = "/Users/ashwinidubey/Desktop/Automation_Revamped/Python/MobileAutomation_Appium/chromedriver"

    print(f"Chromedriver installed at: {chromedriver_path}")

    """Set up the Appium driver with desired capabilities."""
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:platformVersion": "15",  # Ensure this is the correct version
        "appium:deviceName": "26131FDF6007P2",
        "browserName" : "Chrome",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:autoGrantPermissions": True,
        "appium:noReset": True,
        "appium:chromedriverExecutable": "/Users/ashwinidubey/Desktop/Automation_Revamped/Python/MobileAutomation_Appium/chromedriver"

    })

    # Initialize driver
    driver_instance = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Attach driver to test class
    request.cls.driver_instance = driver_instance

    # Start screen recording
    driver_instance.start_recording_screen()

    yield driver_instance

    # Stop recording & quit driver
    driver_instance.stop_recording_screen()
    driver_instance.quit()


@pytest.mark.usefixtures("driver")
class TestSwagLabsApp:

    def test_chromeLaunch(self):
        """
        Open Chrome & Visit Google.
        """
        self.driver_instance.get("https://www.google.com")
        time.sleep(10)