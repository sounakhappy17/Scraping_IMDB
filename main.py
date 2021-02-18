import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd



url = "https://www.imdb.com/chart/top/"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")


movie_list = []

table = soup.find('tbody', class_='lister-list')
rows = table.find_all('tr')
for row in rows:
    movies = row.find('td', class_='titleColumn')
    movie_name = movies.find('a').text.strip()
    rating = row.find('td', class_='ratingColumn imdbRating').text.strip()
    # print(movie_name, rating)
    imdb = {
        'movie':movie_name,
        'rating':rating
    }
    movie_list.append(imdb)


df = pd.DataFrame(movie_list)
print(df.head())