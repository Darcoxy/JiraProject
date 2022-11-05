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
test_filter_url = 'https://anbast.atlassian.net/issues/?filter=19013'
patch_filter_url = 'https://anbast.atlassian.net/issues/?filter=19012'
both_filters_url = test_filter_url + '\n ' + patch_filter_url
released_patch_version = '1.63.77'
released_test_version = '1.65.19'
patch_version_changed = False
test_version_changed = False

#This is a required dictionary for Jira to know where to connect and to know to verify
Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

#This will read the patch version number and return it
def get_patch_version_number():
    data = Path("index.html").read_text().replace('\n', ' ')
    output = data
    patchVersion = output.split('<')[0].rstrip()
    return(patchVersion)

#This will read the test version number and return it
def get_test_version_number():
    data = Path("index.html").read_text().replace('\n', ' ')
    output = data
    testVersion = output.split('>')[1].replace(" ", "")
    return(testVersion)

def set_version_numbers():
    global released_patch_version
    global released_test_version

    new_patch_version = get_patch_version_number()
    new_test_version = get_test_version_number()

    if new_patch_version != released_patch_version:
        released_patch_version = new_patch_version
        global patch_version_changed
        patch_version_changed = True

    if new_test_version != released_test_version:
        released_test_version = new_test_version
        global test_version_changed
        test_version_changed = True

#This will update the patch filter
def update_patch_filter():
    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    patchJQL = 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <=' + get_patch_version_number()
    patchJQL.join(get_patch_version_number())
    patchJQL = patchJQL.replace('\u0000', '').rstrip()
    updatePatchFilter = jira.update_filter(19012, 'JiraProjectPatchQueue', 'Updated Patch Queue with Script', patchJQL[:-2])

#This will update the test filter
def update_test_filter():
    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    testJQL = 'project = PUR AND fixVersion >= 1.65.0 and fixVersion <=' + get_test_version_number()
    testJQL.join(get_test_version_number())
    testJQL = testJQL.replace('\u0000', '').rstrip()
    updateTestFilter = jira.update_filter(19013, 'JiraProjectTestQueue', 'Updated Test Queue with Script', testJQL[:-2])

#This will post a message to slack
def post_message_to_slack(text, blocks = None):
    global test_version_changed
    global patch_version_changed
    if test_version_changed == True & patch_version_changed == True:
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': both_filters_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
    elif test_version_changed == True:
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': test_filter_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
    elif patch_version_changed == True:
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': patch_filter_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
    test_version_changed = False
    patch_version_changed = False

def mainLogic():
    if test_version_changed == True:
        update_test_filter()
        
        print("updated test filter")
    else:
        print("patch version not changed")

    if patch_version_changed == True:
        update_patch_filter()
        print("updated patch filter")
    else:
        print("test filter not changed")

#Function calls
set_version_numbers()
post_message_to_slack('testing')
