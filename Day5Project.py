'''
                                        Password Generator
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
hardword = []
print("Welcome to the Password Generator")
num_letters = int(input("How many letters would you like in your password\n"))
num_numbers = int(input(("How many numbers would you like in your password\n")))
num_symbols = int(input("How many symbols would you like in your password\n"))
easy_or_hard = input("Do you want to a random hard password Type Y or N\nExample of Random Password : r72!bh3%k)6\nExample of Basic Password : abcdef123%* \n").lower()
if easy_or_hard == "n":
    for letter in range(num_letters):
        password.append(random.choice(letters))
    for number in range(num_numbers):
        password.append(random.choice(numbers))
    for symbol in range(num_symbols):
        password.append(random.choice(symbols))
    basic_password = ''.join(password)
    print(f"Your Basic Password is : {basic_password}")
elif easy_or_hard == "y":
    for letter in range(num_letters):
        password.append(random.choice(letters))
    for number in range(num_numbers):
        password.append(random.choice(numbers))
    for symbol in range(num_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    hard_password = ''.join(password)
    print(f"Your Hard Password is : {hard_password}")
else:
    print("You typed wrong letter")
