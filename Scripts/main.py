import requests
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
page = 1

names = []
finalItems = []

def Main():
    global itemsList, names, finalItems, page

    currentIndex = 0
    itemsList.clear()
    names.clear()
    finalItems.clear()
    item = ""
    page = 1

    getAmount()

    bazaarJson = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
    bazaarJson = bazaarJson["products"]

    #get
    for key in items:
        value = items[key]
        if (bazaarJson[value]["quick_status"]["sellMovingWeek"] >= lowestAmount) and (bazaarJson[value]["quick_status"]["buyMovingWeek"] >= lowestAmount):
            item = check_average(bazaarJson, value)
            itemsList.append([item, key])
        currentIndex += 1
        print(str(currentIndex) + "/197    ")

    #reverse the list
    itemsList.sort(reverse=True)

    for i in range(len(itemsList)):
        names.append(itemsList[i][1])
        finalItems.append(itemsList[i][0])

    printLn(names, finalItems)

    again = input("Do you want to do this again? (y/n)")
    if again == "y":
        Main()
    elif again == "n":
        quit()


def printLn(name, price):
    global page

    maxPage = 0

    if len(name) % 10 != 0:
        maxPage = (len(name) // 10) + 1
    elif len(name) % 10 == 0:
        maxPage = len(name) // 10

    if page <= maxPage:
        if page == maxPage:
            for i in range((page * 10) - 10, len(name)):
                print(str(i + 1) + ". " + str(name[i]) + ": " + str(price[i]) + "\n")
        else:
            for i in range((page * 10) - 10, (page * 10)):
                print(str(i + 1) + ". " + str(name[i]) + ": " + str(price[i]) + "\n")
            more = input("Do you want to load more results? (y/n)")
            if page >= 20 and more == "Y":
                print("This is already the last page")
            else:
                if more == "y":
                    page += 1
                    printLn(name, price)

Main()