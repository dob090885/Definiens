import json
import jsonpath
import requests
import pytest


@pytest
def test_Validate_StatusCode():
    # Send the GET request
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    assert response.status_code == 200

@pytest
def test_FetchServer():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    assert response.headers.get('Server') == 'cloudflare'

@pytest
def test_CountUser():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    json_response = json.loads(response.text)
    albums = jsonpath.jsonpath(json_response, '$[:]')
    assert len(albums) == 100
