import time
import connect4_board
import tictactoe_board
import player

def play_game(playerX, playerO, board):
    board.reset_board()
    winner = ""
    print("A new game has been started.")
    board.print_board()   
    while winner == "":
        #Player 1 turn
        initial_time = time.time()
        playerX_move = playerX.move(board)
        decision_time = time.time() - initial_time
        board.place_disc(playerX.disc, playerX_move, "game")    
        board.print_board()
        print("Player X chose move " + str(playerX_move) + ".")
        print("Decision time:", (decision_time), "seconds")
        if board.check_for_win(playerX.disc):
            winner = "X"
        else:
            #Player 2 turn
            initial_time = time.time()
            playerO_move = playerO.move(board)
            decision_time = time.time() - initial_time
            print(playerO_move)
            board.place_disc(playerO.disc, playerO_move, "game")
            board.print_board()
            print("Player O chose move " + str(playerO_move) + ".")
            print("Decision time:", (decision_time), "seconds")
            if board.check_for_win(playerO.disc):
                winner = "O"
    print("Player " + winner + " wins!")
    replay = input("Game Over. Enter 'N' here to play again or any other key to go back to the menu: ")
    if replay.upper() == "N":
        play_game(playerX, playerO)
    else:
        menu()

def choose_game_mode(board):    
    game_mode_choice = input("Enter your choice of game mode here: ")
    if game_mode_choice == '1':
        playerX = player.Player("human", "X")
        playerO = player.Player("human", "O")
        play_game(playerX, playerO, board)
    elif game_mode_choice == '2':
        piece_choice = input("Do you want to play as X or O against the computer? X has the first move. Enter your choice here: ")
        if piece_choice.upper() == 'X':
            playerX = player.Player("human", "X")
            playerO = player.Player("computer", "O")
            play_game(playerX, playerO, board)
        elif piece_choice.upper() == 'O':
            playerX = player.Player("computer", "X")
            playerO = player.Player("human", "O")
            play_game(playerX, playerO, board)
        else:
            print("Not a valid choice.")
            choose_game_mode()
    elif game_mode_choice == '3':
        playerX = player.Player("computer", "X")
        playerO = player.Player("computer", "O")
        play_game(playerX, playerO, board)
    elif game_mode_choice == '4':
        print("Quitting the game.")
        quit()
    else:
        print("Not a valid choice.")
        choose_game_mode()

def menu():
    print("Welcome to Command Line Board Games. Please choose one of the following games listed below."
          "\n  1: Connect4\n  2: Tic-tac-toe\n  3: Exit")
    game_choice = input("Enter your choice of game here: ")
    if game_choice == '1':
        board = connect4_board.Connect4Board()
        print("LETS PLAY CONNECT4.")
    elif game_choice == '2':
        board = tictactoe_board.TictactoeBoard()
        print("LETS PLAY TIC-TAC-TOE.")
    elif game_choice == '3':
        print("Quitting the program.")
        quit()
    else:
        print("Not a valid choice.")
        menu()
    print("Please choose one of the following game modes listed below."
          "\n  1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Exit")
    choose_game_mode(board)

menu()