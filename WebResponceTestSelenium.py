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



sourcegoogle = "http://www.google.com/"
sourceduckduckgo = "http://www.duckduckgo.com"
sourcebing = "http://www.bing.com"
sourceswisscows= "http://onesearch.com"

#duckduckgo Measurement
driver = webdriver.Firefox()
driver.get(sourceduckduckgo)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("duckduckgo: Back End: %s" % backendPerformance)
print ("duckduckgo: Front End: %s" % frontendPerformance)

# Google Measurement
driver.quit()

driver = webdriver.Firefox()
driver.get(sourcegoogle)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("google: Back End: %s" % backendPerformance)
print ("google: Front End: %s" % frontendPerformance)

driver.quit()

driver = webdriver.Firefox()
driver.get(sourcebing)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("sourcebing: Back End: %s" % backendPerformance)
print ("sourcebing: Front End: %s" % frontendPerformance)

driver.quit()

driver = webdriver.Firefox()
driver.get(sourcebing)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("sourceswisscows: Back End: %s" % backendPerformance)
print ("sourceswisscows Front End: %s" % frontendPerformance)

driver.quit()

