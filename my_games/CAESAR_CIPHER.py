import streamlit as st

def app():
  st.header("🔐 Caesar Cipher")
  import streamlit as st

  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


  mode = st.selectbox("Mode", ["Encrypt", "Decrypt"])
  if mode == "Encrypt":
    def encrypt(message, key):
      result = ""
      for letter in message:
        if letter in alphabet:
          i = alphabet.index(letter.lower())
          new_alphabet = (i + key) % 26 
          result += alphabet[new_alphabet]
        elif letter.isupper():
          i = alphabet.index(letter.lower())
          new_alphabet = (i + key) % 26
          result += alphabet[new_alphabet].upper()
        else:
          result += letter
      return result

    st.title("Caesar Cipher")
    st.subheader("Encrypt your secret message!")

    message = st.text_input("Enter your message: ")
    key = st.number_input("Shift key: ", min_value=1, max_value=25, step=1)

    if st.button("Encrypt"):
      encrypted = encrypt(message, key)
      st.success(f"Encrypted Message: {encrypted}")

  elif mode == "Decrypt":
    def decrypt(message, key):
      result = ""
      for letter in message:
        if letter in alphabet:
          i = alphabet.index(letter.lower())
          new_alphabet = (i - key) % 26 
          result += alphabet[new_alphabet]
        elif letter.isupper():
          i = alphabet.index(letter.lower())
          new_alphabet = (i - key) % 26
          result += alphabet[new_alphabet].upper()
        else:
          result += letter
      return result

    st.title("Caesar Cipher")
    st.subheader("Decrypt your secret message!")

    message = st.text_input("Enter your message: ")
    key = st.number_input("Shift key: ", min_value=1, max_value=25, step=1)

    if st.button("Decrypt"):
      decrypted = decrypt(message, key)
      st.success(f"Decrypted Message: {decrypted}")
      

      







      





