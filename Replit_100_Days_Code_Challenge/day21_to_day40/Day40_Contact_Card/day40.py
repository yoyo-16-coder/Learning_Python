import os, time
print()
def main():
  while True:
    print("🌟Contact Card🌟")
    print()
    Name = input("Enter your name: ").strip().capitalize()
    print()
    DOB = input("Enter your date of birth: ")
    print()
    Tel = int(input("Enter your phone number: "))  
    print()
    Email = input("Enter your email: ").strip()
    print()
    Address = input("Enter your address: ").strip().capitalize()
    print()
    UserDetails = {"Name": Name, "DOB": DOB, "Tel": Tel, "Email": Email, "Address": Address}
    time.sleep(1)
    os.system("clear")
    print(f"Here is your contact card:\n\n Name: {UserDetails['Name']}\n DOB: {UserDetails['DOB']}\n Tel: {UserDetails['Tel']}\n Email: {UserDetails['Email']}\n Address: {UserDetails['Address']}")
    time.sleep(4)
    os.system("clear")

main()
