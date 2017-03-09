# If the month changes it will create new folder called : Monthly_DUMP_MonthName_Yr and push all files into it
# this script runs on every Monday 9:00 PM and creates a Folder in Monthly Folder on Desktop Saying : Weekly_DUMP_$DATE

import os
import datetime
import subprocess
now = datetime.date.today()


mfolder ="DataDump_"+now.strftime("%B")+"_"+str(now.year)
print mfolder


direct_output = subprocess.check_output('ls ~/Desktop/', shell=True)

deskfiles = [x for x in direct_output.split("\n") if x!=""]

if mfolder not in deskfiles:
    os.system("mkdir ~/Desktop/"+mfolder)

targetdict = "~/Desktop/"+mfolder+"/"+str(now)
os.system("mkdir " + targetdict)

for filename in deskfiles:
    if "DataDump_" not in filename and "GDC Data Prep" not in filename:
        os.system('mv ~/Desktop/"'+ filename + '" ' + targetdict)