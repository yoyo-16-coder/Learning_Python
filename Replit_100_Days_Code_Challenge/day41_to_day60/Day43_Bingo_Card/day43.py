print()
print("Bingo Card Generator")
print()
import random

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
  return Chosen_One
  

my2DList = [ [rolldice(), rolldice(), rolldice()],
            [rolldice(), rolldice(), rolldice()],
            [rolldice(), rolldice(), rolldice()], ]

for row in my2DList:
  row.sort()

display()


