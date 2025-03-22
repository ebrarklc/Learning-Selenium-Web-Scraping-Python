# selenium ile web sitesinden veri çekme

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install() # chromedriver otomatikmen yüklenecek.

driver=webdriver.Chrome() # seleniumdan bir chrome tarayıcısı oluşturmasını sağladık.
# gitmek istediğimiz sitenin adresi
site_url="https://store.steampowered.com/charts/topselling/TR"
driver.get(site_url)
driver.maximize_window() # bunu yapma sebebimiz bazen responsiveden dolayı yerler değişiyor.
sleep(5) # mesela süre önemli web sayfası açıldığında yüklenmeden kapanırsa verileri çekemeyiz buna dikkat et.

game_name=driver.find_element(By.CLASS_NAME, "_1n_4-zvf0n4aqGEksbgW9N").text # bu etiket içerisindeki text metinleri verir.
print(f"Oyun Adı: {game_name}")
sleep(5)

# sayfada bulunan ilk 20 oyuna erişmek için
game_name=driver.find_elements(By.CLASS_NAME, "_1n_4-zvf0n4aqGEksbgW9N") # şu class ismine sahip tüm elemanları bul ELEMENTS(element olunca 1 tane elements olunca birden fazla).
for i in range(0,20):
    print(f"Oyun adı: {game_name[i].text}")

sleep(5)

driver.quit() # tarayıcıyı kapat.
