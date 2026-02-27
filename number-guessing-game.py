import streamlit as st
import random

# Initialize some variables
def setup_game():
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.guess_count = 0
        st.session_state.game_finished = False

# Main function to handle the game logic
def main():
    st.title("Simple Number Guessing Game")
    setup_game()
    
    if not st.session_state.game_finished:
        player_guess = st.number_input("Enter a number between 1 and 100:", min_value=1, max_value=100, step=1)
        
        if st.button("Submit Guess"):
            st.session_state.guess_count += 1
            
            if player_guess < st.session_state.secret_number:
                st.write("Your guess is too low!")
            elif player_guess > st.session_state.secret_number:
                st.write("Your guess is too high!")
            else:
                st.write(f"Congratulations! You guessed the correct number in {st.session_state.guess_count} tries.")
                st.session_state.game_finished = True
                
    st.write(f"Number of guesses: {st.session_state.guess_count}")
    
    if st.session_state.game_finished:
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.guess_count = 0
            st.session_state.game_finished = False

if __name__ == "__main__":
    main()