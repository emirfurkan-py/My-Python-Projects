# Bu projede amacımız aradığımız kitabın fiyatlarını karşılaştırmak.

import time
from selenium import webdriver
from selenium. webdriver. common. keys import Keys
from bs4 import BeautifulSoup

#chrome driverını etkinleştirme
chrome_driver_path="C:\driverselenium\chromedriver"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

#kullanıcıdan kitap bilgilerini alma
kitap_adi= input("Kitap adini giriniz : ")
yayin_evi=input("Yayinevini giriniz :")

driver.get("https://www.google.com.")

def bkmkitap():

    #arama motoruna kitap ismini yazma ve onaylama
    bkm_kitap_veri_girisi=driver.find_element_by_css_selector(".gLFyf.gsfi")
    bkm_kitap_veri_girisi.send_keys(kitap_adi+" "+yayin_evi+" "+" site:bkmkitap.com")
    time.sleep(2)
    bkm_kitap_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)
    giris=driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/a/h3")
    giris.click()
     
    #kitap bilgilerini bs4 ile alma
    bkm_kitap_sayfa=driver.page_source
    bkm_kitap_soup=BeautifulSoup(bkm_kitap_sayfa,"lxml")
    bkm_kitap_bilgiler=bkm_kitap_soup.find("div",attrs={"id":"productInfo"})
    #kitap bilgilerini etiketlerinden alma
    bkm_kitap_adi=bkm_kitap_bilgiler.find("h1").text
    bkm_kitap_yayin_evi=bkm_kitap_bilgiler.find("a").text.strip()
    bkm_kitap_yazar=bkm_kitap_bilgiler.find("a",attrs={"id":"productModelText"}).text.strip()
    bkm_kitap_fiyat=bkm_kitap_soup.find("span",attrs={"class":"product-price"}).text

    #kitap bilgilerini ekrana yazdırma
    print("BKM KİTAP = "+ bkm_kitap_adi+" , "+ bkm_kitap_yayin_evi+" , "+ bkm_kitap_yazar+" , "+bkm_kitap_fiyat+"TL")

def kitapyurdu():
    driver.get("https://www.google.com/")
    
    #arama motoruna kitap ismini yazma ve onaylama
    kitapyurdu_veri_girisi = driver.find_element_by_css_selector(".gLFyf.gsfi")
    kitapyurdu_veri_girisi.send_keys(kitap_adi+ " "+ yayin_evi+ " "+" site:kitapyurdu.com")
    kitapyurdu_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    #kitap linkine tıklama
    kitapyurdu_tikla = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div[1]/a/h3")
    kitapyurdu_tikla.click()

    #kitap bilgilerini bs4 ile alma
    kitapyurdu_sayfa = driver.page_source
    kitapyurdu_soup = BeautifulSoup(kitapyurdu_sayfa, "lxml")

    #kitap bilgilerini etiketlerinden alma
    kitapyurdu_kitap_adi = kitapyurdu_soup.find("h1",attrs={"class":"pr_header__heading"}).text 
    kitapyurdu_yazar_adi = kitapyurdu_soup.find("a",attrs={"class":"pr_producers__link"}).text.strip()
    kitapyurdu_yayin_evi = kitapyurdu_soup.find("div",attrs={"class":"pr_producers__publisher"}).text.strip()
    kitapyurdu_fiyat = kitapyurdu_soup.find("div",attrs={"class":"price__item"}).text.strip()
    
    #kitap bilgilerini ekrana yazdırma
    print("KİTAP YURDU = "+ kitapyurdu_kitap_adi+" , "+kitapyurdu_yazar_adi+" , "+kitapyurdu_yayin_evi+" , "+kitapyurdu_fiyat+"TL")   

bkmkitap()
kitapyurdu()    