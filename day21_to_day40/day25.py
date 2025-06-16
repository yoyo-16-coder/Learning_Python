print()
while True:
    print()
    name = input("Name your warrior: ")
    def rolldice(size):
        import random
        pong = ""
        pong = random.randint(1, 6)
        return pong
    justdoit = rolldice(1)
    def rolldice2(size):
        import random
        pong2 = ""
        pong2 = random.randint(1, 8)
        return pong2
    justdoit2 = rolldice2(1)

    if justdoit*justdoit2 <= 16:
        print("Their health is" "\033[31m" ,justdoit * justdoit2 , "\033[0m" "hp")
    elif justdoit*justdoit2 >= 32:
        print("Their health is " "\033[32m", justdoit * justdoit2, "\033[0m" "hp")
    else:
        print("Their health is" "\033[33m" , justdoit * justdoit2, "\033[0m" "hp")
