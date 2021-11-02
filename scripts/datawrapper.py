import requests
import json

# Create a new file ("touch key.py" in terminal) that houses an API_KEY constant.
# Put your datawrapper API key there.
from key import API_KEY

def new_chart(params, data):
    url = 'https://api.datawrapper.de/v3/charts'

    payload = {
        "theme": "cbc",
        "metadata": {
            "describe": {}
        }
        }

    for key, value in params.items():
        
        if key == 'intro':
            payload['metadata']['describe'][key] = value
        else:
            payload[key] = value

    print(payload)

    headers = {
        'Authorization': 'Bearer ' + API_KEY,
        'content-type': 'application/json'
        }
    
    chart_data = data.to_csv()

    r = requests.post(url, json=payload, headers=headers)
    chart_id = r.json()['id']

    data_headers = {
        'Authorization': 'Bearer ' + API_KEY,
        'content-type': 'text/csv'
    }

    publish_headers = {
        'Authorization': 'Bearer ' + API_KEY,
    }

    p = requests.put(url + "/" + chart_id + '/data', headers=data_headers, data=chart_data)
    publish = requests.post(url + "/" + chart_id + '/publish', headers=publish_headers)
    if (str(p) == '<Response [201]>'):
        print("Success! Your chart has been created.")
    else:
        print("Chart creation failed with error: " + str(p))

    chart = json.loads(publish.text)
    print(chart)
    return chart