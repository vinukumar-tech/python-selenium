import time

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/vinu/Documents/WorkSpace/Drivers/chromedriver")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
print(len(countries))


for country in countries:
    if country.text == "India":
     country.click()
     break

#print(driver.find_element(By.ID, "autosuggest").text)
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") =="India"


time.sleep(2)
driver.quit()