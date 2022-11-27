import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

display = []

for letter in chosen_word:
    display += "_"

print(display)

end_of_game = False
lives = 6
length = len(chosen_word)

while not end_of_game:
    guess = input("Guess a letter : ").lower()

    if guess in chosen_word:

        for i in range(length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        if lives == 0:
            end_of_game = True


    print(hangman_art.stages[lives])
    print(display)

    if lives == 0:
        print("You lose.")

    if '_' not in display:
        end_of_game = True
        print("You won.")
