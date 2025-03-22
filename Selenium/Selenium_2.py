from selenium import webdriver 

# Selenium WebDriver'ı projeye dahil eder.
# WebDriver, tarayıcıları kontrol etmek için kullanılır (Chrome, Firefox, Edge vs.).
# Örneğin, bir web sayfasını açmak, butona tıklamak veya form doldurmak için kullanılır.

import chromedriver_autoinstaller

# Chromedriver'ı otomatik olarak yükler ve çalıştırır.
# Chromedriver, Selenium’un Chrome tarayıcısını kontrol edebilmesi için gerekli olan bir araçtır.

from time import sleep

# Kodun belirli bir süre beklemesini sağlar.
# Web sayfalarının yüklenmesini beklemek veya belirli bir süre duraksamak için kullanılır.

chromedriver_autoinstaller.install() # bu kod bizim yerimize uygun olan chromedriverı otomatik olarak yüklüyor.

driver= webdriver.Chrome() # bir chrome tarayıcısı kullanacağımızı belirttik.

video_url="https://tr.wikipedia.org/"

driver.get(video_url)

print(driver.title) # sitedeki başlık bilgisi consolda göründü.

sleep(3) # adrese gidip anında kapanmıştı şimdi adrese gidip 3 saniye bekleyip öyle kapatacak.
driver.quit() # tarayıcı tüm işlemler sonucunda kapanması için.
