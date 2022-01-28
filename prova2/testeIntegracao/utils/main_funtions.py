import json
import unittest
import requests
from nose.tools import *


URL = "https://testapi.jasgme.com/sgme/api"

def auth_token():
    data = {
        "login": "iasmin.santos@dellead.com",
        "password": "1234abcd"
    }

    response = requests.post(f"{URL}/authenticate/login", json=data)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    token = json_data['token']
    return f"Bearer {token}"

def get_id(header):
    response = requests.get(f"{URL}/companies", headers=header)
    assert_equal(response.status_code, 200)

    json_data_id = json.loads(response.content)
    company = json_data_id[0]
    id = company['id']
    return id

