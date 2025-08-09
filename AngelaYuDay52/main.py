import time
from selenium.common.exceptions import NoSuchElementException
from insta_follower import InstaFollower
from selenium.webdriver.common.by import By

insta = InstaFollower()

insta.login()
insta.find_followers()
time.sleep(4)

followers_pop_up = insta.driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

for i in range(1,int(insta.follower_number),1):
    try:
        pop_up = insta.driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]')
        pop_up.click()
    except NoSuchElementException:
        follow_account = insta.driver.find_element(By.XPATH,f'/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button')
        follow_account.click()
        time.sleep(1)
        insta.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 2;", followers_pop_up)
