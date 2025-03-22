# Ekran Görüntüsü Alma Genelde test otomasyonlarında görünüyor

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from time import sleep

# Chromedriver otomatik yükleme
chromedriver_autoinstaller.install()

# Chrome tarayıcısını başlat
driver = webdriver.Chrome()

# Siteyi aç ve pencereyi büyüt
site_url = "https://store.steampowered.com/"
driver.get(site_url)
driver.maximize_window()
sleep(3)

driver.save_screenshot("images.png") # alınan ekran görüntüsünün ismi images.png

# tüm sayfanın değilde belirli bir kısmın ekran görüntüsünü almak istiyorum 
element=driver.find_element(By.CLASS_NAME,"home_special_offers_group")
element.screenshot("images.png")


driver.quit()
