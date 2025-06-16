print()
print("EPIC ROCK PAPER AND SCISSORS BATTLE")
print()
p1 = input("Player 1's name: ")
p2 = input("Player 2's name: ")
print()
print("""Select your move. Type:"
      S for Scissors
      P for Paper
      R for Rock""")
print()

count1 = 0
count2 = 0
while True :
    move1 = input(p1 + " 's move: ")
    move2 = input(p2 + " 's move: ")
    if move1 == "R" and move2 == "S":
        print(p1, "'s rock smashes " ,p2, "'s scissors!")
        count1 = count1 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif  move1 == "R" and move2 == "P":
        print(p1, "'s rock is smothered by " ,p2, "'s paper!")
        count2 = count2 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif  move1 == "S" and move2 == "P":
        print(p1, "'s scissors slices through " ,p2, "'s paper!")
        count1 = count1 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif move1 == "S" and move2 == "R":
        print(p2, "'s rock smashes " ,p1, "'s scissors!")
        count2 = count2 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif  move1 == "P" and move2 == "R":
        print(p2, "'s rock is smothered by " ,p1, "'s paper!")
        count1 = count1 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif  move1 == "P" and move2 == "S":
        print(p2, "'s scissors slices through " ,p1, "'s paper!")
        count2 = count2 + 1
        print(p1, "=" ,count1, "and" ,p2, "=" ,count2)
    elif move1 == move2:
        print("Woops! That's a tie!")
        continue
    else:
        print("Invalid input. Try again.")
        continue
    if count1 == 3 or count2 == 3:
        print("Well done!")
        if count1 > count2:
            print(p1, "won by", count1 - count2, "points.")
        else:
            print(p2, "won by", count2 - count1, "points.")
        playAgain = input("Do you want to play again?")
        if playAgain == "yes":
            count1 = 0
            count2 = 0
            continue
        else: break
print("Thanks for visiting")
exit()







