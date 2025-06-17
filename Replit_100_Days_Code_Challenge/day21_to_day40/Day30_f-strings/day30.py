print()
print("30 Days Down- What did you think?")
print()
print("Please choose your color." )
print()
colour = input()
def color(x, colour, y):
    if colour == "red":
        print(x, "\033[31m" ,y, "\033[0m")
    elif colour == "blue":
        print(x, "\033[34m" ,y, "\033[0m")
    elif colour == "yellow":
        print(x, "\033[33m" ,y, "\033[0m")
    elif colour == "purple":
        print(x, "\033[35m" ,y, "\033[0m")
    elif colour == "cyan":
        print(x, "\033[36m" ,y, "\033[0m")
    elif colour == "white":
        print(x, "\033[37m" ,y, "\033[0m")
    elif colour == "black":
        print(x, "\033[30m" ,y, "\033[0m")
    elif colour == "green":
        print(x, "\033[32m" ,y, "\033[0m")
    else:
        print(x , "\033[39m" ,y, "\033[0m")

for i in range(1,31):
    print(f"Day {i}: ")
    day = input()
    print()
    jing = f"You thought Day {i} was"
    ling = f"{day}\n"
    color(f"{jing:^75}\n", colour, f"{ling:^75}")
