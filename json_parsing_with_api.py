import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

"""
All of these functions 'headers, content etc,
is all carried out by the requests module.
It is able to collect the data from the website specified and then return it
in milliseconds
"""


# print(post_codes_req.headers)
# print(type(post_codes_req.headers)) # We are displaying the data type of the browser header
# print(post_codes_req.content)
print(post_codes_req)

# Why should we use built in packages

"""
Using JSON alongside requests!!!
"""
# print(post_codes_req.json())

# json_data = post_codes_req.json()

# print(type(json_data)) # This will tell us the class of the data

"""
Once knowing that json_data is a dict, we can the iterate through the dictionary
and find out the data types inside the dictionary
"""
# for key in json_data:
#     print(key) # Here we iterate through all of the keys in the json_data dict (only two keys), and print these keys
#
# print(json_data) # Here we are displaying the whole of json_data, which we found out was a dictionary


"""
# Exercise is to fetch data by key value pairs within dictionaries
# Create a function to return the above values (Key:value)
# Create a class and move the code inside the class

"""
json_data = post_codes_req.json()

for key, value in json_data.items():
    if type(value) is dict:
        print(value)












"""
Creating this class allows us to recall this functionality
whenever we need to as well as importing it to other files
"""
# class Live_Web_Status_Code:
#
#     def check_status_code(self):
#         if post_codes_req.status_code == 200:
#             return "Success"
#         elif post_codes_req.status_code == 400:
#             return "Page Not Available"
#
#
# requests1 = Live_Web_Status_Code()
#
# print(requests1.check_status_code())
