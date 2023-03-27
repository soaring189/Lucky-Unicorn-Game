"""LU Yes / No
Simplifies the input by converting it to Lower case. Also, accepts y or n as
abbreviations. Prints result of user choice as well as input - for testing
"""

# Ask the user if they have played before
show_instructions = input("Have you played this game before?: ").lower()

# If they say yes, output 'Program Continues'
if show_instructions == "yes" or show_instructions == "y":
    print("Program Continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display Instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}")
