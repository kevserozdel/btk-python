import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")
#list = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=1) gösterilecek tr etiketini 1 ile limitler.

# print(list)
count = 0
for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()") #strip silinmesi istediğimiz karakteri siler.
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    count += 1
    # print(title, year, rating)  #belirttiğimiz list içerisinde class'ı titlecolumn olan tdleri bulup içinden a'yı bulup text kısmını yazdırır.
                  #yani film adlarını liste şeklinde yazdırmış olduk.
    print(f"{count}- Film: {title.ljust(50)} Yıl: {year} Değerlendirme: {rating}")
