import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()

e_mail = os.getenv("MAIL")
password = os.getenv("PASSWORD")
phone_number = os.getenv("PHONE")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()
driver.get("https://tinder.com/")
time.sleep(2)
sign_in_button =driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
sign_in_button.click()
time.sleep(1)
sign_with_face = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')
sign_with_face.click()
time.sleep(2)

windows = driver.window_handles
main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

mail = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
mail.send_keys(e_mail,Keys.TAB)
fb_password = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
fb_password.send_keys(password)
fb_entry = driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
fb_entry.click()
time.sleep(2)
continue_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]/div/span/span')
continue_button.click()
driver.switch_to.window(main_window)
time.sleep(10)

phone = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/input')
phone.send_keys(phone_number)

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[3]/button'))
)
next_button.click()
time.sleep(20)


location_allow =WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]'))
)
location_allow.click()
time.sleep(2)

notification = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div/div/div[3]/button[2]')
notification.click()

for i in range(1,100,1):
    time.sleep(2)
    swipe_left = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[2]/button')
    swipe_left.click()
    print(f"{i}. swiped lef")

driver.quit()





