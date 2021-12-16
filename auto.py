# pip3 install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://dynamic6.scrape.center/')
driver.execute_script(open('hook.js').read())
time.sleep(2)

for index in range(10):
    print('current page', index)
    btn_next = driver.find_element(By.CSS_SELECTOR, ".btn-next")
    btn_next.click()
    time.sleep(2)


driver.close()
driver.quit()
