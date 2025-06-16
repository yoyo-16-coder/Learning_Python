print()
print("INFINITY DICE")
print()
n = int(input("How many sides?"))
import random
num = random.randint(1, n)
print("You rolled", num)
print()
again = input("Roll again?")
if again == "no":
  print()
  print("Thanks for visiting.")

def rolldice(again):
  print()
  n = int(input("How many sides?"))
  import random
  num = random.randint(1, n)
  print("You rolled", num)
  print()
  again = input("Roll again?")
  while again == "restart":
    import random
    num = random.randint(1, n)
    print("You rolled", num)
    print()
    again = input("Roll again?")
    if again == "no":
      print()
      print("Thanks for visiting")
      exit()
    elif again == "yes":
      continue
    else:
      print()
      print("Invalid value. Please try again.")
      continue
  while again == "yes":
    import random
    num = random.randint(1, n)
    print("You rolled", num)
    print()
    again = input("Roll again?")
    if again == "no":
      print()
      print("Thanks for visiting")
      exit()
    elif again == "yes":
      continue
    elif again == "restart":
      break
    else:
      print()
      print("Invalid value. Please try again")
      continue
  if again != "no":
    print("Sorry wrong input. Please try again")
    rolldice(again)
  else :
    print("Thanks for visiting")
    exit()
  rolldice(again)


while again == "yes":
  import random
  num = random.randint(1, n)
  print("You rolled", num)
  print()
  again = input("Roll again?")

  if again == "restart":
    rolldice(again)
  elif again == "no":
    print()
    print("Thanks for visiting")
    exit()
  elif  again == "yes":
    continue
  else:
    print()
    print("Invalid value. Please try again")
    rolldice(again)

if again == "yes":
  rolldice(again)
else:
  print("Sorry wrong input. Please try again.")
  rolldice(again)








