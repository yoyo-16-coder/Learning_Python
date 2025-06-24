print()
aplha = ["r","g","b","y","m", " "]
print("What sentence do you want to see rainbow-ising?")
sentence = input()
def cc(color):
  if color == "red":
    return("\033[31m")
  elif color == "green":
    return("\033[32m")
  elif color == "yellow":
    return("\033[33m")
  elif color == "blue":
    return("\033[34m")
  elif color == "magenta":
    return("\033[35m")
  elif color == " ":
    return("\033[0m")


for letter in sentence:
  if letter.lower() in aplha[0]:
    print(f"{cc('red')}" ,end= "")
  elif letter.lower() in aplha[1]:
    print(f"{cc('green')}", end="")
  elif letter.lower() in aplha[2]:
    print(f"{cc('blue')}", end="")
  elif letter.lower() in aplha[3]:
    print(f"{cc('yellow')}", end="")
  elif letter.lower() in aplha[4]:
    print(f"{cc('magenta')}", end="")
  elif letter.lower() in aplha[5]:
    print(f"{cc(' ')}", end="")
  print(letter, end="")
