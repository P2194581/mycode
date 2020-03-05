#!usr/bin/env python

msg = "buy a "

salary = float(input("what is your salary (in K)?"))

if salary == 0:
    msg = msg + 'nothing'

elif salary >= 500:
    msg = msg + "lamborghini huracan"
    
elif salary >= 100:
    msg = "porsche 911"

elif salary >= 80:
    msg = "BMW M3"

elif salary > 50:
    msg = "2nd hand R35 GTR"

elif salary <= 50:
    msg = "something boring"

else :
    msg = "invalid input"


print(msg)

