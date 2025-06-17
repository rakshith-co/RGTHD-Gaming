import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Welcome to The Number Gambit!")

fee = int(input("Enter the amount (in ₹) to play the game: ₹"))

print("Choose difficulty level:")
print("1. Easy (1.7x)")
print("2. Moderate (3x)")
print("3. Difficult (5x)")
lvl = input("Enter 1, 2, or 3: ")

if lvl == '1':
    mult = 1.7
    comp_count = 5
elif lvl == '2':
    mult = 3
    comp_count = 3
elif lvl == '3':
    mult = 5
    comp_count = 1
else:
    print("Invalid choice.")
    comp_count = 0
    mult = 0

if comp_count > 0:
    user_num = int(input("Pick a number between 1 and 10: "))

    if 1 <= user_num <= 10:
        comp_nums = random.sample(range(1, 11), comp_count)

        print(f"\nYou chose: {user_num}")
        print(f"Computer chose: {comp_nums}")

        if user_num in comp_nums:
            win_amt = fee * mult
            print(f"You win! You earned ₹{win_amt:.2f} (x{mult} of your entry)")
        else:
            print("You lost. Better luck next time!")
    else:
        print("Number out of range!")
else:
    print("Game ended due to invalid difficulty selection.")

scores_df = pd.DataFrame([["Player", fee if comp_count > 0 and user_num in comp_nums else 0]], columns=['Player', 'Score'])
scores_df.to_csv('game_scores.csv', index=False)
scores_df.to_excel('game_scores.xlsx', index=False)
print('Scores exported to game_scores.csv and game_scores.xlsx')

