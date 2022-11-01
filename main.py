from jira import JIRA

jira = JIRA('https://anbast.atlassian.net/')

auth_jira = JIRA(basic_auth=('jj@anbast.com', 'SUGv050W7U8sbpoi7LyOF7EC'))