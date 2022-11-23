# JiraProject
An over-engineered way to get version numbers from .exe files on a virtual machine and then update Jira filters with those version numbers before sending a Slack message with the updated filter links. 

# How it works
On a remote computer, a powershell script (script.ps1) checks version numbers of PurGo.exe for Test and Patch environments. This happens every day, every 15 minutes betweeen 8:00 AM and 8:00 PM. It stores the version numbers in index.txt. Every 15 minutes a script (script2.ps1) tries to commit and push that file to the repository. Then on another machine where python is installed, another script (script4.ps1) pulls from the repo every 15 minutes and runs the main.py file which:
    Checks if a version has changed.
        If it has:
            It will update Jira filters and send a slack message to a channel with an updated filter.
        If it has not:
            It will not do anything.

Things I learned:

1. Encoding in Python 3 changed and it was hard to find right anwsers for how Python encodes strings. 
2. I cannot just point at a powershell script and set the task scheduler to run it. I need to the task scheduler to run powershell and pass the file as an argument. 
3. First full project with Git. Learned about pushes, pulls, clones, branches etc.

Things I need to read up about:
1. Encoding. I need to actually learn how Python handles encoding. I had .txt files that had weird utf-8 encodings and Python kept reading the beginning characters. 
