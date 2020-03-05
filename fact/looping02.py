#!/usr/bin/env python3
#open file in read
dnsfile = open("dnsservers.txt", "r")
dnslist = dnsfile.readlines()
for svr in dnslist:
    print(svr, end="")
dnsfile.close()


