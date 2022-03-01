from selenium import webdriver 
from selenium.webdriver.common.by import By

import random, time

chrome_driver_path = './chromedriver.exe' 
options = webdriver.ChromeOptions() 
options.headless = True 
 
url = "https://www.saucedemo.com/" 
 
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url) 
driver.set_page_load_timeout(150)

usernames = driver.find_element(By.ID, "login_credentials").text
usernames_list = usernames.split("\n")  ## Get the results as a list
del usernames_list[0]           ## Deletes the first element of the list
rand_username = random.choice(usernames_list)      ## Gets a random username from the list


passwords = driver.find_element(By.CLASS_NAME, "login_password").text
passwords_list = passwords.split("\n")  ## Get the results as a list
del passwords_list[0]           ## Deletes the first element of the list
rand_password = random.choice(passwords_list)      ## Gets a random username from the list

print(f"Username: {rand_username}")
print(f"Password: {rand_password}")

driver.find_element(By.ID, "user-name").send_keys(rand_username)        ## Types the username
driver.find_element(By.ID, "password").send_keys(rand_password)         ## Types the password

driver.find_element(By.ID, "login-button").click()      ## Clicks the login button

time.sleep(2) ## Waits 2 seconds, just to see the automatic Login

driver.quit()
