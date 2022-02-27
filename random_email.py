from selenium import webdriver 
from selenium.webdriver.common.by import By

chrome_driver_path = './chromedriver.exe' 
options = webdriver.ChromeOptions() 
options.headless = True 
 
url = "https://theonegenerator.com/es/generadores/documentos/generador-de-email/" 

data = 3
 
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url) 

driver.set_page_load_timeout(150)

for a in range(data):

    element = driver.find_element(By.TAG_NAME, "form")
    element.submit()

    input = driver.find_element(By.ID, "copyToClipboard-email").get_attribute('value')

    print(input)

driver.quit()
