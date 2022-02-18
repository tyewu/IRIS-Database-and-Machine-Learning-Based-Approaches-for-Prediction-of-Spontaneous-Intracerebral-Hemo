import requests
import json


def client_project(test_data):
    content_type = 'application/json'
    headers = {'content-type': content_type}
    addr = 'http://localhost:5001'
    url = addr + '/api'
    jsonin = json.dumps({"data": test_data})
    # post request
    res = requests.post(url, json=jsonin, headers=headers)
    print(res.text)


data = {'Name': 'fan',
        'Age': 26,
        'Baseline heart rate': 10,
        'Uric acid': 2,
        'D-dimer': 4,
        'Chlorine': 5,
        'GCS': 2,
        'GFR': 7}
client_project(data)