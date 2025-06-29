import os
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("CAESAR CIPHER")
print()

def encrypt():
  for letter in message:
    if letter.lower() in alphabet:
      i = alphabet.index(letter)
      try: 
        new_alphabet = alphabet[i + key]
      except IndexError:
        new_alphabet = alphabet[(i + key) % 26]  
      print(new_alphabet, end="")
    else:
      print(letter, end="")
      
      
def decrypt():
  for letter in message:
    if letter.lower() in alphabet:
      i = alphabet.index(letter)
      try: 
        new_alphabet = alphabet[i - key]
      except IndexError:
        new_alphabet = alphabet[(i - key) % 26]  
      print(new_alphabet, end="")
    else:
      print(letter, end="")

while True:
  print()
  ask = input("Do you want to 'decrypt' or 'encrypt'?: ").strip().lower()
  print()
  os.system("clear")
  print()
  print("CAESAR CIPHER")
  print()
  message = input("Type your message: ")
  key = int(input("Shift key: "))
  print()
  if ask == "encrypt":
    encrypt()
  elif ask == "decrypt":
    decrypt()
