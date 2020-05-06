import requests

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"

#sell_summary = insta sell price
#buy_summary = insta buy price
#sellMovingWeek = insta sell volume
#buyMovingWeek = insta buy volume

def check_average(productId):
    item = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
    item = item["products"]

    if len(item[productId]['sell_summary']) > 0:
        buyPrice = item[productId]["sell_summary"][0]["pricePerUnit"]
    else:
        buyPrice = 0

    if len(item[productId]['buy_summary']) > 0:
        sellPrice = item[productId]["buy_summary"][0]["pricePerUnit"]
    else:
        sellPrice = 0
    return round((sellPrice - buyPrice), 1)