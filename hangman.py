# import random
# print("Welcome to Hangman!")
# print("You have 6 incorrect guesses.")
# words = ["python", "computer", "coding", "program", "Keyboard"]
# secret_word=random.choice(words)
# print("Secret word:", secret_word)
# display_word=["_"]*len(secret_word)
# print(display_word)
# guess=input("Guess a letter: ")
# if guess in secret_word:
#     print("Good guess!")
# else:
#     print("Wrong guess!")
# for i in range(len(secret_word)):
#     if secret_word[i]==guess:
#         display_word[i]=guess
# print(display_word)
import random

print("Welcome to Hangman!")
print("You have 6 incorrect guesses.")

words = ["python", "computer", "coding", "program", "keyboard"]

secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

wrong_guesses = 0
guessed_letters = []

while wrong_guesses < 6 and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Wrong guesses:", wrong_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in display_word:
    print("\nCongratulations! You guessed the word!")
    print("The word was:", secret_word)
else:
    print("\nGame over!")
    print("The word was:", secret_word)