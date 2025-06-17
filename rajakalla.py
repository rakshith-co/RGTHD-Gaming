import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("=== Welcome to RGTHD Gaming ! ===")
print("now you are playing - Raja,Mantri,Kalla and Sipahi Game")

# Player input
p1 = input("Enter your name player 1: ")
p2 = input("Enter your name player 2: ")
p3 = input("Enter your name player 3: ")
p4 = input("Enter your name player 4: ")

players = [p1, p2, p3, p4]
scores = {p1: 0, p2: 0, p3: 0, p4: 0}

# Predefined role combinations
role_sets = [
    ['Raja', 'Mantri', 'Kalla', 'Sipahi'],
    ['Sipahi', 'Raja', 'Mantri', 'Kalla'],
    ['Kalla', 'Sipahi', 'Raja', 'Mantri'],
    ['Mantri', 'Kalla', 'Sipahi', 'Raja'],
    ['Mantri', 'Kalla', 'Sipahi', 'Mantri']
]

play = 'y'
rounds = 0

while play == 'y':
    rounds += 1
    print(f"\n--- ROUND {rounds} ---")
    
    role_set = random.choice(role_sets)
    random.shuffle(players)
    
    # Assign roles
    assignments = dict(zip(players, role_set))
    raja = [name for name, role in assignments.items() if role == 'Raja'][0]
    mantri = [name for name, role in assignments.items() if role == 'Mantri'][0]
    Kalla = [name for name, role in assignments.items() if role == 'Kalla'][0]
    sipahi = [name for name, role in assignments.items() if role == 'Sipahi'][0]

    # Show king and ask Mantri to guess
    print(f"{raja} is king")
    print(f"Who is chor mantri ji?")
    print(f"{mantri} is: {assignments[mantri]}")
    guess = input("The chor is: ")

    # Scoring
    scores[raja] += 1000
    if guess == Kalla:
        print("right answer")
        scores[mantri] += 500
        scores[Kalla] += 100
    else:
        print("wrong answer")
        scores[Kalla] += 500
        scores[mantri] += 100

    play = input("play:y/n: ")

# Final Score Display
print(f"\nThe total score of {p1} is: {scores[p1]}")
print(f"The total score of {p2} is: {scores[p2]}")
print(f"The total score of {p3} is: {scores[p3]}")
print(f"The total score of {p4} is: {scores[p4]}")

#visualization

# Export scores to CSV
scores_df = pd.DataFrame(list(scores.items()), columns=['Player', 'Score'])
scores_df.to_csv('game_scores.csv', index=False)
scores_df.to_excel('game_scores.xlsx', index=False)
print('Scores exported to game_scores.csv and game_scores.xlsx')

# Visualization
sns.barplot(x='Player', y='Score', data=scores_df)
plt.title('Total Scores of Players')
plt.ylabel('Score')
plt.xlabel('Player')
plt.tight_layout()
plt.show()