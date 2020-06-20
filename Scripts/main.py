import requests
import time
from items import items
import check_missing

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"

def check_average(json, productId):
    buyPrice = 0
    sellPrice = 0
    #if there are no buy orders for the item, the buyPrice will = 0
    if len(json[productId]['sell_summary']) > 0:
        buyPrice = json[productId]["sell_summary"][0]["pricePerUnit"]

    #if there are no sell orders for the item, the sellPrice will = 0
    if len(json[productId]['buy_summary']) > 0:
        sellPrice = json[productId]["buy_summary"][0]["pricePerUnit"]

    return round((sellPrice - buyPrice), 1)

#the lowest amount the insta sell and buy have to be in last 7d
lowestAmount = 0

#getting the lowest amount
def getAmount():
    global lowestAmount
    try:
        lowestAmount = int(input("What is the lowest amount of insta buys and insta sells: "))
    except ValueError:
        print("That is not a valid number.")
        getAmount()
    if lowestAmount < 0:
        print("That is not a valid number.")
        getAmount()

def MainLoop():
    check_missing.check()
    getAmount()
    
    itemsList = []
    itemNames = []
    productId = []
    while True:
        try:
            #global itemsList, itemNames, productId
            itemsList.clear()
            itemNames.clear()
            productId.clear()

            bazaarJson = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
            bazaarJson = bazaarJson["products"]

            #get the list of items that have a average sell more then the lowest amount
            for key in items:
                value = items[key]
                if (bazaarJson[value]["quick_status"]["sellMovingWeek"] >= lowestAmount) and (bazaarJson[value]["quick_status"]["buyMovingWeek"] >= lowestAmount):
                    item = check_average(bazaarJson, value)
                    itemsList.append([item, key])

            #reverse the list
            itemsList.sort(reverse=True)

            for i in range(len(itemsList)):
                itemNames.append(itemsList[i][1])
                productId.append(itemsList[i][0])

            printLn(itemNames, productId)
            time.sleep(5)
        except KeyboardInterrupt:
            print("Stopping...")
            break

def printLn(name, price):
    for i in range(0, 10):
        print(f"{str(i + 1)}. {str(name[i])}: {str(price[i])}\n")

MainLoop()