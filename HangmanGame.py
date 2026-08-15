import random

# List of words
words = ["python", "software", "computer", "database", "programming"]

# Select a random word
word = random.choice(words)

# Create hidden word display
guessed_word = ["_"] * len(word)

guessed_letters = []
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong guess!")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("\nCongratulations! you guessed the word...")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
