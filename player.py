#import random 
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
            move = int(input("Player " + self.disc + " - choose a column to place a disc in: ")) - 1
        else:
            print("Player " + self.disc + " is choosing...")
            move = self.minimax(board, self.disc, self.opponent_disc, 0, 6, -100000000, 100000000) 
        return move 

    def minimax(self, board, disc, opponent_disc, depth, limit, alpha, beta):
        board_score = 0
        level = []
        if (board.state_scanner(disc, disc, disc, disc) > 0) or (board.state_scanner(opponent_disc, opponent_disc, opponent_disc, opponent_disc) > 0) or (depth == limit) or (board.board_full() == True):
            board_score += board.player_score(10, 100, 100000, disc) #player evaluation (positive)    
            board_score -= board.player_score(10, 100, 100000, opponent_disc) #opponent evaluation (negative)
            return board_score    
        if (depth % 2 == 0):
            best_val = -100000000
            for i in range(0, 7):
                if (board.place_disc(disc, i, "simulation") != "full"):
                    current_val = self.minimax(board, disc, opponent_disc, depth + 1, limit, alpha, beta)
                    best_val = max(best_val, current_val)
                    if (depth == 0):
                        level.append(current_val)
                    board.remove_disc(disc, i)
                    alpha = max(alpha, current_val)
                    if (alpha >= beta):
                        break
                elif (depth == 0):
                    level.append(-1000000)
            if (depth != 0):
                return best_val
            else:
                #Add some randomisation where possible - cannot be done if using alpha-beta pruning
                #best_moves = []  #Array of all indexes with max board score
                #max_score = max(level)
                #for i in range(0, 7): #For each index in the level array
                #    if (level[i] == max_score):
                #        best_moves.append(i)
                #chosen_move = best_moves[random.randint(0, len(best_moves) - 1)]  
                chosen_move = level.index(max(level))
                return chosen_move 
    
        else:
            best_val = 100000000
            for i in range(0, 7):
                if (board.place_disc(opponent_disc, i, "simulation") != "full"):
                    current_val = self.minimax(board, disc, opponent_disc, depth + 1, limit, alpha, beta)
                    best_val = min(best_val, current_val)
                    board.remove_disc(opponent_disc, i)
                    beta = min(beta, current_val)
                    if (alpha >= beta):
                        break
            return best_val