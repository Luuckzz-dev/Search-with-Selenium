from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
# Configuration directory download
download_directory = r'C:\Users\pasta' 
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
# Configuration Selenium
selenium_service = Service(r'C:\Users\Desktop\chromedriver-win64\chromedriver.exe')  
driver = webdriver.Chrome(service=selenium_service, options=chrome_options)
# URL site
url = "https://www.google.com.br"
driver.get(url)
# find login with xpath
login_field = driver.find_element(By.XPATH, '//*[@id="txtUsu"]') #xpath alterar
time.sleep(1)
login_field.send_keys('User')
# find password with xpath
password_field = driver.find_element(By.XPATH, '//*[@id="txtSen"]') #xpath alterar
time.sleep(1)
password_field.send_keys('SenhaEnviada')
# click button login
login_button = driver.find_element(By.XPATH, '//*[@id="btnLogin"]') #xpath alterar
time.sleep(1)
login_button.click()
time.sleep(2)
findelementdw = driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_gvwMenusB_hplMenu_0']")
findelementdw.click()
time.sleep(1)
downloaditem = driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_btnExportarGeral']")
downloaditem.click() 
time.sleep(120)
#driver.quit()
