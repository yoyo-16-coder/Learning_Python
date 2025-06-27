import time, os
print()
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

p1 = input("Player 1's name: ")
p2 = input("Player 2's name: ")

def display():
  print(f" {board[0]} | {board[1]} | {board[2]} ")
  print("---+---+---")
  print(f" {board[3]} | {board[4]} | {board[5]} ")
  print("---+---+---")
  print(f" {board[6]} | {board[7]} | {board[8]} ")

time.sleep(1)
os.system("clear")

def playAgain():
  playAgain = input("Do you want to play again? ").strip().lower()
  if playAgain == "no":
    exit()
  elif playAgain == "yes": 
    os.system("clear")
    print()
    board[:] = [" " for _ in range(9)]


def check():
  print()
  if board[1] == board[2] and board[2] ==  board[0] and board[0] == board[1] and board[1] != " ":
    if board[2] == "O":
      print(f"{p2} wins!")
    elif board[2] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[3] == board[4] and board[4] ==  board[5] and board[3] == board[5] and board[3] != " ":
    if board[3] == "O":
      print(f"{p2} wins!")
    elif board[3] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[6] == board[7] and board[6] ==  board[8] and board[7] == board[8] and board[6] != " ":
    if board[6] == "O":
      print(f"{p2} wins!")
    elif board[6] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[0] == board[3] and board[0] ==  board[6] and board[3] == board[6] and board[3] != " ":
    if board[3] == "O":
      print(f"{p2} wins!")
    elif board[3] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[1] == board[4] and board[1] ==  board[7] and board[7] == board[4] and board[1] != " ":
    if board[1] == "O":
      print(f"{p2} wins!")
    elif board[1] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[2] == board[5] and board[2] ==  board[8] and board[5] == board[8] and board[2] != " ":
    if board[2] == "O":
      print(f"{p2} wins!")
    elif board[2] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[0] == board[4] and board[4] ==  board[8] and board[0] == board[8] and board[4] != " ":
    if board[4] == "O":
      print(f"{p2} wins!")
    elif board[4] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[2] == board[4] and board[2] ==  board[6] and board[6] == board[4] and board[6] != " ":
    if board[2] == "O":
      print(f"{p2} wins!")
    elif board[2] == "X":
      print(f"{p1} wins!")
    playAgain()
  if board[0] != " " and board[1] != " " and board[2] != " " and board[4] != " " and board[5] != " " and board[6] != " " and board[7] != " " and board[8] != " ":
    print("It's a tie!")
    playAgain()

  
  
while True:
  time.sleep(1)
  os.system("clear")
  p1display = (f"{p1}'s turn")
  print(f"{p1display:^65}")
  print()
  display()
  print()
  whichbox = int(input("Which box would you like to place your X in? "))
  while board[whichbox -1] != " " :
    print()
    print("That place is already taken!")
    print()
    whichbox = int(input("Which box would you like to place your X in? "))
  board[whichbox-1] = "X"
  display()
  print()
  check()
  print()
  time.sleep(1)
  os.system("clear")
  p2display = (f"{p2}'s turn")
  print(f"{p2display:^65}")
  print()
  display()
  print()
  whichbox = int(input("Which box would you like to place your O in? "))
  
  while board[whichbox -1] != " " :
    print()
    print("That place is already taken!")
    print()
    whichbox = int(input("Which box would you like to place your O in? "))
    
  board[whichbox-1] = "O"
  display()
  print()
  check()
  print()


  

    
