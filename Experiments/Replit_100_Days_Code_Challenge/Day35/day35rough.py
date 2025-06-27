print()
import os, time
List = []
def prettyprinting():
    print()
    print(f"{cc('Blue'): ^90} Your To-Do List \033[0m")
    for index in range(len(List)):
        print(f"{index+1}. {List[index]}")

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
    time.sleep(2)
    os.system("cls")
    print()
    print("Do you want to view, add or remove or edit the to do list?")
    dowhat = input()
    if dowhat == "add":
        print("What would you like to add?")
        change = input()
        print()
        if change in List:
            print(f"{change} already exists in the list.")
        else:
            List.append(change)
            print(f"{change} was successfully added to your list.")
    elif dowhat == "remove":
        print("What would you like to remove?")
        change = input()
        print()
        if change in List:
            List.append(change)
            print(f"{change} was successfully removed from your list.")
        else:
            print(f"{change} was not found in the list.")
    elif dowhat == "view":
        prettyprinting()
    elif dowhat == "edit":
        print()
        for i in range(1, len(List)+1):
            print("What item do you want to change? Please write the index no.")
            io = int(input())
            for i in range(len(List)):
                print(i)
                print("What would you like to change it into?")
                change = input()
                List[i] = change
                print(f"{i+1} item was successfully changed to {change}.")
                break
            break


        prettyprinting()







