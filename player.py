class Player:
    def __init__(self, player_type, disc):
        self.player_type = player_type
        self.disc = disc
        if self.disc == "X":
            self.opponent_disc = "O"
        else:
            self.opponent_disc = "X"
    
    def move(self, board):
        if (self.player_type == "human"):
            move = input("Player " + self.disc + " - choose a move: ")
            invalid_move = True
            while(invalid_move):
                for i in board.moves:
                    if move == str(i):
                        invalid_move = False
                if invalid_move == True:
                    move = input("Not a valid move. Choose again: ")
        else:
            print("Player " + self.disc + " is choosing...")
            move = self.minimax(board, 0, 6, -100000000, 100000000) 
        return move 

    def minimax(self, board, current_depth, max_depth, alpha, beta):
        board_score = 0
        level = []
        if board.check_for_win("X") or board.check_for_win("O") or (current_depth == max_depth) or (board.board_full() == True):
            board_score += board.player_score(10, 100, 100000, self.disc) #player evaluation (positive)    
            board_score -= board.player_score(10, 100, 100000, self.opponent_disc) #opponent evaluation (negative)
            return board_score    
        if (current_depth % 2 == 0):
            best_val = -100000000
            for i in board.moves:
                if (board.place_disc(self.disc, i, "simulation") != "full"):
                    current_val = self.minimax(board, current_depth + 1, max_depth, alpha, beta)
                    best_val = max(best_val, current_val)
                    if (current_depth == 0):
                        level.append(current_val)
                    board.remove_disc(self.disc, i)
                    alpha = max(alpha, current_val)
                    if (alpha >= beta):
                        break
                elif (current_depth == 0):
                    level.append(-1000000)
            if (current_depth != 0):
                return best_val
            else:
                chosen_move = board.moves[level.index(max(level))]
                return chosen_move   
        else:
            best_val = 100000000
            for i in board.moves:
                if (board.place_disc(self.opponent_disc, i, "simulation") != "full"):
                    current_val = self.minimax(board, current_depth + 1, max_depth, alpha, beta)
                    best_val = min(best_val, current_val)
                    board.remove_disc(self.opponent_disc, i)
                    beta = min(beta, current_val)
                    if (alpha >= beta):
                        break
            return best_val