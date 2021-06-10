from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chromeDriverPath = "E:\School Stuff\SKJ\cv7\SeleniumExample\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriverPath)

driver.get("https://orteil.dashnet.org/cookieclicker/")


cookie = driver.find_element_by_id("bigCookie")

action = ActionChains(driver)
action.click(cookie)

#Infinite cycle
for _ in iter(int, 1):
    #10x click on cookie - seems faster
    for i in range(10):
        action.perform()
    #Try to find upgrade, if its enabled to upgrade it upgrades it, Checking from last to first
    try:                
        items = driver.find_elements_by_class_name("enabled")
        for item in items[::-1]:            
            item.click()
    except:
        pass
    
    

    