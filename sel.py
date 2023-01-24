from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait # for waiting for loads
from selenium.webdriver.support import expected_conditions as EC # for expected conditions
import time
import os
from dotenv import load_dotenv

# 0 = any/ default
date_posted = 0
experience_level = ["Internship", "Entry level"] # case sensitive
company = 0
on_site_or_remote = 0
easy_apply = False


load_dotenv()
# cookie vvv
# li_at: AQEDATtQlFkBXXCnAAABha0GVN4AAAGF0RLY3k0AtgoA4T2N2_k46bJcvdjSf9_cu8euPAJivKZv2OTRWZlkJrSm30iJioc0HDUupaKF_znrWYZuSOJ_sZP-4h8MwQ9UeMzkPlVJVftujaTXk_SYDzbL
# school email
# Bot*test123
options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')

# Dev Shared Memory, disable for better perf.
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.linkedin.com/jobs/search/")
driver.add_cookie({"name": "li_at", "value": os.getenv("COOKIE")})
driver.refresh()
#driver.get(
#"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
#username = driver.find_element(
#    By.XPATH, "//*[@id=\"username\"]").send_keys(os.getenv("USERNAME"))
#password = driver.find_element(
#    By.XPATH, "//*[@id=\"password\"]").send_keys(os.getenv("PASSWORD"))
#sign_in = driver.find_element(
#    By.XPATH, "//*[@id=\"organic-div\"]/form/div[3]/button").click()


experience_button = driver.find_element(By.XPATH, f'//button[text()="{"Experience level"}"]')
experience_button.click()
#for exp in experience_level:
    #box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "experience-1")))
    #box = driver.find_element(By.XPATH, f'//button[text()="{exp}"]')
    #box.click()



time.sleep(1000)
driver.quit()