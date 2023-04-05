"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 10% chance of unicorn and 30% chance for each of
donkey, zebra, or horse"""
import random
tokens = ["unicorn", "horse", "horse", "horse","donkey", "donkey", "donkey","zebra", "zebra", "zebra"]
STARTING_BALANCE = 100
balance = STARTING_BALANCE
for item in range(500):
    token = random.choice(tokens)
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"Final balance = ${balance:.2f}")
