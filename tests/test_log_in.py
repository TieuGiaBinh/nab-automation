from pages/log_in_page import LoginPage
import pytest

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("secret_sauce", "axs")]
    )
def test_log_in(username, password):
    login_page = LoginPage()
    login_page.navigate()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    log_in_page.wait_for_page_load()
    assert log_in_page.get_current_url() == "https://www.saucedemo.com/inventory.html", f"Login failed for user: {username}"
