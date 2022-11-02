import os
from jira import JIRA
from ssl import Options
from pathlib import Path

Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

jira = JIRA(options=Options, basic_auth=('jj@anbast.com', os.environ.get("JIRAAPITOKEN")))

#This will read the html file with version numbers and then split them to seperate 
#environments version numbers 
data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")

#This will make the JQL react to changes to versions of PurGo
testJQL = 'project = PUR AND fixVersion >= 1.65.0 and fixVersion <=' + testVersion
patchJQL = 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <=' + patchVersion

testJQL.join(testVersion)
patchJQL.join(patchVersion)

#This will remove unicode from the string so that JQL likes it
patchJQL = patchJQL.replace('\u0000', '').rstrip()
testJQL = testJQL.replace('\u0000', '').rstrip()

#This will update the Jira filters 
updatePatchFilter = jira.update_filter(19012, 'JiraProjectPatchQueue', 'Updated Patch Queue with Script', patchJQL[:-2])
updateTestFilter = jira.update_filter(19013, 'JiraProjectTestQueue', 'Updated Test Queue with Script', testJQL[:-2])