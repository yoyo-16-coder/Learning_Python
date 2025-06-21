import random
Greetings= ["Namaste!","Hello there!", "Konnichiwa!", "Guten Morgan!", "Bore Da!", "Bonjour!", "Ciao!", "Hola!"]
again = ""
while True:
    n = random.randint(0, 7)
    print(f"Today's greeting is {Greetings[n]}")
    again = input("Try again?")
    if again == "no":
        exit()
