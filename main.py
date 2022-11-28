import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

DRIVER = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://magento.softwaretestingboard.com/'
MAIL = 'roni_cost@example.com'
PASSWORD = 'roni_cost3@example.com'


def login():
    # ir a login page
    login_button = DRIVER.find_element(By.CLASS_NAME, "authorization-link")
    login_button.click()
    # insertar credenciales
    email_field = DRIVER.find_element(By.ID, "email")

    password_field = DRIVER.find_element(By.ID, "pass")

    email_field.send_keys(MAIL)

    password_field.send_keys(PASSWORD)

    # pasar credenciales
    submit_btn = DRIVER.find_element(By.ID, "send2")
    submit_btn.click()
    # dar mensaje de exito o de error


def main():
    DRIVER.get(URL)
    login()


main()
