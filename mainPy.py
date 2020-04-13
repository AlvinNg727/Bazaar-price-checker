import requests
from items import products

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"


def check_average(productId):
    item = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=" +api_key + "&productId=" + productId).json()

    instaSell = item["product_info"]["buy_summary"][0]["pricePerUnit"]
    instaBuy = item["product_info"]["sell_summary"][0]["pricePerUnit"]

    print(instaBuy - instaSell)

def main():
    get_item = input("What item do you want to check: ")

    if get_item.lower() in products:
        check_average(products[get_item.lower()])
    else:
        print("THAT AINT EVEN A FUCKING ITEM U GAY SHIT")
    
main()
