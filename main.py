import os
import json
import requests
from jira import JIRA
from ssl import Options
from pathlib import Path

#Global Variables
slack_token = os.getenv('SLACKAPITOKEN')
jira_token = os.getenv('JIRAAPITOKEN')
slack_channel = '#testing_bot'
filter_url = 'https://anbast.atlassian.net/issues/?filter=19013'

#This is a required dictionary for Jira to know where to connect and to know to verify
Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': filter_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()

#This will read the version numbers from the html file and return them in a list
def get_purgo_version_numbers():
    data = Path("index.html").read_text().replace('\n', ' ')
    output = data[2:]
    patchVersion = output.split('<')[0]
    testVersion = output.split('>')[1].replace(" ", "")
    print("get_purgo_version_numbers")
    return([patchVersion, testVersion])

#This will update the patch filter
def update_patch_filter():
    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    patchJQL = 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <=' + get_purgo_version_numbers(0)
    patchJQL.join(get_purgo_version_numbers(0))
    patchJQL = patchJQL.replace('\u0000', '').rstrip()
    updatePatchFilter = jira.update_filter(19012, 'JiraProjectPatchQueue', 'Updated Patch Queue with Script', patchJQL[:-2])
    print("update_patch_filter")

#This will update the test filter
def update_test_filter():
    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    testJQL = 'project = PUR AND fixVersion >= 1.65.0 and fixVersion <=' + get_purgo_version_numbers(1)
    testJQL.join(get_purgo_version_numbers(1))
    testJQL = testJQL.replace('\u0000', '').rstrip()
    updateTestFilter = jira.update_filter(19013, 'JiraProjectTestQueue', 'Updated Test Queue with Script', testJQL[:-2])
    print("update_test_filter")

#This will post a message to slack
post_message_to_slack('testing')