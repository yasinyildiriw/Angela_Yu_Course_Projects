logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+" : add,
    "-": subtract,
    "*" : multiply,
    "/" : divide
}
# print(operations["*"](4, 8))
def calculator():
    is_it_true = True
    print(logo)
    first_number = float(input("What's the first number?: "))
    while is_it_true:
        for key in operations:
            print(key)
        islem = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        if islem not in operations:
            sonuc = 0
            print(f"{first_number} undefined {next_number} = {sonuc}")
            print("You typed wrong operation. Try again")
            calculator()
        if islem == "/" and next_number == 0:
            print(f"{first_number} {islem} {next_number} = Infinity")
            calculator()
        sonuc = operations[islem](first_number, next_number)
        print(f"{first_number} {islem} {next_number} = {sonuc}")
        tamam_mi_devam_mi = input(f"Type 'y' to continue calculating with {sonuc}, or type 'n' to start a new calculation: ").lower()
        if tamam_mi_devam_mi == "y":
            first_number = sonuc
        elif tamam_mi_devam_mi == "n":
            calculator()
        else:
            print("You typed wrong letter")
            calculator()
calculator()