
def cc(color):
  if color == "blue":
    return ("\033[34m")
  elif color == "red":
    return ("\033[31m")
  elif color == "magenta":
    return("\033[35m")

print()
print(f"{cc('magenta')}MOKEBEAST" "\033[0m")
print()

Name = input("Beast name: ").strip().capitalize()
Type = input("Type: ").strip().capitalize()

SpecialM = input("Special Move: ").strip().capitalize()
HP = int(input("HP: "))
MP = int(input("MP: "))
print()

info = {"Name": Name, "Type": Type, "Special M": SpecialM, "HP": HP, "MP": MP}
for name, values in info.items():
  if Type == "Water":
    cc("blue")
    print(f"{cc('blue')} {name}: {values}")
  elif Type == "Fire":
    cc("red")
    print(f"{cc('red')} {name}: {values}")
  else:
    print(f"{name}: {values}")
