print()
print("Math Game")
print()
n = int(input("Name your multiples: "))
count = 0
for i in range(0,10):
    q = n, 'x' ,i+1,'='
    ans = int(input(q))
    i = i + 1
    if ans == i*n:
        print("Well done!")
        count = count + 1
        continue
    elif i == 10:
        break
    else: print("Nope! The answer was" ,i*n)
print("You scored" ,count, "points!")
