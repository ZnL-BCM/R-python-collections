#!/usr/bin/env python
# An example mortgage calculator

import time
import re

while True:
    Menu = input("Press 1 to calculate payoff. Press 2 to estimte minimum payment.")
    if Menu=="1":
        print("Please type in your total unpaid loan amounts in dollars.")
        Loan = float(re.findall('\d+\.\d+|\d+',re.sub('\,',"",input()))[0])
        print("Please type in your annual percent rate in percentages. For example, please type in 3.5 if your APR is 3.5%.")
        API = float(re.findall('\d+\.\d+|\d+',re.sub('\,',"",input()))[0])*0.01
        print("Please type in your expected monthly payment.")
        Monthly = float(re.findall('\d+\.\d+|\d+',re.sub('\,',"",input()))[0])
        i = 1
        while True:
            Interest = (Loan - Monthly) * API / 12
            if Monthly <= Interest:
                print("The monthly payment is not enough to pay off the loan! Press enter to exit.")
                input()
                break
            else: 
                Loan = Loan - Monthly + Interest
                if Loan <= 0:
                    print(str("The loan will be paid off in month ")+str(i)+str("."))
                    print("Please see the above calculations. Press enter to exit.")
                    input()
                    break
                else:
                    print(str("This is your payment information for month ")+str(i)+str(": "))
                    print(str("Your interest for this month is $")+str(round(Interest,ndigits=2)))
                    print(str("The remaining balance is $")+str(round(Loan,ndigits=2)))
                    print("\n")
                    i += 1
                    time.sleep(1)
        break

    elif Menu=="2":
        break

    else:
        break
        
