from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv, find_dotenv

TARGET_ACCOUNT = "noobumu"
load_dotenv(find_dotenv(), override=True)

class InstaFollower:
    def __init__(self):
        self.e_mail = os.getenv("MAIL")
        self.password = os.getenv("PASSWORD")
        self.username = os.getenv("USERNAME")

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.is_there_still_account = True
        self.follower_number = 0

    def login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        username_entry = self.driver.find_element(By.NAME, "username")
        username_entry.send_keys(self.username)

        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.send_keys(self.password)

        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')
        log_in_button.click()


    def find_followers(self):
        sleep(8)
        search_button = self.driver.find_element(By.XPATH,value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div[2]/div[2]/span')
        search_button.click()
        sleep(2)

        search_bar = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input')
        search_bar.send_keys(TARGET_ACCOUNT)
        sleep(4)
        click_target = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div/div[2]/div/div')
        click_target.click()
        sleep(3)

        target_follower = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/div/header/section[3]/ul/li[2]/div/a/span/span/span')
        self.follower_number = target_follower.text.replace(",","")
        target_follower.click()
        sleep(3)

    def follow(self):
        self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        self.driver.execute_script('scrollBy(0,30)')