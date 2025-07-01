print()
print("Bingo Card Generator")
print()
import random, time, os

listOfNumbers = list(range(1,91))


def display():
  print(f"{my2DList[0][0]}  | {my2DList[0][1]}  | {my2DList[0][2]}")
  print("----+-----+----")
  print(f"{my2DList[1][0]}  |BINGO| {my2DList[1][2]}")
  print("----+-----+----")
  print(f"{my2DList[2][0]}  | {my2DList[2][1]}  | {my2DList[2][2]}")




def rolldice():
  Chosen_One = random.choice(listOfNumbers)
  listOfNumbers.remove(Chosen_One)
  my2DList.append
  return Chosen_One


my2DList = []
for _ in range(3):
  row = [rolldice(), rolldice(), rolldice()]
  row.sort()
  my2DList.append(row)



X = 0
while X < 8:
  display()
  print()
  number = int(input("What number was called? "))
  for i in range(len(my2DList)):
    for j in range(len(my2DList[i])):
      if my2DList[i][j] == number:
        my2DList[i][j] = "X"
        X += 1
    time.sleep(1)
    os.system("clear")



print()
print("You WON!")

