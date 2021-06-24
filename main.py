import time
import connect4_board
import tictactoe_board
import player

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
    replay = input("Enter 'N' here to play again or any other key to go back to the menu: ") #change to just going BACK
    if replay.upper() == "N":
        play_game(player_X, player_O, board)
    else:
        menu()

def menu():
    print("Welcome to Command Line Board Games.") 
    print("Please choose one of the following games listed below."
          "\n  1: Connect4\n  2: Tic-tac-toe\n  3: Exit")
    choosing_game = True
    while (choosing_game):
        game_choice = input("Enter your choice of game here: ")
        if game_choice == '1':
            print("LETS PLAY CONNECT4.")
            board = connect4_board.Connect4Board()
            choosing_game = False
        elif game_choice == '2':
            print("LETS PLAY TIC-TAC-TOE.")
            board = tictactoe_board.TictactoeBoard()
            choosing_game = False
        elif game_choice == '3':
            print("Quitting the program.")
            quit()
        else:
            print("Not a valid choice.")  
    print("Please choose one of the following game modes listed below."
          "\n  1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Back")
    choosing_mode = True
    while(choosing_mode):
        mode_choice = input("Enter your choice of game mode here: ")
        if mode_choice == '1':
            play_game(player.Player("human", "X"), player.Player("human", "O"), board)
            choosing_mode = False
        elif mode_choice == '2':
            choosing_piece = True
            while(choosing_piece):
                piece_choice = input("Do you want to play as X or O against the computer? X has the first move. Enter your choice here: ")
                if piece_choice.upper() == 'X':
                    play_game(player.Player("human", "X"), player.Player("computer", "O"), board)
                    choosing_piece = False
                elif piece_choice.upper() == 'O':
                    play_game(player.Player("computer", "X"), player.Player("human", "O"), board)
                    choosing_piece = False
                else:
                    print("Not a valid choice.")
            choosing_mode = False
        elif mode_choice == '3':
            play_game(player.Player("computer", "X"), player.Player("computer", "O"), board)
            choosing_mode = False
        elif mode_choice == '4':
            menu()
        else:
            print("Not a valid choice.")

menu()

