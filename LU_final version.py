import random


def instructions():
    print()
    print(formatter("*", "How to play"))
    print()
    print("Choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter>  to play.  You will get a random token which "
          "might be a horse, a zebra, a donkey, or a unicorn.")
    print()
    print("It costs $1 to play each round but, depending on your prize, you "
          "could win some of your money back.  These are the payout amounts:\n"
          "\tUnicorn: $5 (balance increases by $4\n"
          "\tHorse: $0.50 (balance decreases by $0.50\n"
          "\tZebra: $0.50 (balance decreases by $0.50\n"
          "\tDonkey: $0.00 (balance decreases by $1\n")
    print("\nSee if you can avoid donkeys,Iget the unicorns, and finish with "
          "more money than you started with.\n")
    print("*" * 50)
    print()


def yes_no(question_text):
    while True:
        answer = input(question_text).lower()
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer
        else:
            print("Please answer 'yes' or 'no'")


def num_check(question, low, high):
    error = "That was not valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def generate_token(balance):
    rounds_played = 0
    play_again = ""
    while play_again != "x":
        rounds_played += 1
        print(formatter(".", f"Round {rounds_played}"))
        number = random.randint(1, 100)
        if 1 <= number <= 5:
            balance += 4
            print(formatter("!", "Congratulations, you got a unicorn"))
            print()
        elif 6 <= number <= 36:
            balance -= 1
            print(formatter("D", "Bad luck, you got a donkey"))
            print()
        else:
            if number % 2 == 0:
                balance -= 0.5
                print(formatter("Z", "You got a zebra"))
                print()
            else:
                balance -= 0.5
                print(formatter("H", "You got a horse"))
                print()
        print(f"Your balance is now: ${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            break
        else:
            play_again = input("\nDo you want to play another round?\n"
                               "<enter> to play again or 'X' to exit").lower()
        print()
    return balance


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()
played_before = yes_no("Have you played this game before? ")
if played_before == "No":
    instructions()
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
closing_balance = generate_token(user_balance)
print("Thanks for playing")
print(f"You started with ${user_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*", "Goodbye"))
