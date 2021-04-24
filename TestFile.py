from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from influxdb import InfluxDBClient


responce_data = [
    {
        "measurement" : "websiteresponce",
        "tags":{ 
            "host": "RaspberryPi"
            },
            "fields" : {
                "backendPerformance_duckduckgo": float(2002),
                "backendPerformance_google": float(3000),
                "backendPerformance_bing": float(4000),
                "backendPerformance_onesearch": float(5000),
                
#                "frontendPerformance_duckduckgo": float(frontendPerformance_duckduckgo),
#                "frontendPerformance_google": float(frontendPerformance_google),
#                "frontendPerformance_bing": float(frontendPerformance_bing),
#                "frontendPerformance_onesearch": float(frontendPerformance_onesearch)
                
                             
                
                
                
               
                }
            }
            ]
client = InfluxDBClient('localhost',8086,'websitemonitor','0Pel9321','websiteresponce')
client.write_points(responce_data)