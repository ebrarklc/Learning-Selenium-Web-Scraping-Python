# File Upload (Dosya yükleme işlemi)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from time import sleep

# Chromedriver otomatik yükleme
chromedriver_autoinstaller.install()

# Chrome tarayıcısını başlat
driver = webdriver.Chrome()

# Siteyi aç ve pencereyi büyüt
site_url = "https://the-internet.herokuapp.com/upload"
driver.get(site_url)
driver.maximize_window()

# Dosya yükleme alanının sayfada görünmesini bekle
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "file-upload")))

# Dosya seçme butonunu bul
file_upload = driver.find_element(By.ID, "file-upload")

# Dosya yolu
file_path = r"C:\Users\yakup\Desktop\Ebrar.pdf"  # veya "C:/Users/yakup/Desktop/Ebrar.pdf"

# Dosya seçme butonuna dosya yolunu gönder
file_upload.send_keys(file_path)

#upload butonuna tıklama 
driver.find_element(By.ID,"file-submit").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div/h3' )))

result=driver.find_element(By.XPATH,'//*[@id="content"]/div/h3')
print(result.text)

# 7 saniye bekle ve tarayıcıyı kapat
sleep(7)
driver.quit()
