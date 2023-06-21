import os
import datetime

result = dir(os)
result = os.name  #işletim sistemini belirtir. nt => windows

# os.chdir('C:\\') dizin değiştirir.
# os.chdir('../..') .. bir üst dizine aktarır. ../.. ise iki üst dizine aktarır

""" klasör oluşturma """

# os.mkdir("newdirectory") o isimde dosya oluşturur.
# os.makedirs("newdirectory/kevser") #alt klasör
# os.rename("newdirectory","yeniklasör")
# os.rmdir("yeniklasör")  # klasörü siler
# os.removedirs("yeniklasör/kevser")  # alt dizini olan klasörleri siler
# result = os.getcwd() #bu py dosyası nerede onu belirtir.

""" listeleme """

# result = os.listdir()
for dosya in os.listdir():
    if dosya.endswith('.py'): #py ile biten dosyaları listeler
        print(dosya)

# result = os.stat("date.py") #date.py dosyası ile alaklı boyut, oluşturulma tarihi, değiştirilme tarihi gibi bilgileri verir

# result = datetime.datetime.fromtimestamp(result.st_ctime) #os.stat ile alınan oluşturulma tarihi bilgisini datetime ile okunabilir hale getirdik.
# result = datetime.datetime.fromtimestamp(result.st_atime) #son erişilme tarihi axes
# result = datetime.datetime.fromtimestamp(result.st_mtime) #değiştirilme tarihi modified

# os.system('notepad.exe') # yazılan uygulamayı açar os.system('')

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/kevse/OneDrive/Belgeler/pythonbtk/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/Users/kevse/OneDrive/Belgeler/pythonbtk/_os.py")
print(result)