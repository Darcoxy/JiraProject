[System.Diagnostics.FileVersionInfo]::GetVersionInfo("F:\Purgo\Patch\App\Purgo.exe").FileVersion | Out-File -FilePath C:\Users\JJ.VWSSOFTWARE\Desktop\JiraProject\index.txt
$breakLine = ',' | Out-File -Append -FilePath C:\Users\JJ.VWSSOFTWARE\Desktop\JiraProject\index.html
[System.Diagnostics.FileVersionInfo]::GetVersionInfo("F:\Purgo\Test\App\Purgo.exe").FileVersion | Out-File -Append -FilePath C:\Users\JJ.VWSSOFTWARE\Desktop\JiraProject\index.txt
