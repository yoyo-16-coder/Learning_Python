print()
print("List Generator")
print()
x = int(input("Start at: "))
y = int(input("End before: "))
z = int(input("Increment between values: "))
for number in range(x, y, z):
     print("\033[34m" ,number)
if  x>y and z >= 0 :
    print("Invalid input. Please enter a negative increment.")
elif x<y and z <= 0:
    print("Invalid input. Please enter a positive increment.")
elif x == y:
    print("Stop messing around bro")
