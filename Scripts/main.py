import requests
import time
from getAverage import check_average
from items import items

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"

priceList = []
currentIndex = 0
page = 1

names = []
finalItems = []

#checkItem = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
#checkItem = checkItem["products"]

lowestAmount = 0

def check():
    global lowestAmount
    try:
        lowestAmount = int(input("What is the lowest amount of insta buys and insta sells: "))
    except ValueError:
        print("That is not a valid number.")
        check()
    if lowestAmount >= 0:
        pass
    else:
        print("That is not a valid number.")
        check()


def Main():
    global currentIndex, priceList, names, finalItems, lowestAmount, page

    checkItem = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + api_key).json()
    checkItem = checkItem["products"]

    currentIndex = 0
    priceList.clear()
    names.clear()
    finalItems.clear()
    item = ""
    page = 1

    check()

    startTime = time.time()

    for key in items:
        if (checkItem[items[key]]["quick_status"]["sellMovingWeek"] >= lowestAmount) and (checkItem[items[key]]["quick_status"]["buyMovingWeek"] >= lowestAmount):
            item = check_average(items[key])
            priceList.append([item, key])
        currentIndex += 1
        endTime = time.time()
        print(str(currentIndex) + "/197    " + str(round((endTime - startTime), 1)) + " seconds")

    priceList.sort(reverse=True)

    for i in range(len(priceList)):
        names.append(priceList[i][1])
        finalItems.append(priceList[i][0])

    printLn(names, finalItems)

    again = input("Do you want to do this again? (y/n)")
    if again == "y":
        Main()
    elif again == "n":
        quit()


def printLn(name, price):
    global page, priceList

    maxPage = 0

    if len(priceList) % 10 != 0:
        maxPage = (len(priceList) // 10) + 1
    elif len(priceList) % 10 == 0:
        maxPage = len(priceList) // 10

    if page <= maxPage:
        if page == maxPage:
            for i in range((page * 10) - 10, len(priceList)):
                print(str(i + 1) + ". " + str(name[i]) + ": " + str(price[i]) + "\n")
        else:
            for i in range((page * 10) - 10, (page * 10)):
                print(str(i + 1) + ". " + str(name[i]) + ": " + str(price[i]) + "\n")
            more = input("Do you want to load more results? (y/n)")
            if page >= 20:
                if more == "Y":
                    print("This is already the last page")
            else:
                if more == "y":
                    page += 1
                    printLn(names, finalItems)
                elif more == "n":
                    pass

Main()
