import art
import os

bids = {}
c = ''
while  c != "n":
    print(art.text2art("Blind Auction"))
    name = input("Type your name: ")
    bid = int(input("Type your bid: $"))
    bids[name] = bid
    
    c = input("Is there any other bidder?(Y/N): ").lower()
    if c == "y":
        os.system("clear")
    elif c == 'n':
        pass
    else:
        print("Invalid selection!")
        exit()

# Determing the winner of the bid

max_bid = max(bids.values())
key_list = list(bids.keys())
value_list = list(bids.values())

max_bid_idx = value_list.index(max_bid)
max_bidder = key_list[max_bid_idx]

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")