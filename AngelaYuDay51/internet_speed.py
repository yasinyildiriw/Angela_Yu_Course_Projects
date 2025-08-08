import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class InternetSpeed:
    def __init__(self):
        self.chrome_opt = webdriver.ChromeOptions()
        self.chrome_opt.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_opt)
        self.download_speed = 0
        self.upload_speed = 0
    def get_internet_speed(self):
        '''
        Enters speedtest.net and fetch the tuple of download and upload speeds
        :return:
        '''
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        time.sleep(4)
        go = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go.click()
        time.sleep(70)
        self.download_speed = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.upload_speed = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return self.download_speed,self.upload_speed
