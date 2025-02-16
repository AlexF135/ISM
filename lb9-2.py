import random

def hangman():
    words = ["python", "programming", "developer", "algorithm", "function"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6
    guessed_letters = []

    print("Гра 'Вгадай слово' розпочалася!")
    print("Слово має", len(word_to_guess), "букв.")
    print(" ".join(guessed_word))

    while attempts_left > 0:
        print(f"\nЗалишилось спроб: {attempts_left}")
        guess = input("Введіть літеру: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Будь ласка, введіть лише одну літеру.")
            continue

        if guess in guessed_letters:
            print("Ви вже вгадували цю літеру.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Вірно! Літера є в слові.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Невірно! Такої літери немає.")
            attempts_left -= 1

        print("Слово:", " ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nВітаю! Ви відгадали слово:", word_to_guess)
            break
    else:
        print("\nНа жаль, ви програли. Загадане слово було:", word_to_guess)

hangman()





