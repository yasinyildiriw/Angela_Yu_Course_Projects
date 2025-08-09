from web_scraping import WebScraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
web = WebScraping()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdyYLpQLW5oQxscLxRA918VKDf_vssARM4BXCdfTDDeDjVCCQ/viewform?usp=header")
driver.maximize_window()

address = web.get_address_list()
prices = web.get_rent_price()
links = web.get_links()

sleep(3)
for i in range(44):
    address_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_question.send_keys(address[i])

    rent_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_question.send_keys(prices[i])

    link_question = driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_question.send_keys(links[i])

    send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send_button.click()
    sleep(3)

    another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    sleep(3)

driver.quit()