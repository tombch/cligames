import time
import connect4_board
import tictactoe_board
import player

def custom_quit():
    print("Quitting the program.")
    quit()

def invalid_choice():
    print("Not a valid choice.")

def choose_replay_options():
        print("Please choose one of the following options listed below."
        "\n  1: Play again\n  2: Change who plays the game\n  3: Choose a different game\n  4: Exit")

def play_game(player_X, player_O, board):
    board.reset_board()
    winner = ""
    print("A new game has been started.")
    board.print_board()   
    current_player = player_X
    while winner == "":
        initial_time = time.time()
        current_player_move = current_player.move(board)
        decision_time = time.time() - initial_time
        board.place_disc(current_player.disc, current_player_move, "game")    
        board.print_board()
        print("Player " + current_player.disc + " chose move " + str(current_player_move) + ".")
        print("Decision time:", (decision_time), "seconds")
        if board.check_for_win(current_player.disc):
            winner = current_player.disc
        elif board.board_full():
            winner = "draw"
        else:
            if current_player == player_X:
                current_player = player_O
            else:
                current_player = player_X
    if winner == "draw":
        print("Game ended in a draw.")
    else:
        print("Player " + winner + " wins! Game Over.")
    choose_replay_options()
    choosing_replay = True
    while choosing_replay:
        replay_choice = input("Enter your choice here: ")
        if replay_choice == '1':
            play_game(player_X, player_O, board)
        elif replay_choice == '2':
            choosing_replay = False
        elif replay_choice == '3':
            choose_game()
        elif replay_choice == '4':
            custom_quit()
        else:
            invalid_choice()
    
def choose_piece():
    choosing_piece = True
    piece_choice = ""
    while choosing_piece:
        piece_choice = input("Do you want to play as X or O against the computer? X has the first move. Enter your choice here: ")
        if piece_choice.upper() == 'X' or piece_choice.upper() == 'O':
            choosing_piece = False
        else:
            invalid_choice()
    return piece_choice

def choose_mode_options():
    print("Please choose one of the following options listed below."
    "\n  1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Choose a different game\n  5: Exit")

def choose_mode(board):
    choose_mode_options()
    choosing_mode = True
    while choosing_mode:
        mode_choice = input("Enter your choice here: ")
        if mode_choice == '1':
            play_game(player.Player("human", "X"), player.Player("human", "O"), board)
            choose_mode_options()
        elif mode_choice == '2':
            chosen_piece = choose_piece()
            if chosen_piece.upper() == 'X':
                play_game(player.Player("human", "X"), player.Player("computer", "O"), board)
                choose_mode_options()
            elif chosen_piece.upper() == 'O':
                play_game(player.Player("computer", "X"), player.Player("human", "O"), board)
                choose_mode_options()
        elif mode_choice == '3':
            play_game(player.Player("computer", "X"), player.Player("computer", "O"), board)
            choose_mode_options()
        elif mode_choice == '4':
            choosing_mode = False
        elif mode_choice == '5':
            custom_quit()
        else:
            invalid_choice()

def choose_game_options():
    print("Please choose one of the following options listed below."
    "\n  1: Connect4\n  2: Tic-tac-toe\n  3: Exit")

def choose_game():   
    choose_game_options()
    choosing_game = True
    while choosing_game:
        game_choice = input("Enter your choice here: ")
        if game_choice == '1':
            print("LETS PLAY CONNECT4.")
            board = connect4_board.Connect4Board()
            choose_mode(board)
            choose_game_options()
        elif game_choice == '2':
            print("LETS PLAY TIC-TAC-TOE.")
            board = tictactoe_board.TictactoeBoard()
            choose_mode(board)
            choose_game_options()
        elif game_choice == '3':
            choosing_game = False
        else:
            invalid_choice()
    custom_quit()

def main():
    print("Welcome to Command Line Board Games.") 
    choose_game()

if __name__ == '__main__':
    main()
    