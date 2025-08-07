import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

################### THIS PROGRAM CAN APPLY TO THE FIRST EASY
################### APPLY JOB IN THE LINKEDIN JOBS PAGE
################### WITH GIVEN SEARCH KEYS

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
time.sleep(3)

easy_apply_button = driver.find_element(By.XPATH, value='//*[@id="searchFilter_applyWithLinkedin"]')
easy_apply_button.click()
time.sleep(4)

easy_apply = driver.find_element(By.XPATH, value='//*[@id="jobs-apply-button-id"]/span')
easy_apply.click()
time.sleep(2)

# Questions
country_code = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/div/select/option[235]')
country_code.click()

phone_number = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[4]/div/div/div[1]/div/input')
phone_number.send_keys("1234567891")

next_operator = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
next_operator.click()
time.sleep(2)

next_operator2 = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
next_operator2.click()
time.sleep(2)

question1 = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[1]/div/div/div[1]/div/input')
question1.send_keys("5")

question2 = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[2]/div/div/div[1]/div/input')
question2.send_keys("0")

question3 = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div/div/select/option[3]')
question3.click()

# Apply Button
last_button = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
last_button.click()
