from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # for waiting for loads
from selenium.webdriver.support import (
    expected_conditions as EC,
)  # for expected conditions
import time
import os
from dotenv import load_dotenv

# dataum
experience_dict = {
    "init_equal": "E",  # what the filter has to apply before any sub additions
    "internship": 1,
    "entry_level": 2,
    "associate": 3,
    "mid-senior level": 4,
    "director": 5,
    "executive": 6,
}
job_type_dict = {"init_equal": "JT", "full-time": "F", "part-time": "P", "contract": "C",
                 "temporary": "T", "volunteer": "V", "internship": "I", "other": "O"}

work_type_dict = {"init_equal": "WT", "on-site": 1, "remote": 2, "hybrid": 3}

# 0 = any/ default
date_posted = 0
experience = ["internship", "entry_level"]
company = 0
job_type = ["full-time", "contract"]
work_type = ["remote", "hybrid"]
easy_apply = False


load_dotenv()
# cookie vvv
# li_at: AQEDATtQlFkBXXCnAAABha0GVN4AAAGF0RLY3k0AtgoA4T2N2_k46bJcvdjSf9_cu8euPAJivKZv2OTRWZlkJrSm30iJioc0HDUupaKF_znrWYZuSOJ_sZP-4h8MwQ9UeMzkPlVJVftujaTXk_SYDzbL
# school email
# Bot*test123
options = Options()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")

# Dev Shared Memory, disable for better perf.
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.linkedin.com/jobs/search/")
driver.add_cookie({"name": "li_at", "value": os.getenv("COOKIE")})
driver.refresh()
# driver.get(
# "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
# username = driver.find_element(
#    By.XPATH, "//*[@id=\"username\"]").send_keys(os.getenv("USERNAME"))
# password = driver.find_element(
#    By.XPATH, "//*[@id=\"password\"]").send_keys(os.getenv("PASSWORD"))
# sign_in = driver.find_element(
#    By.XPATH, "//*[@id=\"organic-div\"]/form/div[3]/button").click()

# experience_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'//button[text()="{"Experience level"}"]')))
# experience_button = driver.find_element(By.XPATH, f'//button[text()="{"Experience level"}"]')
# experience_button.click()
# example of linked in URL path for experience
# append for any new search term an &f_
# for experience its you add onto that 'E=1' for first option, after that if there is multiple added '%2C {the experience level type}'

#filter_url = driver.current_url
#for exp in experience:
#    if exp == experience[0]:
#        filter_url += f"{pre_filter}E={experience_dict.get(exp)}"
#    else:
#        filter_url += f"{pre_addtional}{experience_dict.get(exp)}"
#
#for jt in job_type:
#    if jt == job_type[0]:
#        filter_url += f"{pre_filter}JT={job_type_dict.get(jt)}"
#    else:
#        filter_url += f"{pre_addtional}{job_type_dict.get(jt)}"
#
#for jt in job_type:
#    if jt == job_type[0]:
#        filter_url += f"{pre_filter}JT={job_type_dict.get(jt)}"
#    else:
#        filter_url += f"{pre_addtional}{job_type_dict.get(jt)}"


def add_filter(f_type: str, f_type_dict: dict):
    out = ""
    pre_filter = "&f_"
    pre_addtional = "%2C"
    for f in f_type:
        if f == f_type[0]:
            out += f"{pre_filter}{f_type_dict.get('init_equal')}={f_type_dict.get(f)}"
        else:
            out += f"{pre_addtional}{f_type_dict.get(f)}"
    print(out)
    return out


filter_url = driver.current_url
filter_url += add_filter(experience, experience_dict)
filter_url += add_filter(work_type, work_type_dict)
filter_url += add_filter(job_type, job_type_dict)
print(filter_url)


driver.get(filter_url)


time.sleep(1000)
driver.quit()
