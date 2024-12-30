import random
rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''     
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
pc_choice = random.randint(0,2)

if (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
    print(f"You : {rps[user_choice]}")
    print(f"PC : {rps[pc_choice]}")
    print("You Won")
elif user_choice == pc_choice:
    print(f"You : {rps[user_choice]}")
    print(f"PC : {rps[pc_choice]}")
    print("It's Draw")
elif (user_choice == 0 and pc_choice ==1) or (user_choice ==1 and pc_choice ==2) or (user_choice == 2 and pc_choice == 0):
    print(f"You : {rps[user_choice]}")
    print(f"PC : {rps[pc_choice]}")
    print("You Lost")
else:
    print("You typed wrong number")