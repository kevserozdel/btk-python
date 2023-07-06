from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email = "" # your email
password = "" # your password

class Twitter:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(self.email)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(self.password)
        self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()
        time.sleep(5)

login = Twitter(email, password)
login.signIn()