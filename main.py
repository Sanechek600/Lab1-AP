from bs4 import BeautifulSoup
import requests
import os
import re


URL = "https://www.livelib.ru/reviews/~1#reviews"
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"}).text
soup = BeautifulSoup(html_page, features="html.parser")

t_card = soup.find("article", class_="review-card lenta__item")

rating = t_card.find("span", class_="lenta-card__mymark").text
rating = re.search(r"\d", rating).group(0)

with open("t_save.txt", "w") as f:
    f.write(rating)
