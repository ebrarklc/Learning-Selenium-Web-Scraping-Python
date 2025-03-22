# selenium ile uygulama yapacağız öncelikle google a git arama butonunu bul yazdığım şeyleri oraya ekleyip 
# # entera bas

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install() # chromedriver otomatikmen yüklenecek.

driver=webdriver.Chrome() # seleniumdan bir chrome tarayıcısı oluşturmasını sağladık.
site_url="https://www.google.com.tr/"
driver.get(site_url)
driver.maximize_window() # bunu yapma sebebimiz bazen responsiveden dolayı yerler değişiyor.
sleep(1)

# 2. adım
search_box=driver.find_element(By.NAME, "q") # sayfadaki name değerleri arasında bu değeri bulup referans olarak search_box değişkenine aktaracak.

# 3. adım 
search_box.send_keys("Selenium") # yazmak istediğimiz Selenium değerini arama çubuğuna gönderecek.
sleep(1)

# 4. adım enter tuşuna basıp arama yapması
# search_box.send_keys("\ue007") # enterin klavyede özel değeri.
search_box.send_keys(Keys.ENTER)
sleep(3)

driver.quit() # tarayıcıyı kapat.
