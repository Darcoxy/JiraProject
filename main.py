from jira import JIRA
from ssl import Options
from pathlib import Path

Options = {
    'server': 'https://anbast.atlassian.net/',
    'verify': True
}

jira = JIRA(options=Options, basic_auth=('jj@anbast.com', "zRekB4Lcps5uFJaOilZG66C4"))

testFilter = jira.filter(19012)
print(testFilter)

testFilter = jira.update_filter(19012, 'UpdatedJiraFilter', 'Test update python api', 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <= 1.63.77')

#testFilter.update_filter(19012, 'project = PUR AND fixVersion >= 1.61.0 and fixVersion <= 1.63.77')

""" data = Path("index.html").read_text().replace('\n', ' ')
output = data[2:]
patchVersion = output.split('<')[0]
testVersion = output.split('>')[1].replace(" ", "")
 """