# lazy-programmer
Automated cronjobs

## Remove Desktop clutter automatically every Monday.
datadump.py : This file pushes data files on your desktop and pushes it into a new directory like Mar2017 

## Organize the downloads folder into extension based directory structure
organizeDownloads.py: This script takes all the files that are not folder and puts them into a extension directory. For Example: abc.avi will go in avi folder. The avi folder will be created if not exists

## To run this put this in the crontab File:

24 21 * * 1 python ~/cronscripts/datadump.py
17 21 * * 4 python ~/cronscripts/organizeDownloads.py

This will run the first script on every Monday 21:24 
and Second script on Thursday 21:17 
