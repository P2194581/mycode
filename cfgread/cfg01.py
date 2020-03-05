#!/user/bin/env python3
##exp read####
##create file ojb in "r"ead mode
configfile = open("vlanconfig.cfg", "r")
#display file to screen

print(configfile.read())
#close file
configfile.close()

#exp readlines
#re-create file obj
configfile = open("vlanconfig.cfg","r")

#make a list of file lines -.readlines()
configlist = configfile.readlines()
print(configlist)

#ITERATE THRHOUGH CONFIGLIST
for x in configlist:
    print(x)

#always close file
configfile.close


