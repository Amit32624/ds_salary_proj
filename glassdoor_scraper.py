#
# Created on Mon Jan 11 2021 by Amit Sambrekar
#
#
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import  StaleElementReferenceException



def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    # url ="https://www.glassdoor.com/Job/jobs.htm?sc.occupationParam="+keyword+"&sc.locationSeoString=Ireland&locId=70&locT=N&clickSource=searchBox"

    driver.get(url)
    jobs = []
    try:
        time.sleep(5)
        driver.find_element_by_xpath('.//*[@id="onetrust-accept-btn-handler"]').click()
        time.sleep(5)
    except ElementClickInterceptedException:
        pass

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.


        # Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element_by_class_name("react-job-listing").click()
            print("In")
        except ElementClickInterceptedException:
            pass

        time.sleep(5) 

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
        except NoSuchElementException:
            pass

        
        #Going through each job in this page
        time.sleep(5)
        job_buttons =driver.find_elements_by_class_name("react-job-listing") #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break
            try:
                job_button.click()
            except NoSuchElementException:
                pass
            
            except StaleElementReferenceException as e:
                print(e)
                pass  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    
                    company_name = driver.find_element_by_xpath('.//div[@class="css-xuk5ye e1tk4kwz5"]').text
                    location = driver.find_element_by_xpath('.//div[@class="css-56kyx5 e1tk4kwz1"]').text
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "css-1j389vi e1tk4kwz2")]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(1)

            try:
                salary_estimate = driver.find_element_by_xpath('.//span[@class="css-1hbqxax e1wijj240"]').text
            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                rating = driver.find_element_by_xpath('.//span[@class="css-1m5m32b e1tk4kwz4"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            try:
                next =driver.find_element_by_xpath('.//div[@data-item="tab" and @data-tab-type="overview"]')
                driver.execute_script("arguments[0].click();", next)

                try:
                    size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
                except StaleElementReferenceException as E:
                    print(E)
                    pass
                except NoSuchElementException:
                    size = -1

                try:
                    
                    founded = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
                except StaleElementReferenceException as E:
                    print(E)
                    pass
                except NoSuchElementException:
                    founded = -1


                try:
                    industry = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
                except StaleElementReferenceException as E:
                    print(E)
                    pass
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
                except StaleElementReferenceException as E:
                    print(E)
                    pass
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
                except StaleElementReferenceException as E:
                    print(E)
                    pass
                except NoSuchElementException:
                    revenue = -1

            except StaleElementReferenceException as E:
                print(E)
                pass
            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                size = -1
                founded = -1
                industry = -1
                sector = -1

                
            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue})
            #add job to jobs
            
            
        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//*[@id="FooterPageNav"]/div/ul/li[7]/a').click()
            # //*[@id="FooterPageNav"]/div/ul/li[7]
            
            
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.