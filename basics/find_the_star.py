import random

play_again = True

while play_again:
    answer = random.randint(1, 3)
    answer_arr = [' ', ' ', ' ']
    answer_arr[answer - 1] = '*'
    print("Can you find the star (Choose one of the numbers)?:\n")
    choice = int(input("[ 1 ]--[ 2 ]--[ 3 ]\n"))
    print(f"[ {answer_arr[0]} ]--[ {answer_arr[1]} ]--[ {answer_arr[2]} ]\n")
    if choice == answer:
        print("YOU WIN!!!\n")
    else:
        print("YOU LOST.\n")
    play_again = input("Play again? (y)es or (n)o:\n").strip().lower() == 'y'
