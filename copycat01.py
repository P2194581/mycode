#!/usr/bin/env python3
#imports
import shutil
import os
#move to working dir
os.chdir("/home/student/mycode/")
#copy filea to fileb
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy dira to dirb
shutil.copytree("5g_research/", "5g_research_backup/")




