# selenium ile yapılan otomasyonları nasıl daha hızlı hale getirebileceğimizi göreceğiz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller # chromedriver bu kod ile otomatik yüklenecek

driver=webdriver.Chrome() # seleniumdan bir chrome tarayıcısı oluşturmasını sağladık.
# gitmek istediğimiz sitenin adresi
site_url="https://store.steampowered.com/charts/topselling/TR"
driver.get(site_url)
driver.maximize_window() # bunu yapma sebebimiz bazen responsiveden dolayı yerler değişiyor.
# sleep(5) # mesela süre önemli web sayfası açıldığında yüklenmeden kapanırsa verileri çekemeyiz buna dikkat et.

# amacımız hem zaman kaybımız olmasın hem de hata payını en aza indirelim WEBDRİVERWAİT

WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N")))
# bu kodda webdriver çağırıp driver ve 10 değerlerini girince seleniumdan 10 saniye beklemesini söylüyoruz 
# .until yani şu olana kadar 10 saniye bekle untilin içindeki
# yani şu elementler sayfada varsa ben burda 10 saniye bekle diyorum
# hangi elementler içine yazdığımız By.CLASS_NAME,"_1n_4-zvf0n4aqGEksbgW9N"

# aslında burda veri çekme işlemimiz çok hızlı oluyor böyle




# sayfada bulunan ilk 20 oyuna erişmek için
game_name=driver.find_elements(By.CLASS_NAME, "_1n_4-zvf0n4aqGEksbgW9N") # şu class ismine sahip tüm elemanları bul ELEMENTS(element olunca 1 tane elements olunca birden fazla).
for i in range(0,20):
    print(f"Oyun adı: {game_name[i].text}")

sleep(5)
driver.quit()
