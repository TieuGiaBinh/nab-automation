class LogInPage(BasePage):
    USERNAME = ('ID', 'user-name')
    PASSWORD = ('ID', 'password')
    LOGIN_BUTTON = ('ID', 'login-button')
    URL = 'https://www.saucedemo.com/'
    CART_ICON = ('CSS_SELECTOR', '#shopping_cart_container > a')

    def enter_username(self, username: str):
        self.find_element(cls.USERNAME).send_keys(username)

    def enter_password(self, password: str):
        self.find_element(cls.PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(cls.LOGIN_BUTTON).click()

    def navigate(self):
        self.driver.get(cls.URL)

    def wait_for_page_load(self):
        self.find_element(cls.CART_ICON)

    def get_current_url(self):
        return self.driver.current_url