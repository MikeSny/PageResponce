from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from influxdb import InfluxDBClient

##driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver.get("http://www.google.com")
##driver.findElement(By.id("mib")).sendKeys(criteria);
#inputElement= driver.find_element_by_id("mib")
#inputElement.send_keys("test")
#inputElement.submit()

do = True
while do:
    sourcegoogle = "http://www.google.com"
    sourceduckduckgo = "http://www.duckduckgo.com"
    sourcebing = "http://www.bing.com"
    sourceonesearch = "http://www.onesearch.com"

# duckduckgo Measurement
    driver = webdriver.Firefox()
    driver.get(sourceduckduckgo)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_duckduckgo = responseStart - navigationStart
    frontendPerformance_duckduckgo = domComplete - responseStart

#print ("duckduckgo: Back End: %s" % backendPerformance)
#print ("duckduckgo: Front End: %s" % frontendPerformance)

# Google Measurement
    driver.quit()

    driver = webdriver.Firefox()
    driver.get(sourcegoogle)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_google = responseStart - navigationStart
    frontendPerformance_google = domComplete - responseStart

#print ("google: Back End: %s" % backendPerformance)
#print ("google: Front End: %s" % frontendPerformance)

    driver.quit()

# Bing Measurement
    driver = webdriver.Firefox()
    driver.get(sourcebing)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_bing = responseStart - navigationStart
    frontendPerformance_bing = domComplete - responseStart

#print ("bing: Back End: %s" % backendPerformance)
#print ("bing: Front End: %s" % frontendPerformance)

    driver.quit()

# Onesearch Measurement
    driver = webdriver.Firefox()
    driver.get(sourceonesearch)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")

    backendPerformance_onesearch = responseStart - navigationStart
    frontendPerformance_onesearch = domComplete - responseStart

#print ("onesearch: Back End: %s" % backendPerformance)
#print ("onesearch Front End: %s" % frontendPerformance)

    driver.quit()


# uploading data to influxDB
    responce_data = [
        {
            "measurement" : "websiteresponce",
            "tags":{ 
                "host": "RaspberryPi"
                },
                "fields" : {
                    "backendPerformance_duckduckgo": float(backendPerformance_duckduckgo),
                    "backendPerformance_google": float(backendPerformance_google),
                    "backendPerformance_bing": float(backendPerformance_bing),
                    "backendPerformance_onesearch": float(backendPerformance_onesearch),
                
                    "frontendPerformance_duckduckgo": float(frontendPerformance_duckduckgo),
                    "frontendPerformance_google": float(frontendPerformance_google),
                    "frontendPerformance_bing": float(frontendPerformance_bing),
                    "frontendPerformance_onesearch": float(frontendPerformance_onesearch)
                
                             
                
                
                
               
                    }
                }
                ]
    client = InfluxDBClient('localhost',8086,'websitemonitor','0Pel9321','websiteresponce')
    client.write_points(responce_data)

    



