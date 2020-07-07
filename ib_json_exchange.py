import json

class ExchangeRates:
    def __init__(self):
        self.self = self

    # we can add a function which opens the files, so instead of having to type it each time
    # we can just call this function, e.g. self.fetch_exchange_rate
    def fetch_exchange_rate(self, cur):
        with open("exchange_rates.json") as jsonfile:
            # reading from the file we just created
            rates = json.load(jsonfile)
            print(f"The exchange rate between EUR and {cur} is", rates["rates"][
                cur])  # since this is in the with open block, you know that this is coming from the new file
    def fetch_exchange_rates(self, curr):
        with open("exchange_rates.json") as jsonfile:
            # reading from the file we just created
            rates = json.load(jsonfile)
            x_rates = rates["rates"]  # rates is the whole dict, x_rates is the nested dict
            for cur in curr: # Iterates through the input "curr" which is the list of all the keys in the dict
                print(f"The exchange rate between EUR and {cur} is", x_rates[cur])
    def fetch_rates_list(self):
        with open("exchange_rates.json") as jsonfile:
            # reading from the file we just created
            rates = json.load(jsonfile)
            x_rates_list = rates["rates"].keys()  # converts the keys of the dictionary "rates" into a list
            return x_rates_list

c = ExchangeRates()
c.fetch_exchange_rate("AUD")
curr = (list(c.fetch_rates_list()))
c.fetch_exchange_rates(curr)