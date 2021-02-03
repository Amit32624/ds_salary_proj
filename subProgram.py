#
# Created on Tue Jan 19 2021 by Amit Sambrekar
#
#
import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/91720/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1500, False, path, 20)
df.to_csv('glassdoor_jobs.csv', index = False)