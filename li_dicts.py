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