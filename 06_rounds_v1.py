"""Component 4 - game mechanics and looping v1 Based on 05_token_generator_v4
but hard-wired to only allocate donkeys Gives user feedback about number of
rounds and maintains balance.Test amount set to $5"""
import random
TEST_AMOUNT = 5
balance = TEST_AMOUNT
rounds_played = 0
play_again = ""
while play_again != "x":
    rounds_played += 1
    number = random.randint(6, 36)
    if 1 <= number <= 5:
        token = "unicorn"
        balance += 4
    elif 6 <= number <= 36:
        token = "donkey"
        balance -= 1
    else:
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5
        else:
            token = "horse"
            balance -= 0.5
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
    if balance < 1:
        print("\nSorry but you have run out of money")
        break
    else:
        play_again = input(
            "\nDo you want to play another round?\n<enter> to play again or 'X' to exit").lower()
    print()
print(f"\nThanks for playing\nYou started with ${TEST_AMOUNT:.2f}\nand leave with ${balance:.2f}\nGoodbye")
