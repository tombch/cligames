import time
import connect4_board
import tictactoe_board
import player

board = connect4_board.Connect4Board()
board2 = tictactoe_board.TicTacToeBoard()

def play_game(playerX, playerO):
    board.reset_board()
    win = False
    print("A new game has been started.")
    board.print_board()   
    while win != True:
        #Player 1 turn
        initial_time = time.time()
        playerX_move = playerX.move(board)
        decision_time = time.time() - initial_time
        board.place_disc(playerX.disc, playerX_move, "game")    
        board.print_board()
        print("Player " + playerX.disc + " chose column " + str(playerX_move + 1) + ".")
        print("Decision time:", (decision_time), "seconds")
        if board.check_for_win(playerX.disc):
            print("Player " + playerX.disc + " wins!")
            win = True
        #Player 2 turn
        initial_time = time.time()
        playerO_move = playerO.move(board)
        decision_time = time.time() - initial_time
        board.place_disc(playerO.disc, playerO_move, "game")
        board.print_board()
        print("Player " + playerO.disc + " chose column " + str(playerO_move + 1) + ".")
        print("Decision time:", (decision_time), "seconds")
        if board.check_for_win(playerO.disc):
            print("Player " + playerO.disc + " wins!")
            win = True
    replay = input("Game Over. Enter 'N' here to play again or any other key to go back to the menu: ")
    if replay.upper() == "N":
        play_game(playerX, playerO)
    else:
        menu()

def choose_game_mode():    
    game_mode_choice = input("Enter your choice of game mode here: ")
    if game_mode_choice == '1':
        playerX = player.Player("human", "X")
        playerO = player.Player("human", "O")
        play_game(playerX, playerO)
    elif game_mode_choice == '2':
        piece_choice = input("Do you want to play as X or O against the computer? X has the first move. Enter your choice here: ")
        if piece_choice.upper() == 'X':
            playerX = player.Player("human", "X")
            playerO = player.Player("computer", "O")
            play_game(playerX, playerO)
        elif piece_choice.upper() == 'O':
            playerX = player.Player("computer", "X")
            playerO = player.Player("human", "O")
            play_game(playerX, playerO)
        else:
            print("Not a valid choice.")
            choose_game_mode()
    elif game_mode_choice == '3':
        playerX = player.Player("computer", "X")
        playerO = player.Player("computer", "O")
        play_game(playerX, playerO)
    elif game_mode_choice == '4':
        print("Quitting the game.")
        quit()
    else:
        print("Not a valid choice.")
        choose_game_mode()

def menu():
    print("LETS PLAY CONNECT4.")
    print("Please choose one of the following game modes listed below."
          "\n  1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Exit")
    choose_game_mode()

menu()