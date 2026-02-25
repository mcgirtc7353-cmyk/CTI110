#Cedric McGirt
#2/25/2026
#P3LAb
#This programe allows the usere to enter a money (float) value with two places after the decimal 

#Get user input 
amount = float(input("Enter the amount of money as a float: $"))

# convert to cent to avoid floating point precision issues 
cents = round(amount * 100)

if cents == 0:
    print("No change")

#calculate each denomination 
dollars = cents // 100 
cents %= 100

quarters = cents // 25
cents %= 25 

dimes = cents //10 
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents 

#print results (Only if grater than 0)
if dollars > 0: 
    print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
if quarters > 0: 
    print (f"{quarters} Quarter{'s' if quarters > 1 else ''}") 
if dimes > 0:
    print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
if nickels > 0:
    print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
if pennies > 0:
    print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")        