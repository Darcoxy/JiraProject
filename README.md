# JiraProject
An over-engineered way to get version numbers from .exe files on a virtual machine and then update Jira filters with those version numbers before sending a Slack message with the updated filter links. 

Things I learned:

1. Encoding in Python 3 changed and it was hard to find right anwsers for how Python encodes strings. 
2. I cannot just point at a powershell script and set the task scheduler to run it. I need to the task scheduler to run powershell and pass the file as an argument. 
3. First full project with Git. Learned about pushes, pulls, clones, branches etc.

Things I need to read up about:
1. Encoding. I need to actually learn how Python handles encoding. I had .txt files that had weird utf-8 encodings and Python kept reading the beginning characters. 
