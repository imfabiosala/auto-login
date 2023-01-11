# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Edge('.\edge.exe')

driver.maximize_window()
driver.get('http://helpdesk.frisa.com.br/front/ticket.php')

time.sleep(3)

driver.find_element(By.ID, 'login_name').send_keys('username')
driver.find_element(By.ID, 'login_password').send_keys('password')
driver.find_element(By.NAME, 'submit').click()

time.sleep(10)

# pip install pyinstaller

# pyinstaller -w --windowed --noconsole .\main.py

# pyinstaller -f --onefile .\main.py