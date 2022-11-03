import requests
import json

slack_token = 'xoxb-194855553623-4340538178368-rXkrkGz0idMwUVqBBhMD5cUZ'
slack_channel = '#testerskie_ploty'

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