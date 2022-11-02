from jira import JIRA
from pathlib import Path

jira = JIRA('https://anbast.atlassian.net/')

auth_jira = JIRA(basic_auth=('jj@anbast.com', '7mOZ3JbO241wwaL0Qkk9C155'))

""" data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")
print(patchVersion)
print(testVersion) """