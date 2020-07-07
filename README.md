# What is JSON?
## Javascript Object Notation 

### json is a syntax for exchanging data between a browser and server

- json is also used to parse data from existing files or web files
- parsing is where when given a sequence of text, identifying the various parts of the text and is able to assign ‘meaning’ to the text
- The data can only be text, thus json is written in json format
``` bash
- Data Types
a string
a number
an object (json object)
an array
boolean
null

```
In json, data is stored in name/value pairs:

``` bash
{"name": "Andrew", "age": "20"}
- The pairing is seperated by a comma
```

```python
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
```

# json and classes exercise
```python
"""
import json
create a class named Exchange_Rates with attributes
fetch the data from exchange_rates.json
display the data and the type of data
have a method which returns the exchange rates
display exchange rates with specific currencies
"""
```
API calls go to web browsers and request for certain information\
the web browsers have their own API where they can interpret our request\
and send the data back to the premise data if it allows.\
Browsers would have some data that they do not want to allow access to and\
when we request an error would be raised

!["API Picture] --- show pic

```bash
CRUD stands for "Create, Read, Update and Delete.
These are the four basic database operations.
Many HTTP services model CRUD operations.

```
