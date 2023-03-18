import requests
from bs4 import BeautifulSoup

url = "https://www.codewithhtomi.ml/"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.content, "lxml")
title = soup.find_all('h2', {'class': 'post-title'})
print(title)
