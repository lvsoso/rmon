#coding=utf-8

import requests

CREATE_SERVER = 'http://127.0.0.1:5000/api/servers/'

def create_server(name, host):
    data = {
        "name": name,
        "host": host
    }
    resp = requests.post(CREATE_SERVER, json=data)
    return resp.json()

create_server("test", "127.0.0.1")