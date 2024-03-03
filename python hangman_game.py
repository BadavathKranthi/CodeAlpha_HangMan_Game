import random

# List of words for the game
words = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "blueberry", "watermelon"]

def choose_word():
    # Choose a random word from the list
    return random.choice(words)

def display_word(word, guessed_letters):
    # Display the word with dashes for letters not guessed yet
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "-"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        if set(word) <= set(guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break

    if incorrect_guesses == max_incorrect_guesses:
        print("\nSorry, you've run out of guesses. The word was:", word)

hangman()
