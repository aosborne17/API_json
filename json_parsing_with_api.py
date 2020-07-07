import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.status_code)

# Why should we use built in packages

"""
Creating this class allows us to recall this functionality
whenever we need to as well as importing it to other files
"""
class Live_Web_Status_Code:

    def check_status_code(self):
        if post_codes_req.status_code == 200:
            return "Success"
        elif post_codes_req.status_code == 400:
            return "Page Not Available"


requests1 = Live_Web_Status_Code()

print(requests1.check_status_code())
