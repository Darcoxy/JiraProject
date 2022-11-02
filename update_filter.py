import requests
from requests.auth import HTTPBasicAuth
import json

def getFilter():
    url = 'https://anbast.atlassian.net/rest/api/3/filter/19012'

    auth = HTTPBasicAuth('jj@anbast.com', 'lH37epa48lBGDcT3YkXW43B0')

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
    print(response)

def updateFilter():
    url = 'https://anbast.atlassian.net/rest/api/3/filter/19012'

    auth = HTTPBasicAuth("email@example.com", "<lH37epa48lBGDcT3YkXW43B0>")

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
    #print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) 

updateFilter()
#getFilter()