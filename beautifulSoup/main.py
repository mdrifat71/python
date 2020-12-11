from bs4 import BeautifulSoup
import requests


source = requests.get("https://www.prothomalo.com/search?q=%E0%A6%A7%E0%A6%B0%E0%A7%8D%E0%A6%B7%E0%A6%A3").text
soup = BeautifulSoup(source, 'lxml')
soup = soup.body

for news in soup.find_all("div", class_ = "customStoryCard9-m__base__1rOCp"):
    headline = news.find("h2", class_ = "headline").text
    date = news.time.text

    # print(headline)
    # print(date)
    # print(" ")

source = requests.get("http://images.prothomalo.com/prothomalo%2Fimport%2Fmedia%2F2020%2F01%2F12%2F41bc711d30cf11377694975e01246e73-5e1ac34f7fbaf.jpg?w=500&auto=format%2Ccompress&fmt=webp?")
f = open("tests.jpg", "wb")
f.write(source.content)