import requests
from items import products

api_key = "ba710f2d-6547-4936-8aab-72b01300a8a5"


def check_average(productId, amount):
    item = requests.get("https://api.hypixel.net/skyblock/bazaar/product?key=" +api_key + "&productId=" + productId).json()

    instaSell = item["product_info"]["buy_summary"][0]["pricePerUnit"] * amount
    instaBuy = item["product_info"]["sell_summary"][0]["pricePerUnit"] * amount * 0.99

    return instaBuy - instaSell

def input(item, amount):
    if item.lower() in products:
        return check_average(products[item.lower()], amount)
    else:
        return "That is not a valid item"