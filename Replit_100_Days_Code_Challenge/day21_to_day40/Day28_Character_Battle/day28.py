import os, time, random

def rolldice(sides):
    animals = random.randint(1, sides)
    return animals


def healthstat():
    health = rolldice(6)*rolldice(12)/2 + 10
    if 18 >= health >= 0:
        print("HEALTH: " ,"\033[31m" ,health, "\033[0m")
    elif health >= 30:
        print("HEALTH: ", "\033[32m", health, "\033[0m")
    elif health <= 0:
        print("STRENGTH: ", "\033[30m", strength, "\033[0m")
    else:
        print("HEALTH: ", "\033[33m", health, "\033[0m")
    return health

def strength():
    strength = rolldice(6) * rolldice(8) / 2 + 12
    if 18 >= strength >= 0:
        print("STRENGTH: " ,"\033[31m" ,strength, "\033[0m")
    elif strength >= 30:
        print("STRENGTH: ", "\033[32m",strength, "\033[0m")
    elif strength <= 0:
        print("STRENGTH: ", "\033[30m", strength, "\033[0m")
    else:
        print("STRENGTH: ", "\033[33m", strength, "\033[0m")
    return strength

    

print("\033[35m""BATTLE TIME!""\033[0m")
print()
while True:
    print("Name your legend: ")
    print()
    name1 = input()
    print("Character Type (Human, Elf, Wizard, Orc): ")
    character1 = input()
    print()
    print("\033[35m", name1, "\033[0m")
    health1 = healthstat()
    print()
    print("Who are they battling?")
    print()
    time.sleep(1)
    print("Name your legend: ")
    name2 = input()
    print("Character Type (Human, Elf, Wizard, Orc): ")
    character2 = input()
    print()
    print("\033[35m", name2, "\033[0m")
    health2 = healthstat()
    print()
    time.sleep(5)
    os.system("clear")
    count = 1
        
    while health1 > 0 and health2 > 0:
        time.sleep(7)
        os.system("clear")
        print("\033[35m""BATTLE TIME!""\033[0m")
        print()
        print("\033[35m""Round" ,count, "!""\033[0m")
        print()
        print("\033[34m",name1,"\033[0m")
        strength1 = strength()
        print()
        print("\033[34m",name2,"\033[0m")
        strength2 = strength()
        if strength1 > strength2:
            time.sleep(1)
            print()
            print("\033[36m" ,name1, "wins round" ,count,".") 
            print(name2, "takes a hit, with" ,strength1 - strength2, "damage.""\033[0m")
            count = count + 1
            print()
            time.sleep(1)
            print("\033[34m",name1,"\033[0m")
            print("HEALTH: ", health1)
            print()
            time.sleep(1)
            print("\033[34m",name2,"\033[0m")
            print("HEALTH: ", health2 - (strength1 - strength2))
            health2 = health2 - (strength1 - strength2)
            print()
        elif strength1 == strength2:
            time.sleep(1)
            print()
            print("That's a tie! Score remains same.")
            print()
            time.sleep(1)
            print("\033[34m",name1,"\033[0m")
            print("HEALTH: ", health1)
            print()
            time.sleep(1)
            print("\033[34m",name2,"\033[0m")
            print("HEALTH: ", health2)
            print()
        else:
            time.sleep(1)
            print()
            print("\033[36m" ,name2, "wins round" ,count,".") 
            print(name1, "takes a hit, with" ,strength2 - strength1, "damage.""\033[0m")
            count = count + 1
            print()
            time.sleep(1)
            print("\033[34m",name1,"\033[0m")
            print("HEALTH: ", health1 - (strength2 - strength1))
            time.sleep(1)
            print()
            print("\033[34m",name2,"\033[0m")
            print("HEALTH: ", health2)
            health1 = health1 - (strength2 - strength1)
            print()
        
    if health1 > health2 : 
        print()
        print("\033[36m" ,name1, "destroyed" ,name2, "in" ,count, "rounds! Want to play again?""\033[0m")
        rematch = input()
    elif health1 < health2 :
        print()
        print("\033[36m" ,name2, "destroyed" ,name1, "in" ,count - 1, "rounds! Want to play again?""\033[0m")
        rematch = input()
    else: 
        print()
        print("It's a tie! Want a rematch?")
        rematch = input()
    if rematch == "yes":
        os.system("clear")
        continue
    elif rematch == "no":
        break
    print("Thanks for playing!")
    exit()
    




