# Data Science Salary Estimator: Project Overview
* Created a tool that estimates data science salaries (MAE ~ $ 11K) to help data scientists negotiate their income when they get a job.
* Scraped over 1200 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used

Python Version: 3.8
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
- For Web Framework Requirements: pip install -r requirements.txt
- Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
- Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
- Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping

Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Size
* Company Founded Date
* Industry
* Sector
* Revenue

## Data Cleaning

After scraping the data, I needed to clean it up so that it was usable for model. I made the following changes and created the following variables:

* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary
* Parsed rating out of company text
* Made a new column for company state
* Added a column for if the job was at the company’s headquarters
* Made columns for if different skills were listed in the job description:
  * Python
  * R
  * Excel
  * AWS
  * Spark
* Column for simplified job title and Seniority
* Column for description length

## Exploratory data analysis
- I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

- Job opporutinities according to the location

![job_location](https://user-images.githubusercontent.com/57942586/138706634-2b6b4069-46a9-4ad3-9f10-e978fd0b1e04.png)

- Average salary
![avg_salary](https://user-images.githubusercontent.com/57942586/138706626-1db269a1-e89e-43f2-9ced-d4ca1b7dc3dc.png)
![heat_map](https://user-images.githubusercontent.com/57942586/138706645-f20cda72-c81e-4173-8fd9-ec346697a048.png)


# Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

### I tried three different models:

* Multiple Linear Regression – Baseline for the model
* Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
* Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit.

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
Random Forest : MAE = 13.80
Ridge Regression: MAE = 16.11

## Productionization
In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
Contributions, issues, and feature requests are welcome!

Give a ⭐️ if you like this project!
