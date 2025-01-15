from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get('https://demo.automationtesting.in/Index.html')
driver.maximize_window()

email_text = driver.find_element(By.ID,'email')
email_text.send_keys('test@gmail.com')
driver.find_element(By.ID, 'enterimg').click()

#Select class declaration with webelement
select_web = driver.find_element(By.ID,'Skills')
sel = Select(select_web)

#select by index
#sel.select_by_index(5)

#select by value
#sel.select_by_value('Client Support')

#select by visible text
sel.select_by_visible_text('Certifications')

#navigate different url
driver.get("https://www.google.com/")
print(driver.current_url)

#back
driver.back()
print(driver.current_url)

#refresh
driver.refresh()

#farword
driver.forward()

#quit
driver.quit()