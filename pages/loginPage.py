from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    usernameInput = (By.ID, "mat-input-0")
    passwordInput = (By.ID, "mat-input-1")
    loginButton = (By.ID, "login__submit")

