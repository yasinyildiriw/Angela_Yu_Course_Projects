import random
from oyun_data import data
import oyun_logosu
is_it_true = True
def person_info(person):
    person_name = person["name"]
    person_description = person["description"]
    person_country = person["country"]
    return f"{person_name}, a {person_description}, from {person_country}"
def control(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
print(oyun_logosu.logo)
score = 0
person_b = random.choice(data)
while is_it_true:
    person_a = person_b
    person_b = random.choice(data)
    if person_b == person_a:
        person_b = random.choice(data)
    print(f"Compare A: {person_info(person_a)}.")
    print(oyun_logosu.vs)
    print(f"Against B: {person_info(person_b)}.")
    answer = input("Who has more followers? Type 'A' or 'B':").lower()
    print("\n"*25)
    print(oyun_logosu.logo)
    a_follower_count = person_a["follower_count"]
    b_follower_count = person_b["follower_count"]
    is_correct = control(user_guess=answer, a_followers=a_follower_count, b_followers=b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_it_true = False