print()
import time, os
while True:
  print()
  time.sleep(3)
  os.system("clear")
  Name = input("Name: " )
  URL = input("URL: " )
  Description = input("Description: ")
  Rating = input("Rating: ")
  print()
  info = { "Name": Name ,"URL": URL, "Description": Description, "Rating": Rating}
  for name, values in info.items():
    print(f"{name}: {values}")
