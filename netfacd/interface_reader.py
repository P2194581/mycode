#!usr/bin/env python3
import netifaces

print(netifaces.interfaces())
for i in netifaces.interfaces(): 
    print('\n*********details of interface -' + i + '********')
    try:
        raise ValueError
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #print mac
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #print I
    except: 
        print('could not collect adapter info') 

#def MAC
    

#def IP


