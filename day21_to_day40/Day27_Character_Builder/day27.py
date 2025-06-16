import os, time, random

def healthstat():

    sideroll = random.randint(1,6)
    sideroll2 = random.randint(1,12)
    health = sideroll*sideroll2/2 + 10
    if health <= 18:
        print("HEALTH: " ,"\033[31m" ,health, "\033[0m")
    elif health >= 30:
        print("HEALTH: ", "\033[32m", health, "\033[0m")
    else:
        print("HEALTH: ", "\033[33m", health, "\033[0m")



def strength():
    sideroll3 = random.randint(1, 6)
    sideroll4 = random.randint(1, 8)
    strength = sideroll3 * sideroll4 / 2 + 12
    if strength <= 18:
        print("STRENGTH: " ,"\033[31m" ,strength, "\033[0m")
    elif strength >= 30:
        print("STRENGTH: ", "\033[32m",strength, "\033[0m")
    else:
        print("STRENGTH: ", "\033[33m", strength, "\033[0m")


while True:
    print("\033[34m" "CHARACTER BUILDER" "\033[0m")
    print()
    print()
    print("Name your legend: ")
    name = input()
    print("Character Type (Human, Elf, Wizard, Orc): ")
    character = input()
    print()
    time.sleep(1)
    print("\033[35m",name, "\033[0m")
    healthstat()
    strength()
    print("May your name go down in legend...")
    print()
    again = input("Again?: ")
    if again == "no":
        break
    else:
        time.sleep(1)
        os.system("cls")
