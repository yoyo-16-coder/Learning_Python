print("ANIMAL SOUND GENERATOR")
print()
while quit != "yes":
    print()
    print("What animal do you want?")
    animal = input()
    if animal == "cow":
        print("A cow goes moo.")
    elif animal == "lesser spotted lemur":
        print("Ummm... the lesser spotted lemur goes Awooga?")
    else:
        print("Sorry I don't know that animal.")

    print()
    quit = input("Do you want to exit? Type 'yes' or 'no'.")
