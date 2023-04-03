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


def instructions():
    print("** How to Play *****")
    print()
    print("The rules of the game will go here")
    print()


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


played_before = yes_no("Have you played this game before? ")
if played_before == "No":
    instructions()
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")