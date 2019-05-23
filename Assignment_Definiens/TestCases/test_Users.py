import json
import jsonpath
import requests
import pytest

@pytest.fixture()
def getresponse():
    global response
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)


@pytest.mark.Smoke
def test_Validate_StatusCode(getresponse):
    assert response.status_code == 200

@pytest.mark.Smoke
def test_FetchServer(getresponse):
    assert response.headers.get('Server') == 'cloudflare'

@pytest.mark.Sanity
def test_CountUser(getresponse):
    json_response = json.loads(response.text)
    users = jsonpath.jsonpath(json_response, '$[:]')
    assert len(users) == 10
