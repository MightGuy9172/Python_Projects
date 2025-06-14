#Secret Bidding

logo =r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = []


def addBid(name, bid):
    people = {}
    people["name"] = name
    people["bid"] = bid
    bidders.append(people)


print("Welcome to Auction program.")
print(logo)
isStart = True

while isStart:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    addBid(name, bid)
    temp = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if temp == "no":
        isStart = False

max = 0
winner = ""
for people in bidders:
    if people["bid"] > max:
        max = people["bid"]
        winner = people["name"]

print(f"The Winner is {winner} with bid of ${max}")