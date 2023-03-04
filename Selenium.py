from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By as by 
from selenium.webdriver.support.select import Select
import pandas as pd 

'''
Selenium webscrapper can't be bound into venv since
the webdriver is linked to browser and to do so 
you should also include the browser itself in venv
'''

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
driver = Chrome(executable_path='C:/WebDrivers/chromedriver.exe')
driver.get(website)

'''
Structure for relative Xpath search
'//Tag[@atribute="plain text"]'
'''
all_matches = driver.find_element(by.CSS_SELECTOR, "#page-wrapper > div > home-away-selector > div > div > div > div > label:nth-child(2)")
all_matches.click()
dropdown = Select(driver.find_element(by.XPATH, '//*[@id="country"]')).select_by_index(3)
matches = driver.find_elements(by.TAG_NAME, 'tr')
partidos = []

for match in matches:
    partidos.append(match.text)

print(partidos)
driver.quit()

# Pandas
df = pd.DataFrame({'partidos':partidos})
print(df)
df.to_csv('partidos.csv', index=False)
    
