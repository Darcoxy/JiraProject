from jira import JIRA
from pathlib import Path

jira = JIRA('https://anbast.atlassian.net/')

#auth_jira = JIRA(basic_auth=('jj@anbast.com', 'SUGv050W7U8sbpoi7LyOF7EC'))

data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1]
print(patchVersion)
print(testVersion)