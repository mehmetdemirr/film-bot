from fastapi import FastAPI
from .filmm import get_filmler,get_film_url,sayfa_sayisi,get_diziler
from .schemas import Film
from typing import List
from urllib.parse import quote

app= FastAPI()

@app.get("/")
def index():
    return {"message":"starting"}

@app.get("/film_sayfa/{id}",response_model=List[Film])
def get_sayfa(id:int):
    filmler=get_filmler(id=id)
    # for f in filmler:
    #     print(f"Ad: {f.ad}")
    #     print(f"Yabancı Ad: {f.yabanci_ad}")
    #     print(f"Yıl: {f.yil}")
    #     print(f"IMDB: {f.imdb}")
    #     print(f"Kategori: {f.kategori}")
    #     print(f"Link: {f.link}")
    #     print(f"Photo: {f.photo}")
    #     print("\n")
    return filmler

@app.get("/film_link/{film_ad}")
def get_video(film_ad:str):
    new_link=f"https://www.fullhdfilmizlesene.pw/film/{film_ad}/"
    a=get_film_url(new_link)
    return a

@app.get("/son-sayfa")
def son_sayfa():
    son=sayfa_sayisi()
    return {"son":son}

@app.get("/diziler")
def get_dizi():
    dizis=get_diziler()
    return dizis



