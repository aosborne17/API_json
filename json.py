import json

car_data = {"name": "Tesla", "engine": "electric"}
print(car_data)

print(type(car_data))

"""
json.dumps changes a python dictionary to a json string
"""

car_data_json_string = json.dumps(car_data)

print(type(car_data_json_string))