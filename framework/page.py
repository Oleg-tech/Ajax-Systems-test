class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_app_element(self, element_location):
        try:
            element = self.driver.find_element(*element_location)
            return element
        except Exception as e:
            raise e

    def click_app_element(self, element_location):
        element = self.find_app_element(element_location)
        try:
            element.click()
        except Exception as e:
            raise e

    def fill_app_input(self, element_location, value):
        element = self.find_app_element(element_location)
        element.send_keys(value)

    def sleep(self, time_in_seconds):
        self.driver.implicitly_wait(time_in_seconds)
