# web sitelerinde tıklama işlemi 
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from time import sleep

# chromedriver bu kod ile otomatikmen yüklenecek
chromedriver_autoinstaller.install()

driver =webdriver.Chrome()
site_url="https://tr.wikipedia.org/wiki/Anasayfa"
driver.get(site_url)
driver.maximize_window() # açılan web sayfasını tam ekran yapıyor
sleep(5)

# bazı incele kısımlarında id,class ya da name olmayabilir peki nasıl erişeceğiz #xpath denilen bir şeyle 
#iki kere sağ tık incele copy copyxpath

#//*[@id="mp-itn"]/ul/li[1]/a[2] web elementinin tam yolunu gösteriyor

driver.find_element(By.XPATH, '//*[@id="mp-itn"]/ul/li[1]/a[2]').click() # tıklama
#xpath yolunu vererek seleniumdan xpath yolunu bulmasını istedik

# şimdi arama kısmına gidip yazı yazıp ara tuşuna basacak
search_box=driver.find_element(By.NAME, "search") # selenium name değeri search olan elementi bulacak 
search_box.send_keys("Kristof kolomb")
sleep(1)
driver.find_element(By.XPATH, '//*[@id="searchform"]/div/button').click()



sleep(5)
driver.quit() #tarayıcıyı kapatıyor