import art
print(art.logo)
decision = True
bids = {}
while decision:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    choose = input("Do you want to continue? Type yes or no").lower()
    if choose == "yes":
        decision = True
        print("\n"*25)
    else:
        decision = False
highest_bid =0
winner = ""
for key in bids:
    if bids[key]>highest_bid:
        highest_bid = bids[key]
        winner = key
print(f"The winner is {winner}  with a bid of ${highest_bid}")