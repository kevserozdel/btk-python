import requests #herhangi bir internet sitesinin sayfasındaki kaynak html kodlarını görebiliriz.
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
for i in result:
    if i["userId"] == 1:
        print(i)
        print(i["title"]) #title bilgisi