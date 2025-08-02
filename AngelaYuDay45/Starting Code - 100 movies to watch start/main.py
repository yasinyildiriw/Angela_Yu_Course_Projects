import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
reply = requests.get(url=URL)
data = reply.text
soup = BeautifulSoup(data, "html.parser")

films = soup.find_all(name="h3", class_="title")
film_list = [film.getText() for film in films]
# print(film_list)

reversed_film_list = list(reversed(film_list))
# print(reversed_film_list)

with open("movies.txt","w",encoding="utf-8") as file:
    for movie in reversed_film_list:
        file.write(f"{movie}\n")

