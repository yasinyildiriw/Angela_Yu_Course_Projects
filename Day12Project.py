import random
logo = """
┳┓ ┳┳ ┳┳┓ ┳┓ ┏┓ ┳┓  ┏┓ ┳┳ ┏┓ ┏┓ ┏┓ ┳ ┳┓ ┏┓
┃┃ ┃┃ ┃┃┃ ┣┫ ┣  ┣┫  ┃┓ ┃┃ ┣  ┗┓ ┗┓ ┃ ┃┃ ┃┓
┛┗ ┗┛ ┛ ┗ ┻┛ ┗┛ ┛┗  ┗┛ ┗┛ ┗┛ ┗┛ ┗┛ ┻ ┛┗ ┗┛
"""
def easy_game(numara):
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        tahmin = int(input("Make a guess: "))
        if tahmin == numara:
            print(f"You got it! The answer was {numara}")
            return
        else:
            if numara > tahmin:
                print("Too low")
                print("Guess again")
                print("\n")
            else:
                print("Too high")
                print("Guess again")
                print("\n")
        attempt -= 1
    print("You have run out of guesses. Run again")
    return


def hard_game(numara):
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        tahmin = int(input("Make a guess: "))
        if tahmin == numara:
            print(f"You got it! The answer was {numara}")
            return
        else:
            if numara > tahmin:
                print("Too low")
                print("Guess again")
                print("\n")
            else:
                print("Too high")
                print("Guess again")
                print("\n")
        attempt -= 1
    print("You have run out of guesses. Run again")
    return

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
number = random.randint(1,100)
zorluk = input("Choose a difficulty level. Type 'easy' or 'hard':").lower()
if zorluk == "easy":
    easy_game(numara=number)
elif zorluk == "hard" :
    hard_game(numara=number)
else:
    print("You typed wrong!! Try again.")