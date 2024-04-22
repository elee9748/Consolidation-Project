Tuple Out Dice Game - players take turns rolling three dice and aim to score the
most points without rolling three of the same number

`import random`: This statement imports the random module, which provides functions for generating random numbers, shuffling sequences, and selecting random elements.

`roll_dice()`: This function simulates the rolling of three dice. It generates random results for each die and returns them as a list.

`is_tupled_out(roll_results)`: This function checks if all three dice show the same value. It takes the roll results as input and returns True if all dice have the same value, indicating a "tupled out" situation. Otherwise, it returns False.

`play_tuple_out(num_players, target_score=None)`: This function is the main driver of the game. It initiates and controls the flow of the "Tuple Out" dice game. It takes the number of players as input and an optional target score to determine the end condition of the game. It prompts players to roll dice, handles "tupled out" situations, allows for re-rolls, updates player scores, and determines the winner based on the target score (if specified).
