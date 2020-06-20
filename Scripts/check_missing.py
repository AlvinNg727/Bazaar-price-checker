import requests
from items import items

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"
def check():
    bazaarJson = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()

    final1 = []
    final2 = []

    for key in items:
        value = items[key]
        final1.append(value)

    for num2, i2 in enumerate(bazaarJson["products"]):
        final2.append(i2)

    print(list(set(final2) - set(final1)))