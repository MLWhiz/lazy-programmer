# This script goes to the download folder and create folders if they don't already exist using the file extensions
# Pushes the files in the folder with file extensions
# Leaves folders as it is

import os
import datetime
import subprocess

now = datetime.date.today()

direct_output = subprocess.check_output('ls -p ~/Downloads/| grep -v /', shell=True)

deskfiles = [x for x in direct_output.split("\n") if x!="" and "." in x]
extensions = list(set([x.split(".")[-1] for x in deskfiles]))

for extension in extensions:
    os.system("mkdir ~/Downloads/"+extension)

for filename in deskfiles:
	extension = filename.split(".")[-1]
	targetdict = "~/Downloads/"+extension
    os.system('mv ~/Downloads/"'+ filename + '" ' + targetdict)