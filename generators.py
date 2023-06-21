def cube():                #generator'un iterator dan farkı bellekte yer kaplamaz. sadece bir kez itere edilebilir.
    for i in range(5):     
        yield i ** 3  #yield döngüyü sonlandırmaya yarar. ilgili değişken sadece 1 kez kullanılır.

for i in cube():
    print(i)

#eğer değerleri sadece bir kere kullanacaksak ve listeye ihtiyaç duymuyorsak generatorler kullanılabilir.

gen = (i**3 for i in range(5))  #comprehension

for i in gen:
    print(i)
# print(next(gen))
