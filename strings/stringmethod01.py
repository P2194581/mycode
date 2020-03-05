#!usr/bin/env python3

#create small string
lilstring = "alta3 research offers classes on python coding"
newlist = lilstring.split(" ") #this returns a list
print(newlist)

#create list of strings
myiplist = ["192", "168", "0", "12"]
#set singleip as result of join
singleip = ".".join(myiplist)

#display single IP
print(singleip)

