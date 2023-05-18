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

start_time = time.time()

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
    app_time = str(time.time() - start_time)
    job_title = wait.until(EC.element_to_be_clickable((By.XPATH, '//h1[contains(@class, "job-title")]'))).text
    company = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="ember-view t-black t-normal"]'))).text
    #TODO: fix wait
    for i in range(0,2):
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "jobs-apply-button")]'))).click()
            break
        except EC.StaleElementReferenceException:
            print("Stale Reference in Easy Apply, Retrying")


    if element_exists(By.XPATH, '//button[contains(@aria-label, "Submit application")]'):
        unfollow()
        print("PSEUDO SUBMIT")
        write_log(company, job_title, get_job_id(), submit='t', app_time=app_time)
        return

    
    next_button = driver.find_element(By.XPATH,
                        "//button[contains(@aria-label, 'Continue to next step')]")
    while next_button:
        if not driver.find_elements(By.XPATH, '//span[@class="artdeco-inline-feedback__message"]'): # if not false, then indeed has told us we need more info
            next_button.click()
            review_button =  driver.find_elements(By.XPATH, '//span[contains(., "Review")]')
            if review_button:
                review_button[0].click()
                submit_button =  driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Submit application")]')
                if not submit_button: # if submit doesn't pop up
                    print("Unanswerable prompt in review, throwing")
                    write_log(company, job_title, get_job_id(), submit='f', app_time=app_time)
                    return
            submit_button =  driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Submit application")]')

            if submit_button:
                unfollow()
            
                write_log(company, job_title, get_job_id(), os.getenv("USERNAME"), 1, os.getenv("PHONE"), "testing", submit='t', app_time=app_time)
                print("PSEUDO SUBMIT")
                return
        else:
            print("Unanswerable prompt, throwing")

            write_log(company, job_title, get_job_id(), os.getenv("USERNAME"), 1, os.getenv("PHONE"), "testing", submit='t', app_time=app_time)
            return
        try: #got asked for more info on a review slide
            next_button = driver.find_element(By.XPATH,
                        "//button[contains(@aria-label, 'Continue to next step')]")
        except NoSuchElementException:
            print("Unanswerable prompt upon review click, throwing")
            write_log(company, job_title, get_job_id(), submit='f', app_time=app_time)
            return
            

    #include this for resume testing, testing prof does not work
    #resume_name = driver.find_element(By.XPATH, '//h3[contains(@class, "jobs-document-upload")]').text
    

def unfollow(): #unfollows employer before submitting
    follow_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='follow-company-checkbox']")))
    follow_button.click()

def get_job_id(): # gets job ID when at job application page
    return driver.current_url.split("/view/", 1)[1][:-1]

def write_log(company = "na", position = "na", job_id = "0", email = "na", phone_code = "0", phone_number = "0", resume = "na", question_vars = "na", submit = "f", app_time = "0"):
    with open('log.csv', 'a') as csvfile:
        fields = ['company', 'position', 'job-id', 'email', 'phone-country-code', 'phone-number', 'resume', 'question-vars', 'submitted', 'app-time']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writerow({
                    'company': str(company),
                    'position': str(position),
                    'job-id': str(job_id),
                    'email': str(email),
                    'phone-country-code': str(phone_code),
                    'phone-number': str(phone_number),
                    'resume': str(resume),
                    'question-vars': str(question_vars),
                    'submitted': str(submit),
                    'app-time': str(app_time)})


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

    wait = WebDriverWait(driver, 5)  # var for waiting consistently
    with open('log.csv', 'w') as csvfile:
        fields = ['company', 'position', 'job-id', 'email', 'phone-country-code', 'phone-number', 'resume', 'question-vars', 'submitted', 'app-time']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)
        csvwriter.writeheader()

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

    links = driver.find_elements("xpath",'//li[@data-occludable-job-id]') #//div[@data-job-id]'
    job_ids = []#[3257102022, 3541992515] #1 page, error out

    # children selector is the container of the job cards on the left
    for link in links:
        job_ids.append(int(link.get_attribute('data-occludable-job-id')))
    
    #print(job_ids)
    for id in job_ids:
        print("applying for", id)
        get_job(id)
        easy_apply()

    print("finish")
    time.sleep(1000)
    driver.quit()