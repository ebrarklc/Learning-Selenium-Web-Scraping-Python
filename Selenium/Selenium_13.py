# Bot Tespiti ve korunma 
# selenium otomasyonunun bot olarak algılanmasının engellenmesi
# web sitelerinin IP adreslerini engellemesi 
# mesela amazonda bir bilgisayar için yaklaşık 117 sayfa var selenium çok hızlı olduğu için 117 sayfadaki verileri çok hızlı bir  
# çekiyor 
# bu yüzden biz kısa süre içerisinde verileri çekebilmek için siteye istekte bulunuyoruz
# normal bir insan dakikada 30 istek atıyorsa selenium belki de dakikada 100 istek atıyor 
# biz normalde işlemlerimizi tek bir IP adresi üzerinden yapıyoruz 
# PROXY kullanarak işlemleri birçok IP üzerinden yapabiliriz
# örneğin 100 istek 8 farklı IP adresi ile yapılacak
# bot olup olmadığınını anlamak ikinci yöntem insan davranışı
# sayfalar arası işlemler arası süre belirli bir saniye olunca hep aynı mesela siteler sizi bot olarak 
# mesela sayfalar arası geçişte genelde en altta olur ve site şöyle düşünür neden kaydırma çubuğu kullanmadı
# bazı stelerde ben robot değilimtarzında Captcha yapıları mevcut
# otomatik olarak captcha kullanımının önüne geçmek için bazı servisler bulunmakta
# bazı siteler headless mod kullanmamızdan dolayı da bizi engelliyor bu durumda headless moddan da kaçınmak gerekebilir
# basit verileri bot algılaması olmayan için chromedriver
# bot algılaması olan ileri seviye siteler için undetected_chromedriver


import random
from time import sleep
import undetected_chromedriver as uc # tespit edilmesi daha zor bir versiyonu 
# yapılan otomasyonların web siteleri tarafından tespit edilmesinin önüne geçmek için kullanılan ...
from time import sleep

print("1. sayfadan veriler çekiliyor...")
# sleep(3)
sleep(random.uniform(2,5)) # burası 2 ve 5 arasında rastgele bir sayı veriyor bu sayılar tam sayı değil küsüratlı sayılar
print("2. sayfadan veriler çekiliyor...")
sleep(random.uniform(2,5))
print("3. sayfadan veriler çekiliyor...")
sleep(random.uniform(2,5))



# Undetected Chromedriver başlatma
driver = uc.Chrome()
site_url = "https://google.com"
driver.get(site_url)
driver.maximize_window()

sleep(3)
driver.quit()


###   PROXY IP Adresleri
# 10.0.12.54
# 172.16.88.104
# 203.110.13.75
# 87.123.240.18
# 45.67.89.102
# 77.34.22.200
# 54.190.14.9
# 192.0.2.45