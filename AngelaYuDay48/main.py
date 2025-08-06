from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

# driver.get("https://www.amazon.com/dp/B09MCVP94B/ref=sspa_dk_detail_1?sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw")
#
# from selenium.webdriver.support.ui import WebDriverWait
# wait = WebDriverWait(driver, 1000)
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"{price_dollar.text}.{price_cents.text}")

# driver.get("https://www.python.org/")
#
# searchbar = driver.find_element(By.NAME, value="q")
# print(searchbar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# link = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a')
# print(link.text)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(doc_link.text)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

################### FIRST CLICK METHOD #########################################
# article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-of-type(2) a")
# article_number.click()

################### SECOND CLICK METHOD #########################################
# content_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portal.click()

################### SEARCH METHOD ###############################
driver.maximize_window()
search = driver.find_element(By.NAME, "search")

# FIRST KEYBOARD METHOD
search.send_keys("ottoman empire",Keys.ENTER)
#SECOND KEYBOARD METHOD
# search.send_keys(Keys.ENTER)




# driver.close() # Close one tab
# driver.quit() # Close all tabs