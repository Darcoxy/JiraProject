from jira import JIRA
from ssl import Options
from pathlib import Path

Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

jira = JIRA(options=Options, basic_auth=('jj@anbast.com', "XFe7dhwnufe4oS5TOrls3731"))

data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")

print(testVersion)
print(patchVersion)

testJQL = 'project = PUR AND fixVersion >= 1.65.0 and fixVersion <=' +  testVersion
patchJQL = 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <=' + patchVersion

testSize = len(testJQL)
patchSize = len(patchJQL)

testJQL = testJQL[:testSize - 2]
patchJQL = patchJQL[:patchSize -2]

print(testJQL)
print(patchJQL)
print(testJQL[58])
print(patchJQL[58])

""" updatePatchFilter = jira.update_filter(19012, 'JiraProjectPatchQueue', 'Updated Patch Queue with Script', patchJQL)

updateTestFilter = jira.update_filter(19013, 'JiraProjectTestQueue', 'Updated Test Queue with Script', testJQL) """