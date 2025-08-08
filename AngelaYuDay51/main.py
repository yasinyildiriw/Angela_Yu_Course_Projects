import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
from internet_speed import InternetSpeed

######################################## TWITTER COMPLAINT BOT #########################################

speed = InternetSpeed()

load_dotenv()

PROMISED_DOWNLOAD = 150
PROMISED_UPLOAD = 10

e_mail = os.getenv("MAIL")
password = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()
driver.get("https://x.com/i/flow/login")

time.sleep(4)

mail_enter = driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
mail_enter.send_keys(e_mail)
next_button = driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
next_button.click()
time.sleep(6)

# sometimes x.com can ask username question because of many login attempt
try:
    username_enter = driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    username_enter.send_keys("@HOfcode58951")
except NoSuchElementException:
    pass
else:
    next_button_2 = driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    next_button_2.click()
    time.sleep(5)

password_enter = driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_enter.send_keys(password)

sign_in_button = driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
sign_in_button.click()
time.sleep(12)


post_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]')
post_button.click()
time.sleep(2)

write_smthng = driver.find_element(By.CSS_SELECTOR, value='div[aria-multiline="true"][role="textbox"]')

speed_tuple = speed.get_internet_speed()

write_smthng.send_keys(f"Hey @Turkcell, why is my internet speed {speed_tuple[0]} download/{speed_tuple[1]} upload when i pay for {PROMISED_DOWNLOAD} download/ {PROMISED_UPLOAD} upload?")

tweet = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
tweet.click()

driver.quit()