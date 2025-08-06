from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("jack", Keys.TAB)
l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("jackknife", Keys.TAB)
mail = driver.find_element(By.NAME, value="email")
mail.send_keys("jackieboy@gmail.com", Keys.TAB)
register = driver.find_element(By.CSS_SELECTOR, value="form button")
register.send_keys(Keys.ENTER)