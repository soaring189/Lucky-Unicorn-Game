"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 10% chance of unicorn and 30% chance for each of
donkey, zebra, or horse"""
import random
STARTING_BALANCE = 100
balance = STARTING_BALANCE
for item in range(10):
    number = random.randint(1, 100)
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
            balance -= .5
    print(f"Token: {token}, Balance: ${balance:.2f}")
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
