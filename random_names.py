from selenium import webdriver 
from selenium.webdriver.common.by import By 

chrome_driver_path = './chromedriver.exe' 
options = webdriver.ChromeOptions() 
options.headless = True 
 
url = "https://generadordenombres.online/" 

data = 3
 
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url) 

for a in range(data):
    
    input = driver.find_element(By.ID, "resultadoGenerado").text
    driver.execute_script("location.reload()")

    print(input)

driver.quit()
