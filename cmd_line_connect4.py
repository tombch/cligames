import time
b = [[" ", " ", " ", " ", " ", " "], #column 1
     [" ", " ", " ", " ", " ", " "], #column 2
     [" ", " ", " ", " ", " ", " "], #column 3
     [" ", " ", " ", " ", " ", " "], #column 4
     [" ", " ", " ", " ", " ", " "], #column 5
     [" ", " ", " ", " ", " ", " "], #column 6
     [" ", " ", " ", " ", " ", " "]] #column 7
p1_disc = "X"
p2_disc = "O"
column_number = len(b)
row_number = len(b[0])


def print_board():
    print("|---|---|---|---|---|---|---|\n"
          "| " + b[0][5] + " | " + b[1][5] + " | " + b[2][5] + " | " + b[3][5] + " | " + b[4][5] + " | " + b[5][5] + " | " + b[6][5] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "| " + b[0][4] + " | " + b[1][4] + " | " + b[2][4] + " | " + b[3][4] + " | " + b[4][4] + " | " + b[5][4] + " | " + b[6][4] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "| " + b[0][3] + " | " + b[1][3] + " | " + b[2][3] + " | " + b[3][3] + " | " + b[4][3] + " | " + b[5][3] + " | " + b[6][3] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "| " + b[0][2] + " | " + b[1][2] + " | " + b[2][2] + " | " + b[3][2] + " | " + b[4][2] + " | " + b[5][2] + " | " + b[6][2] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "| " + b[0][1] + " | " + b[1][1] + " | " + b[2][1] + " | " + b[3][1] + " | " + b[4][1] + " | " + b[5][1] + " | " + b[6][1] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "| " + b[0][0] + " | " + b[1][0] + " | " + b[2][0] + " | " + b[3][0] + " | " + b[4][0] + " | " + b[5][0] + " | " + b[6][0] +" |\n"
          "|---|---|---|---|---|---|---|\n"
          "  1   2   3   4   5   6   7  \n")


def reset_board():
    for i in range(0, column_number):
        for j in range(0, row_number):
            b[i][j] = " "


def place_disc(disc, column, situation):
    for i in range(0, len(b[column])):
        if b[column][i] == " ":
            b[column][i] = disc
            return
    if situation == "game":
        retry_column = int(input("This column is full. Please choose a different one: ")) - 1
        place_disc(disc, retry_column, "game")
    else:
        return "full"


def remove_disc(disc, column):
    for i in range(len(b[column]) - 1, -1, -1): #loops backwards from top of column down to bottom
        if b[column][i] == disc:
            b[column][i] = " "
            return


def state_scanner(disc1, disc2, disc3, disc4):
    score = 0
    #east scan    
    for i in range(0, column_number - 3): #[0 - 4)
        for j in range(0, row_number): #[0 - 6)
            if ((b[i][j] == disc1) and (b[i + 1][j] == disc2) and (b[i + 2][j] == disc3) and (b[i + 3][j] == disc4)):
                score += 1                 
    #north scan
    for i in range(0, column_number):
        for j in range(0, row_number - 3):
            if ((b[i][j] == disc1) and (b[i][j + 1] == disc2) and (b[i][j + 2] == disc3) and (b[i][j + 3] == disc4)):
                score += 1
    #north east scan
    for i in range(0, column_number - 3):
        for j in range(0, row_number - 3):
            if ((b[i][j] == disc1) and (b[i + 1][j + 1] == disc2) and (b[i + 2][j + 2] == disc3) and (b[i + 3][j + 3] == disc4)):
                score += 1 
    #north east reverse scan
    for i in range(0, column_number - 3):
        for j in range(0, row_number - 3):
            if ((b[i + 3][j] == disc1) and (b[i + 2][j + 1] == disc2) and (b[i + 1][j + 2] == disc3) and (b[i][j + 3] == disc4)):
                score += 1
    return score


def player_score(two_score, three_score, four_score, disc):
    player_score = 0

    player_score += two_score * state_scanner(disc, disc, " ", " ")
    player_score += two_score * state_scanner(disc, " ", disc, " ")
    player_score += two_score * state_scanner(disc, " ", " ", disc)
    player_score += two_score * state_scanner(" ", disc, " ", disc)
    player_score += two_score * state_scanner(" ", " ", disc, disc)

    player_score += three_score * state_scanner(disc, disc, disc, " ") 
    player_score += three_score * state_scanner(disc, disc, " ", disc) 
    player_score += three_score * state_scanner(disc, " ", disc, disc) 
    player_score += three_score * state_scanner(" ", disc, disc, disc) 

    player_score += four_score * state_scanner(disc, disc, disc, disc) 
    return player_score
    

