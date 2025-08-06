from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

driver.get("https://www.python.org/")

events = {}
for i in range(0,5,1):
    content = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]').text
    time = content.split("\n")[0]
    name = content.split("\n")[1]
    events[i] = {'time': time, 'name': name}
print(events)