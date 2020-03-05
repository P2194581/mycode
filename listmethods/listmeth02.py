#!/usr/bin/env pythong3
        proto = ["ssh", "http", "https"]
        protoa = ["ssh", "http", "https"]
        print(proto)
        proto.append("dns") #this line adds "dns" to the end of our list
        protoa.append("dns") #this line adds "dns" to the end of our list
        print (proto)
        proto2 = [22 , 80, 443, 53] #list of commmon port #s
        proto.extend(proto2) #pass proto2 as argument to end method print proto
        protoa.append(proto2) # pass proto2 as argument to the append method print (protoa)i
