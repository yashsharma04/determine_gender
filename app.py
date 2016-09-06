import requests
import json 

a = raw_input("Enter the Name : ")
url = "https://api.genderize.io/"

querystring = {"name":a}

headers = {
    'cache-control': "no-cache",
    'postman-token': "e5f77ec6-3092-b5d1-ff59-5f76931f1cb9"
    }

#using requests 
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
print data["gender"]
# print(response.text)