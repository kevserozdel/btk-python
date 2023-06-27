import requests
from bs4 import BeautifulSoup

url = "https://www.trendyol.com/cep-telefonu-x-c103498"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

phones = soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("div",{"class":"p-card-wrppr with-campaign-view"})
#class'ı belirtilen ifade olan tüm divlerin içinden divleri bulur.
# print(liste)

for phone in phones:
    
    marka = phone.find("div",{"class":"prdct-desc-cntnr-ttl-w two-line-text"}).find_all("span")[0].text #span'in divini belirtmek gerekli.
    model = phone.find("div",{"class":"prdct-desc-cntnr-ttl-w two-line-text"}).find_all("span")[1].text
    fiyat = phone.find("div",{"class":"price-promotion-container"}).find("div",{"class":"prc-box-dscntd"}).text
    #eskifiyat = phone.find("div",{"class":"price-promotion-container"}).find("div",{"class":"prc-box-orgnl"}).text
    
    print(f"{marka} {model.ljust(100)} {fiyat}")