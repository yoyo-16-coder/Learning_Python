print()
color = input("Choose a color: ")
def text(word, choose):
    if color == "Black":
        print("\033[30m" ,word, "\033[0m", sep="", end="")
    elif color == "Red":
        print("\033[31m" ,word, "\033[0m", sep="", end="")
    elif color == "Green":
        print("\033[32m" ,word, "\033[0m", sep="", end="")
    elif color == "Yellow":
        print("\033[33m" ,word, "\033[0m", sep="", end="")
    elif color == "Blue":
        print("\033[34m" ,word, "\033[0m", sep="", end="")
    elif color == "Magenta":
        print("\033[35m" ,word, "\033[0m", sep="", end="")
    elif color == "Cyan":
        print("\033[36m" ,word, "\033[0m", sep="", end="")
    elif color == "White":
        print("\033[37m" ,word, "\033[0m", sep="", end="")
    else:
        print("\033[39m" ,word, "\033[0m", sep="", end="")

print()
print("\033[35m""SUPER SUBROUTINE""\033[0m")
print()
print("With my ", end= "")
print("new program ",end= "")
print("I can just choose a color like-", end= " ")
text( color , color)
print(", and that word will appear in the color I set it to.")
print("With no ", end="")
print("wierd ","gaps.",end = "", sep=" ")
print()
print("\033[35m""Epic!""\033[35m")
