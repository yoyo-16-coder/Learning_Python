import streamlit as st
import CAESAR_CIPHER
import HANGMAN

st.title("🎮 Mini Games")

game = st.selectbox("Choose a game to play:", 
                    ["Caesar Cipher", "Hangman", "Tic Tac Toe"])

st.markdown("---")

if game == "Caesar Cipher":
  CAESAR_CIPHER.app()
elif game == "Hangman":
  HANGMAN.app()
