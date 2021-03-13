from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

##driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.get("http://www.google.com")
##driver.findElement(By.id("mib")).sendKeys(criteria);
#inputElement= driver.find_element_by_id("mib")
#inputElement.send_keys("test")
#inputElement.submit()



source = "http://www.google.com/"
driver = webdriver.Firefox()
driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("Back End: %s" % backendPerformance)
print ("Front End: %s" % frontendPerformance)

driver.quit()