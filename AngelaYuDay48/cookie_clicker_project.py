import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_cookie():
    cookie = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
    cookie.click()
    return 0

def find_max_item():
    time.sleep(5)
    cookie_num = driver.find_element(By.XPATH, value='//*[@id="cookies"]').text
    cook = cookie_num.split()[0]
    cookie_number = int(cook)
    unlocked_products = []
    for up in driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled"):
        unlocked_products.append(up.text.split("\n"))

    prices = []
    for j in range(0,len(unlocked_products),1):
        str_price = unlocked_products[j][1]
        prices.append(int(str_price))
        maximum = max(prices)
        max_index = prices.index(maximum)
        if maximum < cookie_number:
            cursor = driver.find_element(By.XPATH, value=f'//*[@id="product{max_index}"]')
            cursor.click()





chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)

driver.maximize_window()
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

language_choice = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
)
language_choice.click()

last_check = time.time()
while True:
    click_cookie()
    if time.time() - last_check >= 15:
        find_max_item()
        last_check = time.time()

