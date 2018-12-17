import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()

csv_file = open('awards.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)

base_url = 'https://www.theamas.com/winners-database/?winnerKeyword=&winnerYear='

driver.get(base_url)

wait_award = WebDriverWait(driver, 10)       
# DISMISS POPUPS
wait_award.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="onesignal-popover-cancel-button"]')))
driver.find_element_by_xpath('//*[@id="onesignal-popover-cancel-button"]').click()

time.sleep(5)

driver.switch_to_active_element()
driver.find_element_by_xpath('//*[@id="closeButton"]/i')

time.sleep(2)

for year in range(1974, 2018):
    driver.get(base_url + str(year))   
   # wait_award = WebDriverWait(driver, 10)       

    awards = wait_award.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="resultsTable"]')))
    rows = driver.find_elements_by_xpath('//*[@id="resultsTable"]/tbody/tr')

    for row in rows:
        Year = row.find_element_by_xpath('./td[1]/text()').text    # Use relative xpath to locate Year, Category, Winners.
        Category = row.find_element_by_xpath('./td[2]/text()').text
        Winners = row.find_element_by_xpath('./td[3]/p/text()"]').text

        award_dict['Year'] = Year
        award_dict['Category'] = Category
        award_dict['Winners'] = Winners

        writer.writerow(award_dict.values())


        driver.close()