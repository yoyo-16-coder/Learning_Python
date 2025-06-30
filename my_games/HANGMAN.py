import streamlit as st

def app():
  import random
  listOfWords = ["tape", "mice","necklace","paris","talent","shirt","mouse","points","yellow","pants"]
  HANGMANPICS = ['''
       +-------------+
       |             |
       |             |
                     |
                     |
                     |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
                     |
                     |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
       |             |
                     |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
      /|             |
                     |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
      /|\            |
                     |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
      /|\            |
      /              |
                     |
                     |
                     |
                     |
        ================''', '''

       +-------------+
       |             |
       |             |
       O             |
      /|\            |
      / \            |
                     |
                     |
                     |
                     |
        ================''']
  if "Chosen_One" not in st.session_state:
    st.session_state.listOfWords = ["tape", "mice","necklace","paris","talent","shirt","mouse","points","yellow","pants"]
    st.session_state.Chosen_One = random.choice(listOfWords)
    st.session_state.list = ["_"]* len(st.session_state.Chosen_One)
    st.session_state.count = 6
    st.session_state.lettersUsed = []
    st.session_state.game_over = False
    st.session_state.message = ""

  
  st.title("HANGMAN")
  st.write("\n")
  st.subheader(" ".join(st.session_state.list))
  st.write("\n")
  st.write("Letter's used:" ,", " .join(st.session_state.lettersUsed))
  st.write("\n")
  st.code(HANGMANPICS[6 - st.session_state.count])
  st.write("\n")
  st.write("Lives Remaining:") 
  st.write("♥ " * st.session_state.count)
  st.write("\n")



  
  Userletter = st.text_input("Choose a letter").strip().lower()
  if st.button("Guess") and not st.session_state.game_over:
    if not Userletter.isalpha() or len(Userletter) != 1:
      st.warning("Please enter a single valid letter.") 
    elif Userletter in st.session_state.lettersUsed: 
      st.warning("You have already guessed that letter.")
    else:
      st.session_state.lettersUsed.append(Userletter)
      if Userletter in st.session_state.Chosen_One:
        for i, letter in enumerate(st.session_state.Chosen_One):
          if letter == Userletter:
            st.session_state.list[i] = Userletter
            if "_" not in st.session_state.list:
              st.session_state.game_over = True
              st.rerun()
              st.success(f"You won! The word was: {st.session_state.Chosen_One}")
            else:
              st.session_state.feedback = "correct"
    else:
      st.session_state.count -= 1
      if st.session_state.count == 0:
        st.session_state.game_over = True
        st.rerun()
          
        else:
          st.session_state.feedback = "wrong"


  if "feedback" in st.session_state:
    if st.session_state.feedback == "correct":
      st.success("Correct!")
      if st.button("Refresh"):
        del st.session_state["feedback"]
        st.rerun()
    elif st.session_state.feedback == "wrong":
      st.error("Wrong guess!")
      if st.button("Refresh"):
        del st.session_state["feedback"]
        st.rerun()
  
  if st.session_state.game_over:
    if st.session_state.count == 0:
      st.error(f"You lost! The word was: {st.session_state.Chosen_One}")
      if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()
    else:
      st.success(f"You won! The word was: {st.session_state.Chosen_One}")
      if st.button("Play Again"):
        st.session_state.clear()
        st.rerun()
