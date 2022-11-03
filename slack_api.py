import requests
import json
import os

slack_token = os.getenv('SLACKAPITOKEN')
slack_channel = '#testing_bot'

def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': 'Nowe bugi weszły w nowej wersji',
        'username': 'JiraUpdateTestingQueues',
        'blocks': json.dumps(blocks) if blocks else None
    }).json()


slack_info = 'testing'
post_message_to_slack(slack_info)