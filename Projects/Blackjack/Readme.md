# Blackjack Game

A simple command-line Blackjack game implemented in Python. Play against the computer and try to beat the dealer by getting as close to 21 as possible without going over!

## Features

- Simulates a standard Blackjack game between a user and the computer.
- Handles Ace values (11 or 1) automatically.
- Detects Blackjack, busts, and draws.
- ASCII art logo for a fun interface.
- Replay option after each game.

## How to Play

1. Run the script [`blackjack.py`](blackjack.py).
2. You and the computer are each dealt two cards.
3. Your cards and one of the computer's cards are shown.
4. Choose to draw another card (`y`) or end your turn.
5. The computer draws cards until its score is at least 17.
6. The winner is determined based on standard Blackjack rules.

## Rules

- Number cards are worth their face value.
- Face cards (Jack, Queen, King) are worth 10.
- Ace can be worth 11 or 1, depending on which is more favorable.
- Blackjack is when the first two cards total 21.
- If your score exceeds 21, you bust and lose.
- If both you and the computer have the same score, it's a draw.

## How to Run

Make sure you have Python installed.

```sh
python blackjack.py
```

Follow the prompts in the terminal to play.

## Code Overview

- [`deal_card`](blackjack.py): Returns a random card from the deck.
- [`total_score`](blackjack.py): Calculates the total score of a hand, handling Ace values.
- [`compare`](blackjack.py): Compares user and computer scores to determine the outcome.

## Example Gameplay

```
Do you wanna play? press 'y' to continue: y
<ASCII art logo>
Your Cards = [10, 7]  Total Score = [17]
Computer Cards = 8
Type 'y' to get another card or else end : n
Your cards = [10, 7] and Final score = [17]
Computer cards = [8, 9, 2] and Final score = [19]
You Lose 😔
```
