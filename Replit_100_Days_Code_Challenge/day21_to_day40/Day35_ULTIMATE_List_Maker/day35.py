print()
import os, time
List = []
def prettyprinting():
    print()
    print(f"{cc('Blue'): ^90} Your To-Do List \033[0m")
    for index in range(len(List)):
        print(f"{index+1}. {List[index]}")

def cc(color):
    if color == "Blue":
        return("\033[34m")

def editing(i):
    print()
    print("What would you like to change it into?")
    change = input()
    List[i] = change
    print()
    print(f"{i+1} item was successfully changed to {change}.")

while True:
    time.sleep(2)
    os.system("clear")
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
            print(f"Are you sure you want to remove {change} from your list?")
            confirm = input()
            if confirm == "yes":
                List.remove(change)
                print(f"{change} was successfully removed from your list.")
            else:
                continue
        else:
            print(f"{change} was not found in the list.")
    elif dowhat == "view":
        prettyprinting()
        time.sleep(2)
    elif dowhat == "edit":
        print()
        print("What item do you want to change? Please write the index no.")
        indexno = int(input())
        if 0 < indexno < (len(List)+1):
            x = editing (indexno-1)
            print(x)
        else:
            print(f"Index no.{indexno} not in list.")














