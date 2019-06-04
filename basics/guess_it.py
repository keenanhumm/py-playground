import random

play_again = True
lowest = 1
highest = 9
max_guesses = 3

while play_again:
    secret_num = random.randint(lowest, highest)
    num_guesses = 0
    print(f"\nCan you guess the secret number between {lowest} and {highest}?\n")
    while num_guesses < max_guesses:
        guessed_num = int(input(f"\nGuess No. {num_guesses + 1}: "))
        num_guesses += 1
        if guessed_num == secret_num:
            print("YOU WIN!!!\n")
            break
        elif num_guesses >= max_guesses:
            print(f"YOU LOST! The number was {secret_num}.\n")
            break
        elif guessed_num < secret_num:
            print("Try higher\n")
        else:
            print("Try lower\n")

    play_again = input("Play again? (Y)es or (N)o: ").lower() == 'y'

