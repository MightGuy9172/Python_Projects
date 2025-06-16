import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
response.raise_for_status()
site_html=BeautifulSoup(response.text,'html.parser')
movies_list=site_html.select("h2 strong")
top100=[movie.getText() for movie in movies_list]
movies=top100[::-1]

with open("movies.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")





