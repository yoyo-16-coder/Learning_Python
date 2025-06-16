print("EPIC ROCK PAPER SCISSORS BATTLE")
print()
print("""Select your move. Type:
      R for rock
      P for paper
      S for scissors""")
name1 = input("Player 1's name: ")
name2 = input("Player 2's name: ")
print()
p1 = input("Player 1's move: ")
p2 = input("Player 2's move: ")
if p1 == "R" and p2 == "P":
    print(name1, "'s rock got smothered by" ,name2, "'s paper!")
elif p1 == "R" and p2 == "S":
    print(name1, "'s rock brutually smashed" ,name2, "'s scissors!")
elif p1 == "P" and p2 == "S":
    print(name1, "'s paper got torn into peices by" ,name2, "'s scissors!")
elif p1 == "P" and p2 == "R":
    print(name2, "'s rock got smothered by" ,name1, "'s paper!")
elif p1 == "S" and p2 == "R":
    print(name2, "'s rock brutually smashed" ,name1, "'s scissors!")
elif p1 == "S" and p2 == "P":
    print(name2, "'s paper got torn into peices by" ,name1, "'s scissors!")
elif p1 == p2:
    print("That's a tie! ")
else:
    print()
    print("Invalid input. Please try again.")
