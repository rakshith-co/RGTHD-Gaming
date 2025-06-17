print("=== Welcome to RGTHD Gaming ! ===")  
#giveoptions
print("Choose a game to play:")
print("1. The Number Gambit")
print("2. Raja, Mantri, Kalla and Sipahi Game")
game_choice = input("Enter 1 or 2: ")   
if game_choice == '1':
    import gamble
elif game_choice == '2':
    import rajakalla
else:
    print("Invalid choice. Please restart the game and choose 1 or 2.")
    exit()