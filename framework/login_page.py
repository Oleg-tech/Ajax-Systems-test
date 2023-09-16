from .page import Page
from utils.element_locations_utils import (
    login_button, submit_form_button, email_field,
    password_field, displayed_menu
)


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def perform_log_in(self, email: str, password: str):
        # Press "Log In" button
        self.click_app_element(element_location=login_button)

        # Fill Email field
        self.fill_app_input(element_location=email_field, value=email)

        # Fill Password field
        self.fill_app_input(element_location=password_field, value=password)

        # Press "Log In"(Submit) button
        self.click_app_element(element_location=submit_form_button)

    def find_main_menu(self):
        try:
            element = self.find_app_element(displayed_menu)
            if element:
                return True
            return False
        except Exception as e:
            return False
