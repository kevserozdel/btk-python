from selenium import webdriver
import time

url ="https://github.com"

driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)
driver.maximize_window() #tamekran
driver.save_screenshot("github.com-homepage.png") 
print(driver.title) #açılan websitenin title'ını yazar.

url = "https://github.com/kevserozdel"
driver.get(url)
time.sleep(2)
driver.back() #bir önceki yazılan url'ye geri döner.
time.sleep(2) #2 saniye bekletme
driver.close() #tarayıcıyı kapatır