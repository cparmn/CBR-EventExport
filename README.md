# CBR-EventExport

More information on cbapi can be found [Here](https://cbapi.readthedocs.io/en/latest/ "CBAPI Read the docs") 

To get started you’ll want to [install CBAPI](https://cbapi.readthedocs.io/en/latest/installation.html "install guide").  Then you will want to setup your [authentication](https://cbapi.readthedocs.io/en/latest/getting-started.html#api-authentication "Authentication"). 
Now you’re off to running querying Carbon Black.  

I’ve written a quick script that will export all the events for a specific search query, please note that if you don’t put a time frame in it will search all events. 

The CSV file is delimited with a # if you run into any issues it can be changed on line 11.  Make you remove all other delimiters when opening the file

**_WARNING_**
**IF YOU DONT SPECIFY A TIME FRAME IT WILL SEARCH ALL MOUNTED PARTITATIONS**
```
$python EventExport.py 
Enter Carbon Black Proces Query:process_name:powershell.exe start:-60m
Enter FileName:powershell-60m.csv

```
