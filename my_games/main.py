import streamlit as st
import caesar_cipher
import hangman
import tic_tac_toe

st.title("🎮 Mini Games Hub")

game = st.selectbox("Choose a game to play:", 
                    ["Caesar Cipher", "Hangman", "Tic Tac Toe"])

st.markdown("---")

if game == "Caesar Cipher":
    CAESAR_CIPHER.app()
