import requests
from items import products

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"

priceList = []
currentIndex = 0

def check_average(productId, amount):
    item = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=" + api_key + "&productId=" + productId).json()
    if len(item['product_info']['sell_summary']) > 0:
        instaBuy = item["product_info"]["sell_summary"][0]["pricePerUnit"] * amount * 0.99
    else:
        instaBuy = 0

    if len(item['product_info']['buy_summary']) > 0:
        instaSell = item["product_info"]["buy_summary"][0]["pricePerUnit"] * amount
    else:
        instaSell = 0
    return instaBuy - instaSell

def Main():
    global currentIndex, priceList
    names = []
    items = []

    for key in products:
        item = check_average(products[key], 1)
        priceList.append([item, key])
        currentIndex += 1
        print(str(currentIndex) + "/203")

    priceList.sort(reverse=True)
    del priceList[10:]
    
    for i, item in enumerate(priceList):
        names.append(str(priceList[i][1]))
        items.append(str(priceList[i][0]))
        
    for i in range(10):
        print(str(names[i]) + ": " + str(items[i]))

Main()
again = input("Do you want to do this again? (Y/n)")
if again == "Y":
    Main()
elif again == "n":
    quit()
else:
    quit()