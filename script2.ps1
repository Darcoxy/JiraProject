git checkout main

git add index.html

$date = Get-Date -Format "dd/MM/yyyy HH:mm"

git commit -m 'script2.ps1 made changes on:' -m $date

git push