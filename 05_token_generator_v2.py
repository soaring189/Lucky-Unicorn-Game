"""Component 3 (random tokens) v3
Format currency
Ensure odds favour the house - 10% chance of unicorn and 30% chance for each of
donkey, zebra, or horse"""
import random
tokens = ["unicorn", "horse", "horse", "horse","donkey", "donkey", "donkey","zebra", "zebra", "zebra"]
token = 0
balance = 100
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t')
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50
print(f"Token: {token}, Balance: ${balance}")
