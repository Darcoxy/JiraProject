import requests
from requests.auth import HTTPBasicAuth
import json

""" url = 'https://anbast.atlassian.net/rest/api/3/filter/19012'

auth = HTTPBasicAuth('jj@anbast.com', 'njJpXckRq80MU5kqmquH52F4')

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = json.dumps( {
    'jql': 'type = project = PUR AND fixVersion >= 1.61.0 and fixVersion <= 1.63.77',
    'name': 'TestingJiraProject',
    'description': 'Update from 02/11/2022'
})

response = requests.request(
    "PUT",
    url,
    data=payload,
    headers=headers,
    auth=auth
) """


def getFilter():
    url = 'https://anbast.atlassian.net/rest/api/3/filter/19012'

    auth = HTTPBasicAuth('jj@anbast.com', 'njJpXckRq80MU5kqmquH52F4')

    headers = {
        'Accept': 'application/json'
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def updateFilter():
    url = 'https://anbast.atlassian.net/rest/api/3/filter/19012'

    auth = HTTPBasicAuth("email@example.com", "<api_token>")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "jql": "type = project = PUR AND fixVersion >= 1.61.0 and fixVersion <= 1.63.77",
        "name": "UpdatedTestingJiraProject",
        "description": "Lists all bugs for patch version"
    })

    response = requests.request(
        "PUT",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    print(response)
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) 

#updateFilter()
getFilter()