# sayfa kaydırma scroll işlemleri 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep

chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
site_url="https://store.steampowered.com/charts/mostplayed"
driver.get(site_url)
driver.maximize_window()
sleep(3)

driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
# burda bir js kodu yazdık excute_script demek js kodu yazacağız anlamına geliyor 
#içindeki yapı ise 0 dan sayfa sonuna kadar kaydır demek 
sleep(3)

driver.execute_script("window.scrollTo(document.documentElement.scrollHeight,0);")
# tam tersi bu sefer de en alttan en üste kaydırma

# şimdi de 0 dan 40. oyuna kadar kaydıralım 
element=driver.find_element(By.XPATH, '//*[@id="page_root"]/div[3]/div/div/div/div[3]/table/tbody/tr[40]/td[1]/div/div')
driver.execute_script("arguments[0].scrollToView();", element)

# şimdi de 0 dan 800px e kadar kaydıralım 
driver.execute_script("window.scrollBy(0,800)")

# javascript kodu kullanmadan sayfayı kaydırma 
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END) # aşağı doğru
sleep(3)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME) # yukarı doğru

sleep(3)
driver.quit()