def board_state(): # issue with multiple weights not essential but would be more accurate
    
    board_score = 0
    #2 in a row = 10/-5
    #3 in a row = 100/-50
    #4 in a row = 1000/-750           maybe tweak these a bit?
    
    board_score += player_score(-5, -50, -750, p1_disc) #human evaluation (negative)    
    board_score += player_score(10, 100, 1000, p2_disc) #computer evaluation (positive)
    return board_score


def minimax(disc, enemy_disc, moves_ahead, limit, computer_current_choice, human_current_choice):  #human MIN, computer MAX
    #AI using minimax algorithm
    level = []

    if ((state_scanner(disc, disc, disc, disc) > 0) or (state_scanner(enemy_disc, enemy_disc, enemy_disc, enemy_disc) > 0)) or (moves_ahead == limit):
        return board_state()

    else:
        if (moves_ahead % 2) == 0:  #currently computer turn
            for i in range(0, 7):
                if place_disc(disc, i, "simulation") != "full":  
                    level.append(minimax(disc, enemy_disc, moves_ahead + 1, limit, computer_current_choice, human_current_choice))
                    remove_disc(disc, i)
                    
                    computer_current_choice = max(level)
                    if max(level) > human_current_choice:
                        return max(level)
                                       
                else:
                    level.append(-100000)  #find something else to go here
            if (moves_ahead == 0):
                return level.index(max(level))
            else:
                return max(level)
        
        else:  #currently human turn
            for i in range(0, 7):
                if place_disc(enemy_disc, i, "simulation") != "full":  
                    level.append(minimax(disc, enemy_disc, moves_ahead + 1, limit, computer_current_choice, human_current_choice))
                    remove_disc(enemy_disc, i)

                    human_current_choice = min(level)
                    if min(level) < computer_current_choice:
                        return min(level)
                    
            return min(level)
        

def player_move(player_number, player_type):
    player_disc = ""
    opponent_disc = ""
    if (player_number == 1):
        player_disc = p1_disc
        opponent_disc = p2_disc
    else:
        player_disc = p2_disc
        opponent_disc = p1_disc
    if (player_type == "human_player"):
        move = int(input("Player " + player_disc + " - choose a column to place a disc in: ")) - 1
    else:
        print("Player " + player_disc + " is choosing...")
        initial_time = time.time()
        move = minimax(player_disc, opponent_disc, 0, 6, -100000, 100000)
        decision_time = time.time() - initial_time
        print("Decision time:", (decision_time), "seconds")
    return move 


def turn(p1_type, p2_type):
    #Player 1 move
    p1_move = player_move(1, p1_type)
    place_disc(p1_disc, p1_move, "game")    
    print_board()
    print("Player " + p1_disc + " chose column " + str(p1_move + 1) + ".")
    if state_scanner(p1_disc, p1_disc, p1_disc, p1_disc) > 0:
        print("Player " + p1_disc + " wins!")
        return True  
    #Player 2 move
    p2_move = player_move(2, p2_type)
    place_disc(p2_disc, p2_move, "game")
    print_board()
    print("Player " + p2_disc + " chose column " + str(p2_move + 1) + ".")
    if state_scanner(p2_disc, p2_disc, p2_disc, p2_disc) > 0:
        print("Player " + p2_disc + " wins!")
        return True
    #End of turn
    return False


def play_game(p1_type, p2_type):   
    reset_board() 
    win = False
    print("A new game has been started.")
    print_board()
    while win != True:
        win = turn(p1_type, p2_type)    
    replay = input("Game Over. Enter 'N' here to play again or any other key to go back to the menu: ")
    if (replay.upper() == "N"):
        play_game(p1_type, p2_type)
    else:
        menu()


def x_or_o():
    choice = input("Do you want to play as X or O against the computer? X will have the first move. Enter your choice here: ")
    if (choice.upper() == 'X'):
        play_game("human_player", "computer_player")
    elif (choice.upper() == 'O'):
        play_game("computer_player", "human_player")
    else:
        print("Not a valid choice. Please try again.")
        x_or_o()


def game_mode():    
    choice = input("Enter your choice here: ")
    if (choice == '1'):
        play_game("human_player", "human_player")
    elif (choice == '2'):
        x_or_o()
    elif (choice == '3'):
        play_game("computer_player", "computer_player")
    elif (choice == '4'):
        print("Your choice has been made. Quitting the game!")
        quit()
    else:
        print("Not a valid choice. Please try again.")
        game_mode()


def menu():
    print("LETS PLAY CONNECT4.")
    print("Please choose one of the following game modes listed below."
          "\n  1: Player vs Player\n  2: Player vs Computer\n  3: Computer vs Computer\n  4: Exit")
    game_mode()


menu()