import os, time
NameList = []

def prettyprinting():
    print()
    for i in range(len(NameList)):
        print(f"{cc('Green')} {i+1}. {NameList[i]} \033[0m")
def cc(color):
    if color == "Green":
        return("\033[32m")

while True:
    time.sleep(2)
    os.system("clear")
    print()
    firstname = input(f"First name: ").strip().capitalize()
    if firstname == "":
        print()
        print("Sorry, first name can't be empty.")
        continue
    lastname = input(f"Last name: ").strip().capitalize()
    if lastname == "":
        print()
        print("Sorry, last name can't be empty.")
        continue
    jin = f"{firstname} {lastname}"
    if jin in NameList:
        print()
        print(f"ERROR: Duplicate name")
        prettyprinting()
    else:
        NameList.append(jin)
        prettyprinting()
        time.sleep(1)
