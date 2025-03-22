# Headless Mod Nedir
# bir tarayıcıyı nasıl görünmez biçimde çalışacağımızı 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from time import sleep

# Chromedriver otomatik yükleme
chromedriver_autoinstaller.install()

Options=Options()
Options.add_argument("--headless") # arka planda işlemler yapılıyor ancak tarayıcı penceresi açılmıyor 

# headless mode artıları sistem kaynakları , işlemciler daha az kullanılıyor bu sayede daha üst seviye bir performans elde 
#çok çok uzun sayfalar için performans ve kaynak kullanımı açısından önemli

# Chrome tarayıcısını başlat
driver = webdriver.Chrome(options=Options)

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

