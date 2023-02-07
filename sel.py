from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

# dataum for filters and corresponding values
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
industry_type_dict = {"init_equal": "I", "software_development": 4}
easy_apply_type_dict = {"init_equal": "AL",
                        "true": "true"}  # TODO: Fix this it's weird

# filter components
date_posted = 0
experience = ["internship", "entry_level"]
company = 0
job_type = ["full-time", "contract"]
work_type = ["remote", "hybrid"]
easy_apply = ["true"]
# replaced by direct job type searching, which replaces /search
# industry_type = ["software_development"]

load_dotenv()
options = Options()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")

# Dev Shared Memory, disable for better perf.
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome("./chromedriver")

wait = WebDriverWait(driver, 20)  # var for waiting consistently

# TODO: figure out how direct job searches work
# add position so you don't have to reload
driver.get(
    "https://www.linkedin.com/jobs/software-developer-jobs/?position=1&pageNum=0")
driver.add_cookie({"name": "li_at", "value": os.getenv("COOKIE")})
time.sleep(20)

def wait_load(xpath: str):
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))


def add_filter(f_type: str, f_type_dict: dict):
    out = ""
    pre_filter = "&f_"
    pre_addtional = "%2C"
    for f in f_type:
        if f == f_type[0]:
            out += f"{pre_filter}{f_type_dict.get('init_equal')}={f_type_dict.get(f)}"
        else:
            out += f"{pre_addtional}{f_type_dict.get(f)}"
    return out


filter_url = driver.current_url
filter_url += add_filter(experience, experience_dict)
filter_url += add_filter(work_type, work_type_dict)
filter_url += add_filter(job_type, job_type_dict)
filter_url += add_filter(easy_apply, easy_apply_type_dict)


def easy_apply():
    wait_load('//button[contains(@class, "jobs-apply-button")]')
    apply_button = driver.find_elements("xpath",
                                        '//button[contains(@class, "jobs-apply-button")]'
                                        )
    apply_button[0].click()

print(filter_url)
driver.get(filter_url)

time.sleep(20)
wait_load('//ul[@class="scaffold-layout__list-container"]')
links = driver.find_elements("xpath",
                             '//div[@data-job-id]'
                             )
IDs: list = []

# children selector is the container of the job cards on the left
for link in links:
    wait_load('//*[@id="main"]/div/section[1]/div/ul')
    children = link.find_elements("xpath",
                                  '//ul[@class="scaffold-layout__list-container"]')

    for child in children:
        temp = link.get_attribute("data-job-id")
        jobID = temp.split(":")[-1]
        IDs.append(int(jobID))


def get_job(ID: str):
    driver.get(f'https://www.linkedin.com/jobs/view/{ID}')
    time.sleep(20)


get_job(IDs[0])
easy_apply()


time.sleep(1000)
driver.quit()
