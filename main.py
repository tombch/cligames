from timeit import default_timer as timer
import connect4_board
import tictactoe_board
import player


messages = {
    'game_options' : '1: Connect4\n  2: Tic-tac-toe\n  3: Exit',
    'player_mode_options' : '1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Choose a different game\n  5: Exit',
    'choose_piece' : 'Do you want to play as X or O against the computer? X has the first move.',
    'replay_options' : '1: Play again\n  2: Change who plays the game\n  3: Choose a different game\n  4: Exit',
    'invalid' : 'Not a valid choice.',
    'quit' : 'Exiting the program.'
}


def choose_replay(player_X, player_O, board, display_options=True):
    if display_options:
        print('Please choose one of the following options listed below.')
        print(f"  {messages['replay_options']}")
    choice = input("Enter your choice here: ")
    # Replay game
    if choice == '1':
        play_game(player_X, player_O, board)
    # Change who plays the game
    elif choice == '2':
        choose_player_mode(board)
    # Choose a different game
    elif choice == '3':
        choose_game()
    # Quit program
    elif choice == '4':
        print(messages['quit'])
        quit()
    # Invalid choice
    else:
        print(messages['invalid'])
        choose_replay(player_X, player_O, board, display_options=False)


def play_game(player_X, player_O, board):
    board.reset_board()
    winner = ""
    print("A new game has been started.")
    board.print_board()   
    current_player = player_X
    while winner == "":
        start = timer()
        current_player_move = current_player.move(board)
        end = timer()
        board.place_disc(current_player.disc, current_player_move, "game")    
        board.print_board()
        print(f"Player {current_player.disc} chose move {current_player_move}.")
        print(f"Decision time: {end - start} seconds")
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
        print(f"Player {winner} wins! Game Over.")
    choose_replay(player_X, player_O, board)


def choose_piece(display_options=True):
    if display_options:
        print(messages['choose_piece'])
    choosing_piece = True
    while choosing_piece:
        choice = input("Enter your choice here: ").strip().upper()
        if choice == 'X' or choice == 'O':
            choosing_piece = False
        else:
            print(messages['invalid'])
    return choice


def choose_player_mode(board, display_options=True):
    if display_options:
        print('Please choose one of the following options listed below.')
        print(f"  {messages['player_mode_options']}")
    choice = input("Enter your choice here: ")
    # Human vs Human
    if choice == '1':
        play_game(player.Player("human", "X"), player.Player("human", "O"), board)
    # Human vs Computer
    elif choice == '2':
        chosen_piece = choose_piece()
        if chosen_piece.upper() == 'X':
            play_game(player.Player("human", "X"), player.Player("computer", "O"), board)
        elif chosen_piece.upper() == 'O':
            play_game(player.Player("computer", "X"), player.Player("human", "O"), board)
    # Robot wars
    elif choice == '3':
        play_game(player.Player("computer", "X"), player.Player("computer", "O"), board)
    # Different game
    elif choice == '4':
        choose_game()
    # Quit program
    elif choice == '5':
        print(messages['quit'])
        quit()
    # Invalid choice
    else:
        print(messages['invalid'])
        choose_player_mode(board, display_options=False)


def choose_game(display_options=True):
    if display_options:
        print('Please choose one of the following options listed below.')  
        print(f"  {messages['game_options']}")
    choice = input("Enter your choice here: ")
    # Connect4
    if choice == '1':
        print("LETS PLAY CONNECT4.")
        board = connect4_board.Connect4Board()
        choose_player_mode(board)
    # Tic-tac-toe
    elif choice == '2':
        print("LETS PLAY TIC-TAC-TOE.")
        board = tictactoe_board.TictactoeBoard()
        choose_player_mode(board)
    # Quit program
    elif choice == '3':
        print(messages['quit'])
        quit()
    # Invalid choice
    else:
        print(messages['invalid'])
        choose_game(display_options=False)


def main():
    print("Welcome to Command Line Board Games.") 
    choose_game()


if __name__ == '__main__':
    main()    