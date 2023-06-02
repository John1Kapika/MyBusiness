import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

print("Выберете Вашу валюту:\n1) RUB\n2) USD\n3) EUR\n\n")
a = input()
print("Выберете валюту, с которой хотите сверить:\n1) RUB\n2) USD\n3) EUR\n\n")
b = input()

amount = 100
if a == 1:
    from_currency = "RUB"
if a == 2:
    from_currency = "USD"
if a == 3:
    from_currency = "EUR"
if b == 1:
    to_currency = "RUB"
if b == 2:
    to_currency = "USD"
if b == 3:
    to_currency = "EUR"
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")