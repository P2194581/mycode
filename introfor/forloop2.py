#!/usr/bin/env python3
#list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
#2nd list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
#loop
for x in vendors:
        print("\nThe vendor is " + x, end="")
        if x not in approved_vendors: 
            print(" - not an approved vendor", end="")
print("\nOur loop has ended")

