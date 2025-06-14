#Blackjack Game

import random

def deal_card():
    """Returns random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def total_score(cards):
    """Take cards and return its sum"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)


def compare(user_score,comp_score):
    if user_score==comp_score:
        return "Draw 🗿"
    elif comp_score==0:
        return "Lost , Opponent have Blackjack ☠️"
    elif user_score==0:
        return "Win with Blackjack 🏆"
    elif user_score>21:
        return "You went over 21 🔫"
    elif comp_score>21:
        return "Opponent went over 21 🔥"
    elif user_score>comp_score:
        return "You win 😎"
    else:
        return "You Lose 😔"



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while input("Do you wanna play? press 'y' to continue: ").lower()=="y":
    user_card = []
    comp_card = []
    game_over=False
    logo = r"""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)
    for i in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())

    user_score = 0
    comp_score = 0 
    
    while not game_over:
    
        user_score=total_score(user_card)
        comp_score=total_score(comp_card)
    
        print(f"Your Cards = {user_card}  Total Score = [{user_score}]")
        print(f"Computer Cards = {comp_card[0]}")
        
        if user_score==0 or comp_score==0 or user_score>21:
            game_over=True
        else:
            if input("Type 'y' to get another card or else end : ").lower()=="y":
                user_card.append(deal_card())
            else:
                game_over=True

    while comp_score !=0 and comp_score<17:
        comp_card.append(deal_card())
        comp_score=total_score(comp_card)

    print(f"Your cards = {user_card} and Final score = [{user_score}]")
    print(f"Computer cards = {comp_card} and Final score = [{comp_score}]")
    print(compare(user_score,comp_score))