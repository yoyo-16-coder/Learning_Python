import time, os
print()

p1 = input("Player 1's name: ")
p2 = input("Player 2's name: ")
score = {p1 :0, p2: 0}

def display():
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
  print("---+---+---")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
  print("---+---+---")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

board = []
for m in range(3):
  row = [" ", " ", " "]
  board.append(row)


def main(player, symbol): # main game
    global board
    while True:
      display() 
      i = int(input(f"{player}'s {symbol} in row: "))
      j = int(input(f"{player}'s {symbol} in column: "))
      if board[i-1][j-1] == " ":
        board[i-1][j-1] = symbol
        print()
        game_over(player, symbol)
        time.sleep(0.5)
        os.system("clear")
        break
      else:
        print()
        print("Sorry that place is already taken. Please choose another one.")
        time.sleep(1)
        os.system("clear")
        continue


def playAgain(): # play again
  global board
  playAgain = input("Do you want to play again? ").strip().lower()
  if playAgain == "no":
    exit()
  elif playAgain == "yes": 
    os.system("clear")
    print()
    board = [[" " for _ in range(3)] for _ in range(3)]


def scoreboard(score): # score board function
  print(f"{p1}: {score[p1]} | {p2}: {score[p2]}")

def trash(player):
  display()
  print()
  score[player] += 1
  print(f"{player} wins this round!")
  print()
  scoreboard(score)
  return playAgain()


def game_over(player, symbol): # game over/win conditions
  for i in range(len(board)):
    if all(cell == symbol for cell in board[i]):
      trash(player)
  for j in range(3):
    if all(board[i][j] == symbol for i in range(3)):
      trash(player)
  if all(board[i][i] == symbol for i in range(3)):
    trash(player)
  elif all(board[i][2-i] == symbol for i in range(3)):
    trash(player)
  elif all(cell != " " for row in board for cell in row):
    display()
    print()
    print(f"It's a tie!")
    print()
    scoreboard(score)
    return playAgain()

while True: # loop for the main game
  main(p1, "X")
  main(p2, "O")