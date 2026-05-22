import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Manual driver setup (kept for reference)
# service = Service("/Users/vinu/Documents/WorkSpace/Drivers/chromedriver")
# driver = webdriver.Chrome(service=service)
# Auto ChromeDriver setup using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Rahul")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("vinukumar@gmail.com")
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

#static dropdown >> select
dropdown=Select(driver.find_element(By.CSS_SELECTOR,"Select[id=exampleFormControlSelect1]"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value()



time.sleep(5)

