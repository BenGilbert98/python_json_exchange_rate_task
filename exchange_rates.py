import json


def Find_exchange_rate():
    with open("exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)
        print(exchange_rates)

        for key in exchange_rates["rates"]:
            print(f"Currency : {key}, Exchange Rate : {exchange_rates['rates'][key]}")


Find_exchange_rate()
