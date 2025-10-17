class LogInPage(BasePage):
    USERNAME = ('ID', 'user-name')
    PASSWORD = ('ID', 'password')
    LOGIN_BUTTON = ('ID', 'login-button')

    def enter_username(self, username: str):
        self.find_element(cls.USERNAME).send_keys(username)

    def enter_password(self, password: str):
        self.find_element(cls.PASSWORD).send_keys(password)

    def click_login(self):
        self.find_element(cls.LOGIN_BUTTON).click()