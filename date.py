from datetime import datetime #datetime fonksiyonu içerisinde datetime classı.
# from datetime import date
# from datetime import time 
# print(dir(datetime))  # dir() fonksiyon altındakı classları gösterir.

simdi = datetime.now() #now metodu
simdi = datetime.today() #now ile aynı işlevi görür.
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi) #daha açıklayıcı bir şimdi bilgisi verir.

result = datetime.strftime(simdi, '%Y') #yalnızca yıl bilgisini verdi.
result = datetime.strftime(simdi, '%X') #yalnızca saat bilgisi
result = datetime.strftime(simdi, '%D') #yalnızca gün bilgisi 
result = datetime.strftime(simdi, '%A') #yalnızca gün bilgisi (string)
result = datetime.strftime(simdi, '%B') #yalnızca ay bilgisi (string)

result = datetime.strftime(simdi, '%Y %B %A')
print(result) #şimdiki tarihi ve saati yazdırır.


t = '21 June 2023 hour 12:51:32'

# gun, ay, yil = t.split() #belirtilen nesneyi belirtilen yerlere atayarak ayırır.
# print(gun)
# print(ay)
# print(yil)

dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

print(dt)

birthday = datetime(2002,11,13,1,20,15)
result = datetime.timestamp(birthday) #verilen date'i saniye cinsinden verir.
result = datetime.fromtimestamp(result) #saniye bilgisini tekrar datetime a çevirir.

result = simdi - birthday #şu andan belirtilen tarihi çıkararak gün ve saat bilgisi verir.
#timedelta
print(result)


from datetime import timedelta

result = simdi + timedelta(days=10) #belirtilen tarihe 10 gün ekler

print(result)

