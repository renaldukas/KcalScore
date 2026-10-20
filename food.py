import requests

barcode = input("Enter a barcode: ")

url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
headers = {"User-Agent": "SchoolCalorieApp/1.0"}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

data = response.json()
if data.get("status") != 1:
    print("Sorry, that product isn't in the database.")
    exit()

product = data["product"]

name = product.get("product_name", "Unknown")
kcal = product.get("nutriments", {}).get("energy-kcal_100g", "Unknown")
nova = product.get("nova_group", "Unknown")
score = product.get("nutriscore_grade", "Unknown")
print(f"{name}: {kcal} kcal, processing level {nova}, score {score}")