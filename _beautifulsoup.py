html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Merhaba
    </h1>
    <div class="grup1">
    <h2>
        Python öğreniyorum
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
    </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>
<ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="spongebob.jpg" alt="">

    <a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example2.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example3.com/elsie" class="sister" id="link1">Elsie</a>
</body>
</html>

"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
result = soup.prettify()   #html kodundaki ayarsızlıkları gidererek kodu doğru hale okunabilir hale getirir.
result = soup.title #title kısmı kodu
result = soup.head #head kısmı kodu
result = soup.title.name #title etiketi
result = soup.title.string #title içindeki string ifade
result = soup.h1
result = soup.h2 #birden fazla h2 olduğu için sadece ilk h2yi yazar.
result = soup.h2.string
result = soup.find_all('h2') #bütün h2 leri gösterir.
result = soup.find_all('h2')[0] #ilk h2
result = soup.find_all('h2')[1] #2. h2
result = soup.div #1. div
result = soup.find_all('div') #bütün divler
result = soup.find_all('div')[0]
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul
result = soup.find_all('div')[1].ul.find_all('li')
result = soup.div.findChildren() #divin altındakileri yazar
result = soup.div.findNextSibling() #bir sonraki divi bulur
result = soup.div.findNextSibling().findPreviousSibling() #bir sonraki ve bir önceki div.

result = soup.find_all('a')

for link in result:
    print(link.get('href'))



print(result)