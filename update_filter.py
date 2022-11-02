import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://anbast.atlassian.net/'

auth = HTTPBasicAuth('jj@anbast.com', 'PAArIcdYuTqSujYW8ylq69B7')

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps( {
    'jql': 'type = project = PUR AND fixVersion >= 1.61.0 and fixVersion <= 1.63.77',
    'name': 'Updated JJ Test Filter',
    'description': 'Update from 02/11/2022'
})

response = requests.request(
    "PUT",
    url,
    data=payload,
    headers=headers,
    auth=auth
)