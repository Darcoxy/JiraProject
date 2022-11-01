from jira import JIRA 

jira = JIRA('https://jira.atlassian.com')

issue = jira.issue('SR-1468')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)