from selenium import webdriver
import selenium.webdriver.common.keys as Keys
import booking.constants as const
import os

import json


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r'C:/SeleniumDrivers', teardown=False):
        chrome_options = webdriver.ChromeOptions()
        settings = {
            "recentDestinations": [{
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }],
            "selectedDestinationId": "Save as PDF",
            "version": 2
        }
        prefs = {
            'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--kiosk-printing')
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + self.driver_path
        super(Booking, self).__init__(chrome_options=chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()
        print('Booking.__init__() called')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency: str):
        currency_selector = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]')
        currency_selector.click()

        usd_link = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        usd_link.click()

    def select_place_to_go(self, place: str):
        place_input = self.find_element_by_id('ss')
        place_input.clear()
        place_input.send_keys(place)

    def print_page(self):
        self.execute_script('window.print();')
