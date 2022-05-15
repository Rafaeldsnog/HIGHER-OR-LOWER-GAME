### HIGHER OR LOWER GAME
import game_data
import random
import time
import os

os.system('cls')
game_over = False

count = 0
while not game_over:
    if count == 0:
        one = random.choice(game_data.data)
    else:
        one = two
    two = random.choice(game_data.data)
    print(f"SCORE: {count}\n")
    print("Who has more Instagram followers?\n")
    print(f"A - {one['name'].upper()} -> {one['description']} from {one['country']}")
    print("\nOR\n")
    print(f"B - {two['name'].upper()} -> {two['description']} from {two['country']}")

    print(one['name'])

    choice = 'z'
    while (choice.lower() != 'a') and (choice.lower() !='b'):
        choice = input("\nA or B -> ")

    if (one['follower_count'] >= two['follower_count']) and choice.lower() == 'a':
        print(f"\nYou got it right!\n{one['name']}: {one['follower_count']} Million followers")
        print(f"{two['name']}: {two['follower_count']} Million followers")

    elif (one['follower_count'] < two['follower_count']) and choice.lower() == 'b':
        print(f"\nYou got it right!\n{one['name']}: {one['follower_count']} Million followers")
        print(f"{two['name']}: {two['follower_count']} Million followers")

    else:
        print(f"\nYou got it wrong.\n{one['name']}: {one['follower_count']} Million followers")
        print(f"{two['name']}: {two['follower_count']} Million followers")
        game_over = True

    count+=1
    time.sleep(2)
    os.system('cls')


print(f"Thanks for playing! Final Score: {count-1}")
time.sleep(2)
os.system('cls')

#### SHOW THE RESULT FOR 1 SECOND
### CLEAR SCREEN
