# import json as we are using json file for exchange rate data
import json


def Find_exchange_rate():
    # copies the data and stores it to a variable "exchange rates"
    with open("exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)
        print(exchange_rates)

        # for loop to iterate over the nested dictionary "rates" to print keys and values
        for key in exchange_rates["rates"]:
            print(f"Currency : {key}, Exchange Rate : {exchange_rates['rates'][key]}")

# calling the function
Find_exchange_rate()
