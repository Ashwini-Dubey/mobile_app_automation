"""
This test is for Android Demo Application - Swag Labs with Python-Appium
"""

import time
import os
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def driver(request):
    """Set up the Appium driver with desired capabilities."""
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:platformVersion": "15",  # Ensure this is the correct version
        "appium:deviceName": "26131FDF6007P2",
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:autoGrantPermissions": True,
        "appium:noReset": True
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

    def test_valid_app_login(self):
        """Verify the app login"""
        username = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Username")
        username.click()
        username.send_keys("standard_user")

        password = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Password")
        password.click()
        password.send_keys("secret_sauce")

        login_button = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
        login_button.click()

        time.sleep(10)

        side_menu = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageView\").instance(1)")
        side_menu.click()

        time.sleep(10)

        logout_button = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"LOGOUT\")")
        logout_button.click()
        

    def test_invalid_app_login(self):
        """Verify the app login"""
        username = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Username")
        username.click()
        username.send_keys("locked_out_user")

        password = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Password")
        password.click()
        password.send_keys("secret_sauce")

        login_button = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
        login_button.click()

        expected_error = "Sorry, this user has been locked out."
        locked_out_error = WebDriverWait(self.driver_instance, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Sorry, this user has been locked out.']"))
        )
        locked_error = locked_out_error.text


        # Assert that the error message matches
        assert expected_error == locked_error, f"Expected error message '{expected_error}', but got '{locked_error}'"

    def test_e2e_purchaseflow(self):
        """Verify the app login"""
        username = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Username")
        username.click()
        username.send_keys("standard_user")

        password = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Password")
        password.click()
        password.send_keys("secret_sauce")

        login_button = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
        login_button.click()

        time.sleep(5)

        backpack = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().description(\"test-ADD TO CART\").instance(0)")
        backpack.click()
        time.sleep(5)
        #bikelight = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-ADD TO CART")
        #bikelight.click()

        cart = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
        cart.click()

        time.sleep(5)
        checkout = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CHECKOUT")
        checkout.click()
        time.sleep(5)
        firstname = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
        firstname.send_keys("Ashwini")
        time.sleep(5)
        lastname = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
        lastname.send_keys("Kumar")
        time.sleep(5)
        postalcode = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
        postalcode.send_keys("122001")

        self.driver_instance.execute_script('mobile: scroll', {'direction': 'down'})

        continuebutton = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
        continuebutton.click()
        time.sleep(5)
        finish = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-FINISH")
        finish.click()
        time.sleep(5)
        successmessage = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().text(\"THANK YOU FOR YOU ORDER\")")
        successmessage.click()
        time.sleep(5)
        backhome = self.driver_instance.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-BACK HOME")
        backhome.click()
        time.sleep(5)
        side_menu = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value="new UiSelector().className(\"android.widget.ImageView\").instance(1)")
        side_menu.click()

        time.sleep(10)

        logout_button = self.driver_instance.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"LOGOUT\")")
        logout_button.click()




