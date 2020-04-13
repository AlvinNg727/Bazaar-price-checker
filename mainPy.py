import requests
from items import products

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"


def check_average(productId):
    item = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=" + api_key + "&productId=" + productId).json()

    print(item["product_info"]["quick_status"]["sellPrice"])

def main():
    get_item = input("What item do you want to check: ")

    if get_item.lower() in products:
        check_average(products[get_item.lower()])
    else:
        print("This is not a valid item")
    
main()
