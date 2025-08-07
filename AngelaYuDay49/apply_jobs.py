import time
from selenium import webdriver
from selenium.common import NoSuchElementException
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
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4271013415&f_AL=true&geoId=101356765&keywords=python&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

sign_in = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/section/div/div/div/div[2]/button')
sign_in.click()

mail = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/section/div/div/form/div[1]/div[1]/div/div/input')
mail.send_keys(gmail, Keys.TAB)

password_enter = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/section/div/div/form/div[1]/div[2]/div/div/input')
password_enter.send_keys(password)

sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/section/div/div/form/div[2]/button')
sign_in_button.click()
time.sleep(10)

for i in range(1,26,1):
    job = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f'/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]'))
    )
    job.click()
    print(f"{i}. company clicked ")

    easy = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button--top-card button")))
    easy.click()
    print(f"{i}. easy apply button clicked ")
    time.sleep(2)
    try:
        submit = driver.find_element(By.XPATH,value='/html/body/div[4]/div/div/div[2]/div/div/form/footer/div[3]/button')
        time.sleep(2)
    except NoSuchElementException:
        exit_button = driver.find_element(By.XPATH, value='/html/body/div[4]/div/div/button')
        exit_button.click()
        discard_button = driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div[3]/button[1]')
        discard_button.click()
        time.sleep(2)
        print(f"{i}. comp hard way")
    else:
        time.sleep(2)
        submit.click()
        print(f"{i}. application sent")

