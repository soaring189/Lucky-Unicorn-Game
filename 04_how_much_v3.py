"""Component 2 (How much) v3
More efficient method - includes valid range as the basis of the while loop
which eliminates the need to use the 'valid' variable"""

error = "Please enter a whole number between 1 and 10\n"
user_balance = 0
while not 1 <= user_balance <= 10:
    try:
        user_balance = int(input("Please enter a whole number between 1 and 10"
                                 "\nHow much would you like to play with? $"))
        print()

    except ValueError:
        print(error)
        print(f"You are playing with ${user_balance}")
