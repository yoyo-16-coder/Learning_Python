import time,os
todolist = []

def prettyprint(number):
    if number == 1:
        print()
    row = []
    if all(row not in todolist):
            print("Your To-Do List is empty.")
    else:    
        for row in todolist:
            print("\t")
        for item in row:
            print(f"{item:^10}", end=" | ")
    print()
    return True

def add():
    os.system("clear")
    print()
    print("ADD")
    what = input("What is it? ").strip().capitalize()
    when = input("When is it due? ").strip().capitalize()
    priority = input("How important? ").strip().capitalize()
    row = [what,when,priority]
    if all(what not in row for row in todolist):
        todolist.append(row)
        print()
        print("Added successfully.")
        
    else:
        print(f"{what} already exists in your list. ")
        
def view():
    os.system("clear")
    print("""
        1. View all
        2. View priority""")
    subcat = int(input(">"))
    if subcat == 1:
        prettyprint(1)
    if subcat == 2:
        priorlvl = input("Which Priority(High/Medium/Low)? >").strip().capitalize()
        for row in todolist:
            print("\t")
            for priority in row:
                if priorlvl == priority:
                    for item in row:
                        print(f"{item:^10}", end=" | ")

def remove():
    os.system("clear")
    print("REMOVE")
    print()
    removewhat = input("What do you want to remove? >").strip().capitalize()
    print()
    if all(removewhat not in row for row in todolist):
            print(f"{removewhat} doesn't exist in your list.")
            return
    for row in todolist:
        if removewhat in row[0]:
            todolist.remove(row)
            print(f"{removewhat} successfully removed.")


                

def edit():
    os.system("clear")
    print("EDIT")
    print()
    editwhat = input("What do you want to edit? ").strip().capitalize()
    print()
    if all(editwhat not in row for row in todolist):
            print(f"{editwhat} doesn't exist in your list.")
            return # exit if not found
    for row in todolist:
        if editwhat in row[0]:
            what1 = input("New title: ").strip().capitalize()
            when1 = input("New Due Date: ").strip().capitalize()
            priority1 = input("New Priority: ").strip().capitalize()
            row[0] = what1
            row[1] = when1
            row[2] = priority1
            print()
            print("Updated.")
            return True
    
while True:
    time.sleep(3)
    os.system("clear")
    print()
    print("To Do List Management System")
    print()
    print("""
          1.Add
          2.View
          3.Remove
          4.Edit""")
    dowhat = int(input(">"))
    if dowhat == 1:
        add()
    if dowhat == 2:
        view()
    if dowhat == 3:
        remove()
    if dowhat == 4:
        edit()
                           
                

