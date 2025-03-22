# ALert Penceresi Yönetimi 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()
#Chromedriver otomatik yükleme 


driver= webdriver.Chrome() # bir chrome tarayıcısı kullanacağımızı belirttik.

site_url="https://the-internet.herokuapp.com/javascript_alerts"
driver.get(site_url)
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()

# sleep yerine webdriverWait kullanacağız
WebDriverWait(driver,10).until(EC.alert_is_present()) # şu işlem yapılana kadar 10 saniye bekle işlem = sayfada bir alert penceresi olana kadar

site_Alert=Alert(driver) # site_alert üzerinden alert pencerelerine ulaşmış olacağım 
site_Alert.accept() # o anki alert penceresinde tamam butonuna tıklıyor


alert_result=driver.find_element(By.ID,"result")
print(alert_result.text)

sleep(3) 
driver.quit() # tarayıcı tüm işlemler sonucunda kapanması için.
