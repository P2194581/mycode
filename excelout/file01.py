#!/user/bin/env python
#sudo apt install python3-pip
#python3 -m pip install pyexcel
#python3 -m pip install pyexcel-xls

import pyexcel
#request user data
def get_ip_data():
    input_ip = input("\nWhat is the ip address?")
    input_driver = input("What is the driver associated w/ this device?")
    input_loc = input("where is this device located?")
    input_age = input("how old is this device?")
    d = {"IP": input_ip, "driver": input_driver, "LOC": input_loc, "AGE": input_age}
    return d

#runtime
mylistdict = [] #this is the list that will become our excel file
print("hello! this program will make you a *.xls file.")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *xls file? ")
pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("the file " + filename + ".xls should be in your local dir")

