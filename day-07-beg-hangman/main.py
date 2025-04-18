import random
from hangman_words import word_list
from hangman_art import HANGMANPICS, logo

chosen_word = random.choice(word_list)

print(logo)
placeholder = "_"*len(chosen_word)
print(placeholder)

display = ""

game_over = False
correct_letters = []
all_guesses = []

lives = 6

while not game_over:
    print(f"****************************{lives} of 6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha():
        print(f"{guess} is not a letter. Please, guess a valid letter.")
        continue
      

    if guess in all_guesses:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    else:
        all_guesses.append(guess)

    if guess in chosen_word:
        correct_letters.append(guess)
        print(correct_letters)

    else:
        print(f"You guessed {guess}. That's not in the word.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"(***********************It was {chosen_word}. YOU LOSE!**********************")


    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")


    print(HANGMANPICS[lives])
