from jira import JIRA
from ssl import Options
from pathlib import Path

Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

jira = JIRA(options=Options, basic_auth=('jj@anbast.com', "1QqfZ5AYASQ9ydwU5J977675"))

filter = jira.filter(18839)
print(filter)
""" issue = jira.issue('PUR-12792')
print(issue.key)
print(issue.fields.summary) """

""" data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")
print(patchVersion)
print(testVersion) """