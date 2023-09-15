import pytest

from utils.credentials_utils import (
    valid_email, incorrect_email,
    valid_password, incorrect_password
)


@pytest.mark.parametrize("email, password, expected_result", [
    (valid_email, valid_password, True),            # Correct data
    (incorrect_email, incorrect_password, False),   # Wrong email and password
    (valid_email, incorrect_email, False),          # Wrong password
])
def test_user_login(user_login_fixture, email, password, expected_result):
    test_instance = user_login_fixture
    test_instance.perform_log_in(email=email, password=password)
    test_instance.sleep(time_in_seconds=3)

    actual_result = test_instance.find_main_menu()
    assert actual_result == expected_result
