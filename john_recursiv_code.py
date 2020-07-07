import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

json_data = post_codes_req.json()

class JSONReader:
    def get_all_values(self, nested_dictionary): # This is a method
        for key, value in nested_dictionary.items():  # iterate through the key, value pairs in this dictionary
            if type(value) is dict:  # if the value of a key is a dictionary, then you have found a nested dictionary
                self.get_all_values(value)  # recall this method passing in that dictionary to iterate through it
            else:
                print(key, ":", value)  # if the value of the dictionary is not a dict carry on looping through


json_reader = JSONReader()  # Create instance of this function
json_reader.get_all_values(json_data)  # Returns all the values inside a dictionary including any nested dictionaries