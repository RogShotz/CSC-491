from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

# applied filters
date_posted = 0
experience = ["internship", "entry_level"]
company = 0
job_type = ["full-time", "contract"]
work_type = ["remote", "hybrid"]
easy_apply = False


load_dotenv()
options = Options()
# options.add_argument('--headless')
options.add_argument("--no-sandbox")

# Dev Shared Memory, disable for better perf.
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.linkedin.com/jobs/search/")
driver.add_cookie({"name": "li_at", "value": os.getenv("COOKIE")})
driver.refresh()


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
