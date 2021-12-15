# Connect4 and Tic-tac-toe on the Command Line
Text-based versions of Connect4 and Tic-tac-toe.

The program contains an implementation of the minimax algorithm (with alpha–beta pruning) for the user to play against, or the user can choose to pit the algorithm against itself.

The implementation of the minimax algorithm is contained within the Player class, and is written such that it can play any board games that follow the same structure as the Connect4Board and TictactoeBoard classes.

The program is started by running `python main.py`. 
## How to play
#### Tic-tac-toe
To make a move in Tic-tac-toe, input `xy` when prompted, where `x` and `y` are the x and y coordinates of a square on the board.
#### Connect4
To make a move in Connect4, enter `x` when prompted, where `x` is the index of the column you wish to make a move in.