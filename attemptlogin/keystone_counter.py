#!usr/bin/env python3
#parse keystone and return number of failed login attempts
loginfail = 0 #counter for fails
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") 
keystone_file_lines=keystone_file.readlines()
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("the number of failed login attempts is: ", loginfail)
keystone_file.close()

