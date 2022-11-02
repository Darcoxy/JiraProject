from jira import JIRA
from ssl import Options
from pathlib import Path

Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

jira = JIRA(options=Options, basic_auth=('jj@anbast.com', "EpuTwjVN6Un5g5Au5lOwFAF4"))

filter = jira.filter(19012)
print(filter)

""" data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")
print(patchVersion)
print(testVersion) """