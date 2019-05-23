import json
import jsonpath
import requests
import pytest



def test_validate_urlresponse():
    # Send the GET request
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    # print(response.tex)

    # validate Status Code
    print(response.status_code)

    assert response.status_code == 200

    # Fetch Elapsed time
    print(response.elapsed)

    json_response = json.loads(response.text)
    albums = jsonpath.jsonpath(json_response, '$[:]')
    print(len(albums))
    print(albums)
