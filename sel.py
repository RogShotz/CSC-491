from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


load_dotenv()
# cookie vvv
# li_at: AQEDATtQlFkBXXCnAAABha0GVN4AAAGF0RLY3k0AtgoA4T2N2_k46bJcvdjSf9_cu8euPAJivKZv2OTRWZlkJrSm30iJioc0HDUupaKF_znrWYZuSOJ_sZP-4h8MwQ9UeMzkPlVJVftujaTXk_SYDzbL
# school email
# Bot*test123
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')

# Dev Shared Memory, disable for better perf.
options.add_argument('--disable-dev-shm-usage')
print(os.getenv("COOKIE"))
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
driver.get("https://www.linkedin.com/jobs/search/")
driver.add_cookie({"name": "li_at", "value": os.getenv("COOKIE")})
driver.refresh()

# driver.get(
# "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
# username = driver.find_element(
#     By.XPATH, "//*[@id=\"username\"]").send_keys(os.getenv("USERNAME"))
# password = driver.find_element(
#     By.XPATH, "//*[@id=\"password\"]").send_keys(os.getenv("PASSWORD"))
# sign_in = driver.find_element(
#     By.XPATH, "//*[@id=\"organic-div\"]/form/div[3]/button").click()

time.sleep(1000)
driver.quit()

# 0 = any/ default
date_posted = 0
experience_level = 0
company = 0
on_site_or_remote = 0
easy_apply = False
