#!usr/bin/env python3

from subprocess import call
call(["ip", "link", "show", "up"]
print("this program will check your interfaces")
interface = input("enter an interfae, like, ens3: ")
call(["IP", "addr", "show", "dev", "interface"])
call(["IP", "route", "show" ,"dev", "interface"])

