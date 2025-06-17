# Games Project

**RGTHD Gaming**

## Files

- `Start.py`: Main entry point or launcher for the games.
- `gamble.py`: Number guessing and gambling game.
- `rajakalla.py`: Raja, Mantri, Kalla, Sipahi game.
- `readme.md`: This file.


## How to Play: Raja, Mantri, Kalla, Sipahi (`rajakalla.py`)

| Step | Action |
|------|--------|
| 1    | Run the script: `python rajakalla.py` |
| 2    | Enter the names of four players. |
| 3    | Each round, roles (Raja, Mantri, Kalla, Sipahi) are randomly assigned. |
| 4    | The Raja is revealed. The Mantri must guess who the Kalla (thief) is. |
| 5    | If Mantri guesses correctly, Mantri and Kalla get points (see below). If not, Kalla gets more points. |
| 6    | Scores are tracked and displayed at the end. Results are exported to `game_scores.csv` and `game_scores.xlsx`. A bar chart of scores is shown. |

### Scoring Table

| Role    | Points per Round                      |
|---------|---------------------------------------|
| Raja    | +1000                                 |
| Mantri  | +500 if correct, +100 if wrong        |
| Kalla   | +500 if not caught, +100 if caught    |
| Sipahi  | 0                                     |

## How to Play: The Number Gambit (`gamble.py`)

| Step | Action |
|------|--------|
| 1    | Run the script: `python gamble.py` |
| 2    | Enter the amount (in ₹) you want to play with. |
| 3    | Choose a difficulty level: Easy (1.7x), Moderate (3x), or Difficult (5x). |
| 4    | Pick a number between 1 and 10. |
| 5    | If your number matches any of the computer's numbers, you win and earn a multiple of your entry fee! Otherwise, you lose. |
| 6    | After the game, your score is exported to `game_scores.csv` and `game_scores.xlsx`. |

### Payout Table

| Difficulty | Computer Picks | Multiplier (x) | Win Condition |
|------------|----------------|----------------|--------------|
| Easy       | 5              | 1.7            | Your number matches any of 5 picks |
| Moderate   | 3              | 3              | Your number matches any of 3 picks |
| Difficult  | 1              | 5              | Your number matches the 1 pick     |

### Example Output

- If you play with ₹100 on Moderate and win, you get ₹300.
- If you lose, you get ₹0.

### How to Pay

- Enter your desired amount at the start of the game when prompted.
- Winnings are calculated and displayed automatically.


> **RGTHD Gaming** is our team name, formed from the initials of our members' names listed below.

## Team List

| Name                | Roll Number |
|---------------------|-------------|
| Dhaval Bari         | 2311127     |
| Garvit Saraf        | 2311136     |
| Harshit Maheswari   | 2311142     |
| Rakshith kumar V    | 2311175     |
| Tanish Atreya       | 2311193     |

---

**Bye!**


