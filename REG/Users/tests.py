import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import time
from selenium.webdriver.common.by import By

class TestLandingChrome(unittest.TestCase):
    def setUp(self):
        # Specify the path to your ChromeDriver if it's not in your PATH
        # service = Service(executable_path='/usr/bin/chromedriver')  #This path is for ubuntu
        service = Service(executable_path='/opt/homebrew/bin/chromedriver')  # This path is for mac
        chrome_options = Options()
        # Optional: add any Chrome options you need here
        # chrome_options.add_argument('--headless')  # Run in headless mode if you don't need a GUI
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000")

    def test_register_button(self):
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        time.sleep(3)

    def test_login_button_(self):
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()  # Ensure this is called with parentheses

if __name__ == '__main__':
    unittest.main()

def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_number_with_digits(digits):
    """Generate a random number with a specified number of digits."""
    if digits <= 0:
        raise ValueError("Number of digits must be positive")
    lower_bound = 10 ** (digits - 1)
    upper_bound = 10 ** digits - 1
    return random.randint(lower_bound, upper_bound)

def generate_random_email():
    """Generate a random email address."""
    username = generate_random_string(8)
    domain = generate_random_string(5)
    return f"{username}@{domain}.com"

def generate_random_password(length=12):
    """Generate a random password with letters, digits, and special characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

name = generate_random_string(6)
number = generate_random_number_with_digits(10)
email = generate_random_email()
password = generate_random_password()

class TestSignupChrome(unittest.TestCase):
    def setUp(self):
        # Specify the path to your ChromeDriver if it's not in your PATH
        # service = Service(executable_path='/usr/bin/chromedriver')  # This path is for ubuntu
        service = Service(executable_path='/opt/homebrew/bin/chromedriver')  # This path is for mac

        chrome_options = Options()
        # Optional: add any Chrome options you need here
        # chrome_options.add_argument('--headless')  # Run in headless mode if you don't need a GUI
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000")
#
    def test_signup_chrome(self):
        # Fill in the form fields
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        self.driver.find_element(By.NAME, 'name').send_keys(name)
        self.driver.find_element(By.NAME, 'number').send_keys(number)
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'password').send_keys("2370")  # Assuming 'password' is the name attribute
        # Click the signup button
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
#
    def test_signup_empty_fields(self):
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        # Submit the form without filling in any fields
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)
    def test_signup_email_address_already_exist(self):
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        self.driver.find_element(By.NAME, 'name').send_keys(name)
        self.driver.find_element(By.NAME, 'number').send_keys(number)
        self.driver.find_element(By.NAME, 'email').send_keys("krr@gmail.com")
        self.driver.find_element(By.NAME, 'password').send_keys("Raj@2370")
        # Click the signup button
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        # error_message = self.driver.find_element(By.XPATH, "//div[@class='error_messages']").is_displayed()
        # self.assertTrue(error_message)
        time.sleep(5)
#
    def test_clicking_login_now_button_logo(self):
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()  # Ensure this is called with parentheses

if __name__ == '__main__':
    unittest.main()

class TestLoginChrome(unittest.TestCase):

    def setUp(self):
        # Specify the path to your ChromeDriver if it's not in your PATH
        service = Service(executable_path='/usr/bin/chromedriver')  # This path is for ubuntu
        service = Service(executable_path='/opt/homebrew/bin/chromedriver')  # This path is for mac

        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # Optional: add any Chrome options you need here
        # chrome_options.add_argument('--headless')  # Run in headless mode if you don't need a GUI
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/")


    def test_login_successful(self):
        # Fill in the login form with valid credentials
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        self.driver.find_element(By.NAME, 'email').send_keys("krr@gmail.com")
        self.driver.find_element(By.NAME, 'password').send_keys("Raj@2370")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        # Wait for the page to load (or use WebDriverWait for a more robust solution)
        time.sleep(3)

#
    def test_login_invalid_email(self):
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        # Fill in the login form with an invalid email
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'password').send_keys("2370")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').submit()  # Or find the submit button and click it
        # Wait for the page to load (or use WebDriverWait for a more robust solution)
        time.sleep(3)

    #
    def test_login_invalid_password(self):
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()

        # Fill in the login form with an invalid password
        self.driver.find_element(By.NAME, 'email').send_keys("a@gmail.com")
        self.driver.find_element(By.NAME, 'password').send_keys("86587")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').submit()  # Or find the submit button and click it
        time.sleep(3)

    def test_login_empty_fields(self):
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').submit()  # Or find the submit button and click it
        time.sleep(3)

    def test_clicking_signup_now_button_logo(self):
        self.driver.find_element(By.XPATH, '//a[@href="/log/"]').click()
        self.driver.find_element(By.XPATH, '//a[@href="/reg/"]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()  # Ensure this is called with parentheses

if __name__ == '__main__':
    unittest.main()



