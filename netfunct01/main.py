#!/usr/bin/env python3
#"""Alta3 Research || Author: RZFeeser@alta3.com"""

#funct to push commands
def commandpush(devicecmd): #devicecdm==list
    for coffeetime in devicecdm.keys():
       print('handshaking. .. ... connecting with ' + coffeetime)
       #we'll learn to write code that connects to devices here
       for mycmds in devicecmd[coffeetime]:
        print('Attempting to send command --> ' + mycmds)
        # we'll learn to write code taht sends cmds to device here
            
#start main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    print("welcome to the network device command pusher") # welcome
    
    ##get data set
    print("\nData set found\n") #replace w/ function call that reads in data from file
    
    ##run
    commandpush(work2do) # call function to push commands to devices
    
    #call our main funct
main()
