import json

car_data = {"name": "Tesla", "engine": "electric"}
print(car_data)

print(type(car_data))

"""
json.dumps changes a python dictionary to a json string
"""

car_data_json_string = json.dumps(car_data)

print(type(car_data_json_string))

"""
Here we are dealing with files
"""

# with open("new_json_file.json", "w") as jsonfile:
    # enter the name of the file, permission type write 'w'


    # json.dump(car_data, jsonfile)
    # json file takes two args, one being the dict, and the
    # other being the json file

# Encoding, creating and writing into json file

with open("new_json_file.json") as jsonfile:  #decoding

    # reading from the file we just created
    car = json.load(jsonfile)
    print(type(car)) # checking data type of the car
    print(car['name']) # Here we are printing the value associated with the key 'name'
    print(car['engine']) # this time we are displaying the value of the 'engine' key


"""
In the above block of code we have decoded/read the file that we 
had just made 'new_json_file'

Using the 'load' method allowed us to read over the file
"""