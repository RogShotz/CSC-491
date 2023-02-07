# CSC-491: Senior Project at Cal Poly SLO

## Overview

### The need for a job bot

In my own world I have been steadily applying for jobs. The bad part about it however is I spend hours a day doing the same task over and over and I definately miss a lot of oppurtunities. If companies are already cycling through peoples resumes automatically, I figure that I should do the same for this project and apply automatically. This bot would be a very beneficial bot to use as it could apply, atleast as fast as me, throughout the day and save me dozens of hours of time.

### Objective

Create a bot that has the ability to find potential jobs and a bot to automatically fill out forms.

### Milestones

- Create bot to login with selenium
- Find jobs that match criteria
- Compile or otherwise notify user of the data
- Automatically apply and notify
- Structure into a UI
- Create user guide on use of the program

### Criterium for success
- Apply to 50 jobs
    - Fail rate < 90%
    - Improper job type < 90%
    - Accurate information submitted ~100%
    - Not rate limited / rate limit bypassed


## Requirements

### Physical:
There will be no required physical materials for this project. Eventually this project may include a web based app, which would require some server hosting.

### Non-Physical:
Python library requirements will be listed in the requirements doc.

### Other projects like mine
https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot
https://github.com/NathanDuma/LinkedIn-Easy-Apply-Bot

## Progress Reports

### 1/24/23
Finished writing senior project proposal. Started the base repository for the bot. Got selenium up and running. Created code to both login in by sending keys, or, and what I will be using, is authentication VIA cookie. This allows users to submit a Cookie rather than a username and password. It's less scary but probably still just as dangerous in terms of security.

## 1/7/23
Finished writing relevant filters like on site/ easy apply filter. Created a way to parse out a list of job ids and navigate to their web pages. At this point I need to continue to work on filling in job applications then review data before actually finishing this with actual application pushes. My advisor meeting noted that point, so hopefully by next test, job fill out will be complete and pseudo "applys" will start to be logged. This will satisify the criterium for success area.