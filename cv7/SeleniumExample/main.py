#import selenium
#pip install -U selenium

from selenium import webdriver

chromeDriverPath = 'E:\School Stuff\SKJ\cv7\SeleniumExample\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chromeDriverPath)


#náš první skript
driver.get("https://www.seznam.cz")
#driver.close()
driver.quit()



"""
#interakce se search na seznam
driver.get("https://www.seznam.cz")

searchBar = driver.find_element_by_name("q")
print(searchBar)

placeholderValue = searchBar.get_attribute("placeholder")
print(placeholderValue)
driver.quit()
"""

"""
#vyhledávání pomocí xpath
#https://www.w3schools.com/xml/xpath_intro.asp
#https://devhints.io/xpath
driver.get("https://www.seznam.cz")

result = driver.find_elements_by_xpath("//li[contains(@class, 'search__tab')]")

for i in result:
    print(i)

result[3].click()

#driver.quit()

"""