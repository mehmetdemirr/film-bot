from pydantic import BaseModel

class Film(BaseModel):
    ad:str
    # yabanci_ad:str
    yil:str
    imdb:str
    kategori:str
    link:str 
    photo:str

class Dizi(BaseModel):
    ad:str
    link:str 
    photo:str