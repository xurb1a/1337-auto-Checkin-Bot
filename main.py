from time import sleep
import getpass
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

class Auth:
    delay = 5
    url = None
    user_input = "user_email"
    password_input = "user_password"
    connect_button = "commit"
    browser = None

    def __init__(self, url, email, password):
        self.url = url
        self.username = email
        self.password = password

    def launchBrowser(self, headless=False):
        options = Options()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.browser.get(self.url)
        print("Browser Initiated and navigated to:", self.url)

    def login(self):
        Browser = self.browser
        Username = self.username
        Password = self.password
        username_log = Browser.find_element(By.ID, self.user_input)
        password_log = Browser.find_element(By.ID, self.password_input)
        username_log.send_keys(Username)
        password_log.send_keys(Password)
        print("Logging in ...", end=" ")
        Browser.find_element(By.NAME, self.connect_button).click()
        time.sleep(self.delay)
        print('[DONE]')

    def check(self):
        text = self.browser.find_element(By.CSS_SELECTOR, "#subs-content > div.row > div > p").text
        print(text)
        return text[:45] != "De nouveaux creneaux ouvriront prochainement."

    def refresh(self):
        self.browser.refresh()

    def disconnected(self):
        self.browser.get(self.url)
        try:
            self.browser.find_element(By.ID, self.user_input)
        except NoSuchElementException:
            return False
        print("Got disconnected..")
        return True

# === Script Start ===

url = 'https://candidature.1337.ma/users/sign_in'
email = "burritoshot53@gmail.com"
password = getpass.getpass('Enter password: ')  # or hardcode if you want
c = Auth(url, email, password)
c.delay = 2
c.launchBrowser()
c.login()

isCheckinAvailable = not c.check()
i = 1
while isCheckinAvailable:
    print("{}: Attempt {}, check-in is not available yet .. ".format(
        datetime.datetime.now(), i))
    sleep(30)
    c.refresh()
    if c.disconnected():
        c.login()
    isCheckinAvailable = not c.check()
    i += 1
