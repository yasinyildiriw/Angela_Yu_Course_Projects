MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 100,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
def rapor():
    print(f"Water: {resources["water"]} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${money}")
def check(kahve):
    if (resources["water"] > MENU[f"{kahve}"]["ingredients"]["water"]) and (resources["coffee"] > MENU[f"{kahve}"]["ingredients"]["coffee"]):
        if (kahve != "espresso") and (resources["milk"] > MENU[f"{kahve}"]["ingredients"]["milk"]):
            return True
        return True
    else:
        return False
def calculate(kahve):
    print("Please insert coins.")
    quarter = int(input("How many quarters?"))
    dime = int(input("How many dimes?"))
    nickel = int(input("How many nickels?"))
    penny = int(input("How many pennies?"))
    gelen_para = quarter*0.25 + dime*0.1 + nickel*0.05 + penny*0.01
    global money
    if (gelen_para >= MENU[f"{kahve}"]["cost"]) and (kahve != "espresso"):
        money += MENU[f"{kahve}"]["cost"]
        resources["water"] -= MENU[f"{kahve}"]["ingredients"]["water"]
        resources["milk"] -= MENU[f"{kahve}"]["ingredients"]["milk"]
        resources["coffee"] -= MENU[f"{kahve}"]["ingredients"]["coffee"]
        print(f"Here is ${gelen_para - MENU[f"{kahve}"]["cost"]} in change.")
        print(f"Here is your {kahve} ☕. Enjoy!")
    elif (gelen_para >= MENU[f"{kahve}"]["cost"]) and (kahve == "espresso"):
        money += MENU[f"{kahve}"]["cost"]
        resources["water"] -= MENU[f"{kahve}"]["ingredients"]["water"]
        resources["coffee"] -= MENU[f"{kahve}"]["ingredients"]["coffee"]
        print(f"Here is ${gelen_para - MENU[f"{kahve}"]["cost"]} in change.")
        print(f"Here is your {kahve} ☕. Enjoy!")
    else:
        print("Your money is not enough.")
control = True
while control:
    coffee = input("What would you like? (Espresso($1.5)/Latte($2.5)/Cappuccino($3))")
    if coffee == "report":
        rapor()
    elif (coffee == "espresso") or (coffee == "latte") or (coffee == "cappuccino"):
        calculate(coffee)
        control = check(coffee)
    else:
        print("You typed wrong")


if resources["water"] <= 49:
    print(f"Sorry there is not enough water")
elif resources["milk"] <= 99:
    print(f"Sorry there is not enough milk")
elif resources["coffee"] <= 17:
    print(f"Sorry there is not enough coffee")