print()
print("Login system")
print()
def wlc():
    print("Welcome Back" ,username)
count = 1
username = input("Username: ")
password = input("Password: ")
while username != "yoyo" and password != "sup":
    print("Whoops! I don't recognise that username or password, please try again.")
    username = input("Username: ")
    password = input("Password: ")
    count = count + 1
    if count == 5:
        print("You have reached the max limit. Please refresh and try again.")
        exit()
wlc()
