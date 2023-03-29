from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from dotenv import load_dotenv
import csv
import li_dicts as dicts

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

def element_exists(by, path):
    try:
        driver.find_element(by, path)
    except NoSuchElementException:
        return False
    return True


def easy_apply():
    apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "jobs-apply-button")]')))
    apply_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "phoneNumber")]'))).send_keys(os.getenv("PHONE"))

    if element_exists(By.XPATH, '//button[contains(@aria-label, "Submit application")]'):
        print("PSEUDO SUBMIT")


    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        "//button[contains(@aria-label, 'Continue to next step')]")))
    next_button.click()

    resume_name = driver.find_element(By.XPATH, '//h3[contains(@class, "jobs-document-upload")]').text
    
    if element_exists(By.XPATH, "//button[contains(@aria-label, 'Continue to next step')]"):
        "REQUIRES MULTIPLE STEPS"
    else:
        review_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        '//button[aria-label="Review your application"]')))
        review_button.click()

    follow_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='follow-company-checkbox']")))
    follow_button.click()

    submit_button =  wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '//button[contains(@aria-label, "Submit application")]')))
    print("PSEUDO SUBMIT")
    
    

    with open('log.csv', 'w') as csvfile:
        fields = ['job-id', 'contact', 'resume', 'other']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()
        csvwriter.writerow({'job_id': driver.current_url.split("/view/", 1)[1],
                    'email': str("NA"),
                    'phone-country-code': str("NA"),
                    'phone-numer': str(os.getenv("PHONE")),
                    'resume': str(resume_name),
                    'question_vars': str("f")})

def no_follow(self):
    follow_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, '//label[contains(.,"to stay up to date with their page.")]'))).send_keys(os.getenv("PHONE"))
    follow_checkbox.click()


def get_job(ID: str):
    driver.get(f'https://www.linkedin.com/jobs/view/{ID}')


if __name__ == "__main__":
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

    filter_url = driver.current_url
    filter_url += add_filter(dicts.experience, dicts.experience_dict)
    filter_url += add_filter(dicts.work_type, dicts.work_type_dict)
    filter_url += add_filter(dicts.job_type, dicts.job_type_dict)
    filter_url += add_filter(dicts.easy_apply, dicts.easy_apply_type_dict)
    print(filter_url)
    driver.get(filter_url)

    links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@data-job-id]')))
    IDs: list = []

    # children selector is the container of the job cards on the left
    for link in links:
        children = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//ul[@class="scaffold-layout__list-container"]')))

        for child in children:
            temp = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-job-id]')))
            temp = temp.get_attribute("data-job-id")
            jobID = temp.split(":")[-1]
            IDs.append(int(jobID))
    
    get_job(IDs[0])
    easy_apply()

    time.sleep(1000)
    driver.quit()