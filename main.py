import getAverage
from items import products

priceList = []
currentIndex = 0
productIndex = 0



def Main():
    global productIndex
    for key in products:
        item = getAverage.check_average(products[key], 1)
        priceList.append(item)
        productIndex += 1
        print(productIndex)

    priceList.sort(reverse=True)
    del priceList[10:]
    print("\n".join(priceList))

    input()

Main()