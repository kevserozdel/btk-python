import json
import requests
api_url = "https://api.exchangeratesapi.io/latest?base="
bozulan_doviz = input("Bozulan döviz türü: ")
alinan_doviz = input("Alınan döviz türü: ")
miktar = input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: ")
result = requests.get(api_url+bozulan_doviz)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alinan_doviz],alinan_doviz))

#site key istediği için kod hata veriyor.s
