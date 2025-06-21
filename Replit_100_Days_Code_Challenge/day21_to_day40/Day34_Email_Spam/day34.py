print()
import os, time
List = []
print("SPAMMER Inc.")

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

def prettyprinting():
    print(f"{cc('Cyan'): ^100}List of Emails \033[0m")
    for index in range(len(List)):
        print(f"{index+1}. {List[index]}")
    time.sleep(3)

def spammingmssg():
    for index in range(len(List)):
        print(f"{cc('Red')}Email: {index+1}\n\n \033[0mDear {List[index]},\n It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away.If you don't we will pass on your email adress to every spammer we've ever encountered and also sign you to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n\n Love and hugs, \n\n Yoshita")
        print()
        time.sleep(5)
        os.system("clear")
        if index == 9:
            break

while True:
    time.sleep(2)
    os.system("clear")
    print()
    print(f"Enter a number to:\n 1. Add email\n 2. Remove email\n 3. Show emails\n 4.Get SPAMMING")
    dowhat = input()
    if dowhat == "1":
        addremove = input("Email- ")
        if addremove in List:
            print("Email already exists in list.")
        else:
            List.append(addremove)
            print("Email was successfully added.")
    elif dowhat == "2":
        addremove = input("Email- ")
        if addremove in List:
            List.remove(addremove)
            print("Email was successfully removed.")
        else:
            print("Email was not found in the list.")
    elif dowhat == "3":
        prettyprinting()
    elif dowhat == "4":
            spammingmssg()
    else:
        print("Please chose between 1,2,3 and 4")
        continue



