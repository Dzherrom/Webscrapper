from selenium import webdriver

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path =  '/Users/jerox/OneDrive/Documentos/chromedriver'

driver = webdriver.Chrome(path)
driver.get(website)

