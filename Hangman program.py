import random

words = ["apple", "python", "school", "computer", "pakistan"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
wrong_guesses = 0

while wrong_guesses < 6 and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))

    guess = input("Guess a letter: ").lower()

    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", 6 - wrong_guesses)

if "_" not in guessed_word:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game Over!")
    print("The word was:", word)