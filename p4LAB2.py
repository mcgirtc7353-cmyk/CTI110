#Cedric McGirt
#P4LAB2
#3/25/2026
# testint knowledge of using loops and interger 

while True:
  num = int(input("Enter a positive integer: "))
# only positive numbers 
if num <= 0:
    print("please enter a positive interger only.")

# multiplication table using for loop
else:
    for i in range(1, 13):
        print(f"{num} * {i} = {num * i}")


choice = input("\nWould you like to run the program again? ")


if choice != "yes":
        print("Exiting program...") 
