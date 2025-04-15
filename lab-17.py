import requests


"""response = requests.get("https://example.com")
print("Код відповіді:", response.status_code)
print("HTML сторінки (перші 500 символів):")
print(response.text[:500])"""

"""name = input("Введіть ім'я: ")
url = f"https://api.agify.io/?name={name}"
response = requests.get(url)
data = response.json()

print(f"Ім'я: {data['name']}, прогнозований вік: {data['age']}")"""

"""data = {
    "name": "Olena",
    "city": "Kyiv"
}

response = requests.post("https://httpbin.org/post", data=data)
result = response.json()

print("Відповідь сервера:")
print("Надіслані дані:", result["form"])
"""

"""headers = {
    "User-Agent": "MyCustomAgent"
}

response = requests.get("https://httpbin.org/headers", headers=headers)
print("Заголовки, які отримав сервер:")
print(response.json()["headers"])"""

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()

print("Курс гривні (UAH):", data["rates"]["UAH"])
print("Курси для інших валют:")
for currency in ["EUR", "GBP", "CAD", "JPY", "PLN"]:
    print(f"{currency}: {data['rates'][currency]}")