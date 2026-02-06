#start: 5/2/2026
#finish: if it ain't broke, don't fix it 
#-5/2/2026-

import random
import time

players = ["player 1", "player 2", "player 3", "player 4"]
turn_score = 0
player_scores = [0, 0, 0, 0]
player_index = 0

    
def roll_dice():

    print('Rolling the dice...')
    time.sleep(1)
    result = random.randint(1, 6)
    print(f"You rolled a {result}!")
    return result


print("Welcome to the PIG game!")


should_start = input("Do you want to start the game? (y/n): ").strip().lower()


if should_start != 'y':
    print("Maybe next time!")
    exit()


player_num = input("Enter your player number(2-4): ").strip()

if player_num not in ['2', '3', '4']:
    print("Invalid number of players, Bozo.")
    exit()


while True:
    try:
        max_score = int(input("Max score is: "))
        if max_score <= 0:
            print("Do you understand positive numbers, asshole?")
            continue
    except ValueError:
        print("That's not a number, bright spark.")
        continue
    time.sleep(1)
    break

while True:  
    text = "Do you want to turn or hold"

    while True:
        if player_scores[player_index] >= max_score:
            print(f"{players[player_index]} wins with a score of {player_scores[player_index]}!")
            exit()
        hold_turn = input(f"{text}, {players[player_index]}? (t/h): ").strip().lower()

        if hold_turn not in ['t', 'h']:
            print("Invalid, bozo. Use 't' or 'h'.")
            continue

        if hold_turn == 't':
            roll = roll_dice()

            if roll == 1:
                print("You rolled a 1! No points this turn.")
                turn_score = 0

                # END TURN
                player_index = (player_index + 1) % int(player_num)
                text = "Do you want to turn or hold"
                break   # <-- THIS is the critical fix

            else:
                turn_score += roll
                print(f"Your turn score is now {turn_score}.")
                text = "Now turn, or hold"

        elif hold_turn == 'h':
            player_scores[player_index] += turn_score
            turn_score = 0

            print(f"{players[player_index]} holds. Total score: {player_scores[player_index]}")

            # END TURN
            player_index = (player_index + 1) % int(player_num)
            text = "Do you want to turn or hold"
            break

                

        

    
    


    






