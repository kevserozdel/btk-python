"""liste = [1,2,3,4,5] #class

iterator=iter(liste)  #iter metod, itere yazılmalı ki liste iterable bir obje olsun.

print(next(iterator)) #sırayla listenin birinci elamanından başlayarak yazdırır.
print(next(iterator))
print(next(iterator)) #ard arda yazınca 1 2 3 diye liste elemanlarını next metoduyla yazdırır. her yazıldığında bir sonraki elemanı 
                     #yazmış olur.

print(next(iterator))
print(next(iterator))
# print(next(iterator)) #listenin uzunluğunu aşarsak StopIteration hatası verir.

 aslında for döngüsünün altında dönen olay bu 
for i in liste:
    print(i)                      """
"""
iterator = iter(liste)
while True:
    try:
        eleman = next(iterator)
        print(eleman)
    except StopIteration:
        break

"""
class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x=self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
list= MyNumbers(10,20)

myiter=iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#for x in list:
#    print(x)