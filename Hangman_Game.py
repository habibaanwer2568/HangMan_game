"""
the pseudocode :

1- Initializing the game by importing a 
            -list of words, 
            -selecting a random word, 
            -creating a list of underscores,
            - and setting the number of incorrect guesses allowed.
2- Entering a main game loop that continues as long as the player has remaining guesses and the word is not guessed.
3- Inside the loop, 
            -displaying the current state of the word, 
            -prompting the player for a letter, 
            -and checking if the letter is in the word. 
                    --If it is, replacing the corresponding underscores with the letter. 
                    --If not, decrementing the number of remaining guesses.
4- Checking if the player has guessed the word. 
            -If yes, displaying a congratulatory message and exiting the game. 
            -If no, checking if the player has run out of guesses. If yes, displaying the word and a game over message, 
            -then exiting the game. If no, continuing the game loop.
"""

import random as rr

print("/\\" * 14, 
        "Welcome to the Hangman Game", 
      "\\/" * 14,
        sep="\n")

WordsList = ['unicorn', 'wizard', 'galaxy', 'treasure', 'pirate', 'enchanted', 'mermaid', 'magic', 'adventure', 'potion']

while True:
    # choosing a random word from our list
    random_word = rr.choice(WordsList)

    for x in random_word:
        print("_", end=" ")

    def draw_hangman(wrong):
        if wrong == 0:
            print("\n+---+")
            print("    |")
            print("    |")
            print("    |")
            print("   ===")
        elif wrong == 1 :
            print("\n+---+")
            print("O   |")
            print("    |")
            print("    |")
            print("   ===")
        elif wrong == 2 :
            print("\n+---+")
            print("O   |")
            print("|   |")
            print("    |")
            print("   ===")
        elif wrong == 3 :
            print("\n+---+")
            print(" O  |")
            print("/|  |")
            print("    |")
            print("   ===")
        elif wrong == 4 :
            print("\n+---+")
            print(" O  |")
            print("/|\\ |")
            print("    |")
            print("   ===")
        elif wrong == 5 :
            print("\n+---+")
            print(" O  |")
            print("/|\\ |")
            print("/   |")
            print("   ===")
        elif wrong == 6 :
            print("\n+---+")
            print(" O  |")
            print("/|\\ |")
            print("/ \\ |")
            print("   ===")

# making a func to print off the word on each iteration of the loop
    def printWord(guessed_letters):
        counter = 0
        right_letters = 0
        for letter in random_word:
            if letter in guessed_letters:
                print(random_word[counter], end=" ")
                right_letters += 1
            else:
                print(" ", end=" ")
            counter += 1
        return right_letters

# printing the lines that we alraedy made above continuously
    def print_UnderScores():
        print("\r")
        for letter in random_word:
            print("\u203E", end=" ")

# creating the loop that will operate the game
    WORD2guess_length = len(random_word)
    wrong_attempts_count = 0
    current_guess_index = 0       # to keep tracke where we are
    current_letters_guessed = []
    current_letters_right = 0

    while wrong_attempts_count != 6 and current_letters_right != WORD2guess_length:
        print("\nLetters guessed till now:")
        for letter in current_letters_guessed:
            print(letter, end=" ")

        # Ask the user for input to guess
        guessed_letter = input("\nguess a letter:").lower()

        # Check if the guessed letter is in the random word 
        if guessed_letter in random_word:
            current_letters_guessed.append(guessed_letter)
            current_letters_right = printWord(current_letters_guessed)
            if current_letters_right == WORD2guess_length:
                print(f"Congratulations! You guessed the word ^-^ '{random_word}'.")
                break  
            print_UnderScores()
        
        # in case the guess is wrong
        else:
            wrong_attempts_count += 1
            current_letters_guessed.append(guessed_letter)

            # updating our hangman drawing
            draw_hangman(wrong_attempts_count)

            # printing the word
            current_letters_right = printWord(current_letters_guessed)
            print_UnderScores()
            if wrong_attempts_count == 6:
                print(f"\nSorry, you ran out of guesses ): \nThe word was '{random_word}'.")
                break  # Exit the loop if the user runs out of guesses

    # Ask the users if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower().strip()
    if play_again not in ["yes", "y"]:
        break

print("Thanks for playing ^-^")