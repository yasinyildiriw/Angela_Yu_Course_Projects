import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

load_dotenv()
gmail = os.getenv("GMAIL")
password = os.getenv("PASSWORD")

# Create Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()
driver.get("https://www.linkedin.com/")

# Enter the LinkedIn site
enter_with_mail = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/a')
enter_with_mail.click()

mail = driver.find_element(By.ID, value="username")
mail.send_keys(gmail, Keys.TAB)

password_enter = driver.find_element(By.ID, value="password")
password_enter.send_keys(password)
time.sleep(1)

tikla = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[4]/button')
tikla.click()
time.sleep(15)

# Select Jobs Buttons
jobs = driver.find_element(By.XPATH, value='//*[@id="global-nav"]/div/nav/ul/li[3]')
jobs.click()
time.sleep(2)

job_kind = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search by title, skill, or company"]'))
)
job_kind.clear()
job_kind.send_keys("Python Developer",Keys.TAB)

job_place = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="City, state, or zip code"]'))
)
job_place.clear()
job_place.send_keys("London Area, United Kingdom", Keys.ENTER)
time.sleep(4)

easy_apply_button = driver.find_element(By.XPATH, value='//*[@id="searchFilter_applyWithLinkedin"]')
easy_apply_button.click()
time.sleep(5)

for i in range(1,26,1):
    company = driver.find_element(By.XPATH, value=f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]')
    company.click()
    time.sleep(0.2)
    save = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[6]/div/button/span[1]')
    save.click()
    time.sleep(0.2)
time.sleep(2)
main_page = driver.find_element(By.XPATH, value='/html/body/div[6]/header/div/nav/ul/li[1]')
main_page.click()
time.sleep(2)
see_saves = driver.find_element(By.XPATH, value='/html/body/div[6]/div[3]/div/div/div[2]/div/div/aside[1]/div/div[4]/ul/li[1]')
see_saves.click()