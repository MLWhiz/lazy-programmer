# lazy-programmer
Automated cronjobs

# Remove Desktop clutter automatically every Monday.
datadump.py

# Organize the downloads folder into extension based directory structure
organizeDownloads.py

# To run this put this in the crontab File:

24 21 * * 1 python ~/cronscripts/datadump.py
17 21 * * 4 python ~/cronscripts/organizeDownloads.py
