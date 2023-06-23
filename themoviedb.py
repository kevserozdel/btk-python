import requests

class Movie:

    def __init__(self):
        self.api_url ='https://api.themoviedb.org/3'
        self.api_key = '240c44000a8cb7d5e63a12a7fc8eefc5'

    def search(self, filmadi):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={filmadi}&page=1")
        return response.json()
    
    def popular(self):
        response = requests.get(f"{self.api_url}/trending/movie/day?api_key={self.api_key}&language=en-US")
        return response.json()
    
    def vision(self):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
movieApi = Movie()

while True:
    secim = input('1-Film ara\n2-En popüler filmleri listele\n3-Vizyondaki filmleri listele\n4-Çıkış\nSeçiminiz: ')

    if secim == '1':
        filmadi = input("Film adı: ")
        movies = movieApi.search(filmadi)
        for movie in movies['results']:
            print(movie['name'])
    elif secim == '2':
        movies = movieApi.popular()
        for movie in movies['results']:
            print(movie['title'])
    elif secim == '3':
        movies = movieApi.vision()
        for movie in movies['results']:
            print(movie['title'])
    elif secim == '4':
        break 
    else:
        print('Geçerli bir sayı giriniz.')

