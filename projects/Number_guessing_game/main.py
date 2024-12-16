import os
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_last_score(file_path):
    try:
        with open(file_path, 'r') as f:
            last_score = int(f.readline())
    except (FileNotFoundError, ValueError):
        last_score = float('inf')  # Set to inf if file doesn't exist or can't read
    return last_score

def update_score(file_path, score):
    with open(file_path, 'w') as f:
        f.write(str(score))

def number_guessing_game():
    clear_console()
    print("Number Guessing Game")

    computer = random.randint(1, 100)
    chances = 0
    score_file = 'projects/Number_guessing_game/score.txt'
    last_score = check_last_score(score_file)

    print('Last High Score:', last_score)

    while True:
        try:
            user = int(input("Guess a number (between 1 and 100): "))
        except ValueError:
            print('Type only numbers, not text.\n')
            continue

        chances += 1

        if user > computer:
            clear_console()
            print(f"Your guess was too high: {user}")
        elif user < computer:
            clear_console()
            print(f"Your guess was too low: {user}")
        else:
            clear_console()
            print('CONGRATULATIONS! You guessed the right number.')
            break 

    if chances < last_score:
        update_score(score_file, chances)

    last_score = check_last_score(score_file)

    print("High Score: ", last_score)
    print("Your Score: ", chances)

if __name__ == '__main__':
    number_guessing_game()