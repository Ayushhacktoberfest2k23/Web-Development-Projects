import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'date', 'grape', 'kiwi', 'lemon', 'melon', 'orange', 'peach']
    return random.choice(words)

def play_game():
    word = choose_word()
    guessed = '_' * len(word)
    guessed = list(guessed)
    attempts = 0
    max_attempts = 10
    guessed_letters = []

    print("Welcome to the Word Guessing Game!")
    print("The word contains", len(word), "letters.")

    while True:
        print(" ".join(guessed))
        if attempts >= max_attempts:
            print("You have run out of attempts. The word was", word)
            break

        if '_' not in guessed:
            print("Congratulations! You guessed the word", word, "correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts += 1
            print("The letter is not in the word. Attempts left:", max_attempts - attempts)

if __name__ == '__main__':
    play_game()
