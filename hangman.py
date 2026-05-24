import random

#We have these 5 predefined words
words = ["apple", "mango", "grape", "banana", "orange"]

# choose a word
chosen_word = random.choice(words)

# Create blanks for guessed letters
guessed_word = ["_"] * len(chosen_word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

#loop for game
while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nCurrent Word:", " ".join(guessed_word))
    print("Wrong Guesses Left:", max_wrong - wrong_guesses)

    # ask for user input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter exists in word
    if guess in chosen_word:
        print("Correct Guess!")

        # Reveal all matching letters
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong Guess!")
        wrong_guesses += 1

#Result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\n Game Over!")
    print("The correct word was:", chosen_word)
