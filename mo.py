print("WLCOME TO LOAN ELIGIBILITY")
age=int(input("Enter your age"))
if(age>=18):
    print("Elgible for loan")
else:
     print("error bcoz your age is less than 18")
Monthly=int(input("Enter your Monthly Income"))
if (Monthly >=20000):
     print("Eligible")
else:
    print("error bcoz your monthly income is less than 20000")
credit=int(input("Enter your Credit score"))
if(credit>700):
    print("eligible")
else:
    print("error")
multiplier=int(input("Enter your credit score to check your multiplier"))
if(credit>=700 and credit==749):
    print("multiplier=5",5*Monthly)
elif(credit>=750 and credit==799):
    print("multiplier=7",7*Monthly)
elif(credit>=800):
    print("multiplier=10",10*Monthly)
else:
    print("error")
status=input("Enter your Employment status")
if(status=='employed'):
    print("your are eligible")
else:
    print("error you are unemployed")
print("eligible for loan")



