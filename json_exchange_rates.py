"""
import json
create a class named Exchange_Rates with attributes
fetch the data from exchange_rates.json
display the data and the type of data
have a method which returns the exchange rates
display exchange rates with specific currencies
"""

import json

class Exchange_Rates:
    def __init__(self):
        pass

    def check_rates(self):
        with open("exchange_rates.json", "r") as exchangefile:

            rates = json.load(exchangefile)
            for data in rates:
                if data == "base":
                    print(rates["base"])
                # print(data)
            print(rates)
            # print(type(rates))


    def choose_rate(self):
        with open("exchange_rates.json", "r") as exchangefile:

            rates = json.load(exchangefile)
            for data in rates:
                if data == "rates":
                    print(rates["rates"])
                    


"""
for key in dataset:
            if key == "rates":
                print(dataset["rates"])
        currency = input("What currency would you like the exchange rate of, please see list.\n")
        # display exchange rates with specific currencies
        print(dataset["rates"][currency])
"""

exchange1 = Exchange_Rates()

# exchange1.check_rates()
exchange1.choose_rate()
