import json
import jsonpath
import requests
import pytest


@pytest.mark.Smoke
def test_Validate_StatusCode():
    # Send the GET request
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.Smoke
def test_FetchServer():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.headers.get('Server') == 'cloudflare'

@pytest.mark.Sanity
def test_CountUser():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    json_response = json.loads(response.text)
    users = jsonpath.jsonpath(json_response, '$[:]')
    assert len(users) == 10
