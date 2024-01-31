import requests
from bs4 import BeautifulSoup

responce = requests.get('https://www.kinopoisk.ru/lists/movies/top250/')
print(responce.text)