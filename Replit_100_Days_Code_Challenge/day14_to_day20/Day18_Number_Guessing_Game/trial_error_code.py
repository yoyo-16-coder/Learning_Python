print("Number Guessing Game")
print()
print("Pick a number between 1 to 100")
import random
number = random.randint(1,100)
ques = ""
count = 0
while ques != number:
    ask = int(input("What is your guess?"))
    if ask > number:
        print("Too high")
        count = count + 1
        if count == 5:
            print("You lose. The number was", number)
            tryAgain = input("Do you want to try again?")
            if tryAgain == "yes":
                count = 0
                continue
            else:
                print("Thanks for visiting!")
                exit()
        else: continue
    elif ask < number and ask > 0:
        print("Too low")
        count = count + 1
        if count == 5:
            print("You lose. The number was", number)
            tryAgain = input("Do you want to try again?")
            if tryAgain == "yes":
                count = 0
                continue
            else:
                print("Thanks for visiting!")
                exit()
    elif ask == number:
        count = count + 1
        break
    else:
        exit()
print("It took you only", count, "guesses to get it correct!")
