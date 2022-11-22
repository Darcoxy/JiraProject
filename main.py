import os
import json
import sys
import requests
from jira import JIRA
from jira import JIRAError
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
errors_updating_test_filter = False
errors_updating_patch_filter = False

#This is a required dictionary for Jira to know where to connect and to know to verify
Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

#This will read the patch version number and return it
def get_patch_version_number():
    data = Path("index.txt").read_text(encoding='utf-16 LE')
    output = data
    patchVersion = output.split(',')[0].rstrip()
    return(patchVersion[1:])

#This will read the test version number and return it
def get_test_version_number():
    data = Path("index.txt").read_text(encoding='utf-16 LE')
    output = data
    testVersion = output.split(',')[1].replace(" ", "")
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
    global errors_updating_patch_filter

    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    patchJQL = 'project = PUR AND status = testing AND fixVersion >= 1.61.0 and fixVersion <=' + get_patch_version_number()
    patchJQL.join(get_patch_version_number())
    patchJQL = patchJQL.replace('\u0000', '').rstrip()
    try:
        updatePatchFilter = jira.update_filter(19012, 'JiraProjectPatchQueue', 'Updated Patch Queue with Script', patchJQL[:-2])
    except JIRAError as e:
        blocks = None
        requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': 'Error whilst updating Patch filter! ' + e.text,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
        errors_updating_patch_filter = True

#This will update the test filter
def update_test_filter():
    global errors_updating_test_filter

    jira = JIRA(options=Options, basic_auth=('jj@anbast.com', jira_token))
    testJQL = 'project = PUR AND status = testing AND fixVersion >= 1.65.0 and fixVersion <=' + get_test_version_number()
    testJQL.join(get_test_version_number())
    testJQL = testJQL.replace('\u0000', '').rstrip()
    try:
        updateTestFilter = jira.update_filter(19013, 'JiraProjectTestQueue', 'Updated Test Queue with Script', testJQL[:-2])

    except JIRAError as e:
        blocks = None
        requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': 'Error whilst updating Test fiter! ' + e.text,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
        errors_updating_test_filter = True

#This will post a message to slack
def post_message_to_slack(text, blocks = None):
    global test_version_changed
    global patch_version_changed
    global errors_updating_patch_filter
    global errors_updating_test_filter

    if test_version_changed and patch_version_changed and errors_updating_test_filter == False and errors_updating_patch_filter == False:
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': both_filters_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
    elif test_version_changed and errors_updating_test_filter != True:
        return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': test_filter_url,
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()
    elif patch_version_changed and errors_updating_patch_filter != True:
        if errors_updating_patch_filter:
            pass
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
    # if errors_updating_test_filter:
    #     print('Errors updating test filter')
    # elif errors_updating_patch_filter:
    #     print('Errors updating patch filter!')

    if test_version_changed == True:
        update_test_filter()
        if errors_updating_test_filter:
            print('Errors updating_test_filter')
        else:
            print("updated test filter")
    else:
        print("patch version not changed")

    if patch_version_changed == True:
        update_patch_filter()
        if errors_updating_patch_filter:
            print('Errors updating patch filter')
        else:
            print("updated patch filter")
    else:
        print("test filter not changed")

#Function calls
set_version_numbers()
mainLogic()
if errors_updating_patch_filter and errors_updating_test_filter:
    sys.exit(1)
else:
    post_message_to_slack('testing')
