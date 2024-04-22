import random

def roll_dice():
    die_faces = [1, 2, 3, 4, 5, 6]
    return random.randit(1, 6)

def is_tupled_out(roll_results):
    return len(set(roll_results)) == 1

def play_tuple_out(num_players, target_score=None):
    players = {}
    for index in range(1, num_players + 1):
        players[f"Player {index}"] = 0

    scores = {player: 0 for player in players}
    
    while True:
        for player in players:
            print(f"{player}'s turn:")
            roll_results = roll_dice()
            print(f"Rolled: {roll_results}")
            
            if is_tupled_out(roll_results):
                print("Tupled out! Zero points for this turn.")
            else:
                fixed_dice = set(roll_results)
                while True:
                    choice = input("Do you want to re-roll? (yes/no): ")
                    if choice.lower() == "no":
                        break
                    elif choice.lower() == "yes":
                        re_roll_dice = [random.choice([1, 2, 3, 4, 5, 6]) if dice not in fixed_dice else dice for dice in roll_results]
                        print(f"Re-rolled: {re_roll_dice}")
                        roll_results = re_roll_dice
                        fixed_dice.update(set(roll_results))
                
                turn_score = sum(roll_results)
                scores[player] += turn_score
                print(f"Scored {turn_score} points this turn.")
            
            print(f"Total score for {player}: {scores[player]}")
            
            if target_score and scores[player] >= target_score:
                print(f"{player} wins!")
                return