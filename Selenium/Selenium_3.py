from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep 

chromedriver_autoinstaller.install() # bu kodu yazdığımızda chromedriver otomatikmen yükleniyor.

driver= webdriver.Chrome() # selenium bir web tarayıcısına ihtiyaç duyar. 
video_url="https://www.python.org/"
driver.get(video_url)

#1. işlem
print(f"Bulunduğunuz Sayfanın linki: {driver.current_url}") # sayfanın linkini verir.
print(f"Sayfa Başlığı: {driver.title}") # sayfanın başlığını veriyor.

#2. işlem
driver.maximize_window() # selenium o anki chrome tarayıcısı penceresini tam ekran yapar.
sleep(5)
driver.minimize_window()# selenium o anki chrome tarayıcısı penceresini simge durumunda küçültür. 
sleep(5)
driver.maximize_window() # selenium o anki chrome tarayıcısı penceresini tam ekran yapar.

#3. işlem
driver.get(video_url)
sleep(5)
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
sleep(5)
driver.back() # bir önceki sayfa.
sleep(5)
driver.forward() # bir sonraki sayfa.
sleep(5)
driver.refresh()# refresh atma tarayıcıyı yenileme.


# 4. işlem yeni sekme
driver.get(video_url)
sleep(5)
driver.execute_script("window.open('https://www.google.com', '_blank');") # yeni sekme açıp başka yere gitme js kodu.
driver.switch_to.window(driver.window_handles[-1]) # en son sekmeye geçiş.
sleep(5)
driver.close() # en son sekmeyi kapatır.


sleep(5)
driver.quit() # tarayıcıyı kapatma.