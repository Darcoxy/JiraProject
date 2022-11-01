from jira import JIRA 

jira = JIRA('https://jira.atlassian.com')

issue = jira.issue('PUR-123')
print(issue.fields.project.key)
print(issue.fields.issuetype.name)
print(issue.fields.reporter.displayName)