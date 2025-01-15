from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get('https://demo.automationtesting.in/Index.html')

email_text = driver.find_element(By.ID,'email')
email_text.send_keys('test@gmail.com')
driver.find_element(By.ID, 'enterimg').click()
#Radio button
driver.find_element(By.XPATH, '//input[@value="FeMale"]').click()
#Checkbox and get attribute
li = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')

for ele in li:
    val = ele.get_attribute('value')
    if val == "Hockey":
        ele.click()