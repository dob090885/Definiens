import json
import jsonpath
import requests

# API URL

url= "https://jsonplaceholder.typicode.com/albums"

#Send the GET request
response = requests.get(url)
#print(response.tex)
print(response.headers.get('Server'))

#validate Status Code
print(response.status_code)

assert response.status_code == 200

#Fetch Elapsed time
print(response.elapsed)

json_response = json.loads(response.text)
albums = jsonpath.jsonpath(json_response, '$[:]')
print(len(albums))
#print(albums)