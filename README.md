# Exchange Rate Task
- In this instance we will be using a JSON file with exchange rates 
- build your class around it 
- You will see from the exchange rates file that you will be accessing these data points  as you would in a dictionary

## Acceptance Criteria 
- Create a New Repo for this task
- .gitignore and README in a new pycharm project
- have the exchange_rates.json file available in your pycharm project/folder
- Display all the data from .json file
- iterate through the data and display exchange rate by country

## Solution
- Since we are using a json file we must ```import json```
- Json is used to convert the json file into a python dictionary so it can be iterated through
- The next step is to define a function for our solution
- Inside the function we have to assign a variable to the converted json file (shown below)
``` python
def Find_exchange_rate():
    with open("exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)
```
- Then, the iterative method is added 
- It will iterate through the nested dictionary "rates" and will print each key value pair
``` python
        for key in exchange_rates["rates"]:
            print(f"Currency : {key}, Exchange Rate : {exchange_rates['rates'][key]}")
```

- Finally the function must be called
``` python
Find_exchange_rate()
```

### All together 
``` python
import json


def Find_exchange_rate():
    with open("exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)
        print(exchange_rates)

        for key in exchange_rates["rates"]:
            print(f"Currency : {key}, Exchange Rate : {exchange_rates['rates'][key]}")


Find_exchange_rate()

```