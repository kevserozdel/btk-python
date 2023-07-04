""" Listeler arasından rastgele isim soyisim oluşturan program """


import random

def randomisim():
    isimler = ['Ahmet','Ayşe','Ela','Ali','Mehmet','Can','Seda','Deniz','Pelin','Tolga']
    soyisimler = ['Öztürk','Yılmaz','Çelik','Demir','Gül','Uğur']

    # print(f"{random.choice(isimler)} {random.choice(soyisimler)}")
    return "{} {}".format(random.choice(isimler), random.choice(soyisimler))
for i in range(5):
    print(randomisim())
    #randomisim()