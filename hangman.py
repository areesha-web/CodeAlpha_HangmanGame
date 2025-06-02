import random

# List of predefined words
words = ["apple", "banana", "grape", "mango", "orange"]
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")
print("_ " * len(word_to_guess))

while incorrect_guesses < max_attempts:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    display_word = [letter if letter in guessed_letters else '_' for letter in word_to_guess]
    print(" ".join(display_word))

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

if incorrect_guesses == max_attempts:
    print(f"😞 Game Over! The word was: {word_to_guess}")
