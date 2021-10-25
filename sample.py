from selenium import webdriver
path = "F:/my_projects/ds_salary_prj/ds_salary_proj/chromedriver"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=path, options=options)
driver.set_window_size(1120, 1000)
url ='https://github.com/Amit32624'
driver.get(url)
#Refreshes the web page
for i in range(100):
    driver.refresh()