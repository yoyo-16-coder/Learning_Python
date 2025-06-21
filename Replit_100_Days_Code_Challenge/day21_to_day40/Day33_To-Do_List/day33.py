print()
print("ALEXA TO DO LIST MANAGER ")
print()

import os, time

ToDoList = []
count = 0

def printlist():
  index =1
  for addremove in ToDoList:
    print(f"\033[32m {index}.{addremove} \033[0m", sep=" ")
    index = index + 1

def cc(color):
  if color == "Black":
        return("\033[30m")
  elif color == "Red":
        return("\033[31m")
  elif color == "Green":
        return("\033[32m")
  elif color == "Yellow":
        return("\033[33m")
  elif color == "Blue":
        return("\033[34m")
  elif color == "Magenta":
        return("\033[35m")
  elif color == "Cyan":
        return("\033[36m")
  elif color == "White":
        return("\033[37m")
  else:
        return("\033[39m")

while True:
    print()
    dowhat = input("Do you want to view, add or edit the to do list? ")
    if dowhat == "view":
        os.system("clear")
        time.sleep(1)
        title = f"{cc('Blue')}To Do List""\033[0m"
        print(f"                                \t{title: ^100}")
        print()
        if count == 0:
            print("Your to-do list is empty.")
        else:
            printlist()
        time.sleep(7)
        os.system("clear")
    elif dowhat == "add":
        print("What do you want to add? ")
        addremove = input()
        ToDoList.append(addremove)
        print()
        print(f"{addremove} was successfully added your list.")
        time.sleep(5)
        os.system("clear")

    elif dowhat == "edit":
        print("What do you want to remove? ")
        addremove = input()
        if addremove in ToDoList:
            ToDoList.remove(addremove)
            print(f"{addremove} was successfully removed from your list.")
        else:
            print(f"{addremove} doesn't exist in your list.")
        time.sleep(5)
        os.system("clear")
