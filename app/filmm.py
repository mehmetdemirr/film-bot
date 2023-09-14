from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

from app.schemas import Film,Dizi

options = webdriver.FirefoxOptions()
options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştır
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Firefox(options=options)


def get_film_url(link:str):
    driver.get(link)
    time.sleep(1)
    src=driver.find_element(By.XPATH,'//*[@id="plx"]/iframe').get_attribute("src")
    driver.quit()
    return src

def get_filmler(id:int):
    url=f"https://www.fullhdfilmizlesene.pw/yeni-filmler-izle-2/{id}"
    driver.get(url)
    time.sleep(1)
    filmler= driver.find_elements(By.XPATH,'/html/body/div[5]/div[1]/main/section/ul/li')
    film_list = []  # Film bilgilerini tutmak için boş bir liste
    for film in filmler:
        try:
            href = film.find_element(By.CLASS_NAME, "tt").get_attribute("href")
        except Exception:
            href = ""

        try:
            title = film.find_element(By.CLASS_NAME, "film-title").text
        except Exception:
            title = ""

        try:
            yil = film.find_element(By.CLASS_NAME, "film-yil").text
        except Exception:
            yil = ""

        try:
            photo = film.find_element(By.CLASS_NAME, "afis").get_attribute("data-src")
        except Exception:
            photo = ""

        try:
            imdb = film.find_element(By.CSS_SELECTOR, ".imdb").text
        except Exception:
            imdb = ""

        try:
            kategori = film.find_element(By.CSS_SELECTOR, ".trz.trz").text
        except Exception:
            kategori = ""

        film_model = Film(ad=title, yil=yil, imdb=imdb, kategori=kategori, link=href or "", photo=photo or "")
        film_list.append(film_model)
    driver.quit()
        
    return film_list  # Film listesini döndürün

def sayfa_sayisi():
    driver.get("https://www.fullhdfilmizlesene.pw/yeni-filmler-izle-2/1")
    time.sleep(1)
    sayfalama= driver.find_elements(By.XPATH,'/html/body/div[5]/div[1]/main/div/a')
    driver.quit()
    return sayfalama[len(sayfalama)-2].text

def get_diziler():
    driver.get("https://yabancidizi.pro/dizi-izle")
    time.sleep(3)
    diziler=driver.find_elements(By.CLASS_NAME,"segment-poster-sm")
    # i=0
    dizi_list = []  # Dizi bilgilerini tutmak için boş bir liste
    for dizi in diziler:
        link=dizi.find_element(By.XPATH,'./div[@class="poster poster-xs"]/a').get_attribute("href") or ""
        photo=dizi.find_element(By.XPATH,'./div[@class="poster poster-xs"]/a/div/img').get_attribute("data-src") or ""
        ad=dizi.find_element(By.XPATH,'./div[@class="poster poster-xs"]/a/div/h2[@class="truncate"]').text or ""
        # i=i+1
        # print(f"{i}- {ad}- {link}- {photo}")
        dizi_model = Dizi(ad=ad,link=link, photo="https://yabancidizi.pro/"+photo)
        dizi_list.append(dizi_model)
    driver.quit()
    return dizi_list

