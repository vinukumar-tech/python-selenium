import time

from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxs = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxs))

for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


Radiobuttons = driver.find_elements(By.XPATH,"//input[@name='radioButton']")
Radiobuttons[1].click()
assert Radiobuttons[1].is_selected()

assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

#alerts
name = "vinu"
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
alert.accept()
#alert.dismiss()
print(alerttext)
assert name in alerttext










time.sleep(3)
driver.quit()