
import random, os, time
listOfWords = ["tape", "mice","necklace","paris","talent","shirt","mouse","points","yellow","pants"]

lettersUsed = []

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
def editing():
    count = 6
    Chosen_One = random.choice(listOfWords)
    list = ["_" for _ in Chosen_One]
    lettersUsed = []
    while count > 0 and "_" in list:
        time.sleep(3)
        os.system("clear")
        print("HANGMAN")
        print()
        print(f"Letter's used: {lettersUsed}")
        print()
        print(" ".join(list))
        print()
        print(HANGMANPICS[6 -count])
        print()
        print(f"Lives Remaining: {'♥ ' * count}")
        print()
        Userletter = input("Choose a letter: ").strip().lower()
        if not Userletter.isalpha() or len(Userletter) != 1:
            print("Please enter a single valid letter.")
            continue
        if Userletter not in lettersUsed:
            lettersUsed.append(Userletter)
            if Userletter in Chosen_One: 
                for i in range(len(Chosen_One)):
                    if Chosen_One[i] == Userletter:
                        list[i] = Userletter
                print()
                print()
                print("Congrats, you got a letter correct. ")
                print()
                
                


            elif Userletter not in Chosen_One:
                print()
                print()
                count = count - 1
                print("Nope, it's not there. ")
                print()

            
        else: 
            print()
            print("You have already guessed that letter.")
    if "_" not in list:
        print("You won! The word was:", Chosen_One)
        print()
        print()
        time.sleep(1)
        playAgain = input("Do you want to play again? ").strip().lower()
        if playAgain == "yes":
            editing()
        else:
            exit()
    elif count == 0:
        print()
        print(HANGMANPICS[6 -count])
        print("You lost. The word was:", Chosen_One)
        print()
        print()
        time.sleep(1)
        playAgain = input("Do you want to play again? ").strip().lower()
        if playAgain == "yes":
            editing()
        else:
            exit()
       

        
editing() 
        

    
    

