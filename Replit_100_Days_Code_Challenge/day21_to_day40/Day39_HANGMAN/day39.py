print()
print("HANGMAN")
print()
import random
listOfWords = ["burger", "pastries","steak","cricket","talent","scissors","brush","knife","folklore","badminton" ]

Chosen_One = random.choice(listOfWords)

lettersUsed = []

def editing():
    count = 6
    list = ["_" for _ in Chosen_One]
    lettersUsed = []
    while count > 0 and "_" in list:
        Userletter = input("Choose a letter: ").strip().lower()
        if Userletter not in lettersUsed:
            lettersUsed.append(Userletter)
            if Userletter in Chosen_One: 
                for i in range(len(Chosen_One)):
                    if Chosen_One[i] == Userletter:
                        list[i] = Userletter
                print()
                print(list)
                print()
                print(f"Congrats, you got a letter correct. You have {count} lives left.")

            elif Userletter not in Chosen_One:
                print()
                print(list)
                print()
                count = count - 1
                print(f"Nope, its not there.You have {count} lives left.")

            
        else: 
            print()
            print("You have already guessed that letter.")
    if "_" not in list:
        print("You won! The word was:", Chosen_One)
        exit()
    elif count == 0:
        print("You lost. The word was:", Chosen_One)

        
editing() 
        

    

