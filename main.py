from collections import Counter
from typing import cast
from urllib import request, response

from jira import JIRA
from jira.client import ResultList
from jira.resources import Issue

url = "https://anbast.atlassian.net/browse/SR-1468"

jira = JIRA(
    basic_auth=("jj@anbast.com", "J$b#g!b4a"), 
)

headers = {
    "Accept": "application/json"
}

response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=jira
)

print(json.dumps(json.loads(reposnse.text), sort_keys=True, indent=4, separators=(",", ": ")))
