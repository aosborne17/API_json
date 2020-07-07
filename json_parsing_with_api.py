import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.status_code)

# Why should we use built in packages

if post_codes_req.status_code == 200:
    print("Success!")
elif post_codes_req.status_code == 400:
    print("Page Not Available")
