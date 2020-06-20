import requests
import time
from items import items


api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"

def check_average(json, productId):
    #if there are no buy orders for the item, the buyPrice will = 0
    if len(json[productId]['sell_summary']) > 0:
        buyPrice = json[productId]["sell_summary"][0]["pricePerUnit"]
    else:
        buyPrice = 0

    #if there are no sell orders for the item, the sellPrice will = 0
    if len(json[productId]['buy_summary']) > 0:
        sellPrice = json[productId]["buy_summary"][0]["pricePerUnit"]
    else:
        sellPrice = 0
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
    if lowestAmount >= 0:
        pass
    else:
        print("That is not a valid number.")
        getAmount()

itemsList = []

names = []
finalItems = []

def Main():
    getAmount()

    while True:
        global itemsList, names, finalItems
        itemsList.clear()
        names.clear()
        finalItems.clear()
        item = ""

        bazaarJson = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
        bazaarJson = bazaarJson["products"]

        #get
        for key in items:
            value = items[key]
            if (bazaarJson[value]["quick_status"]["sellMovingWeek"] >= lowestAmount) and (bazaarJson[value]["quick_status"]["buyMovingWeek"] >= lowestAmount):
                item = check_average(bazaarJson, value)
                itemsList.append([item, key])

        #reverse the list
        itemsList.sort(reverse=True)

        for i in range(len(itemsList)):
            names.append(itemsList[i][1])
            finalItems.append(itemsList[i][0])

        printLn(names, finalItems)
        time.sleep(5)

def printLn(name, price):
    for i in range(0, 10):
        print(f"{str(i + 1)}. {str(name[i])}: {str(price[i])}\n")

Main()