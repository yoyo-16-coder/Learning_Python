print("Number Guessing Game")
print()
print("Pick a number between 1 to 100")
import random
number = random.randint(1,100)
ask = ""
count = 0
while ask != number:
    ask = int(input("What is your guess?"))
    if ask > 100:
        print()
        print("Please pick a number between 1 to 100 only")
        continue
    if ask > number:
        print("Too high")
        count = count + 1
        if count == 5:
            print("You lose. The number was", number)
            tryAgain = input("Do you want to try again?")
            if tryAgain == "yes":
                count = 0
                number = random.randint(1,100)
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
                number = random.randint(1,100)
                continue
            else:
                print("Thanks for visiting!")
                exit()
    elif ask == number:
        count = count + 1
        print("It took you only", count, "guesses to get it correct!")
        tryAgain = input("Do you want to play again?")
        if tryAgain == "yes":
            count = 0
            number = random.randint(1,100)
            continue
        else: 
            print("Thanks for visiting!")
            exit()
    else:
        break
    
