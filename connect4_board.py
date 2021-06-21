class Connect4Board:
    def __init__(self):
        self.b = [[" ", " ", " ", " ", " ", " "], #column 1
                 [" ", " ", " ", " ", " ", " "], #column 2
                 [" ", " ", " ", " ", " ", " "], #column 3
                 [" ", " ", " ", " ", " ", " "], #column 4
                 [" ", " ", " ", " ", " ", " "], #column 5
                 [" ", " ", " ", " ", " ", " "], #column 6
                 [" ", " ", " ", " ", " ", " "]] #column 7
        self.column_number = len(self.b) #7
        self.row_number = len(self.b[0]) #6
        self.num_diff_moves = 7

    def print_board(self):
        print("|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][5] + " | " + self.b[1][5] + " | " + self.b[2][5] + " | " + self.b[3][5] + " | " + self.b[4][5] + " | " + self.b[5][5] + " | " + self.b[6][5] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][4] + " | " + self.b[1][4] + " | " + self.b[2][4] + " | " + self.b[3][4] + " | " + self.b[4][4] + " | " + self.b[5][4] + " | " + self.b[6][4] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][3] + " | " + self.b[1][3] + " | " + self.b[2][3] + " | " + self.b[3][3] + " | " + self.b[4][3] + " | " + self.b[5][3] + " | " + self.b[6][3] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][2] + " | " + self.b[1][2] + " | " + self.b[2][2] + " | " + self.b[3][2] + " | " + self.b[4][2] + " | " + self.b[5][2] + " | " + self.b[6][2] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][1] + " | " + self.b[1][1] + " | " + self.b[2][1] + " | " + self.b[3][1] + " | " + self.b[4][1] + " | " + self.b[5][1] + " | " + self.b[6][1] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "| " + self.b[0][0] + " | " + self.b[1][0] + " | " + self.b[2][0] + " | " + self.b[3][0] + " | " + self.b[4][0] + " | " + self.b[5][0] + " | " + self.b[6][0] +" |\n"
            "|---|---|---|---|---|---|---|\n"
            "  1   2   3   4   5   6   7  \n")

    def board_full(self):
        for i in range (0, self.column_number):
            if self.b[i][len(self.b[0]) - 1] == " ":
                return False
        return True

    def reset_board(self):
        for i in range(0, self.column_number):
            for j in range(0, self.row_number):
                self.b[i][j] = " "

    def place_disc(self, disc, column, situation):
        for i in range(0, len(self.b[column])):
            if self.b[column][i] == " ":
                self.b[column][i] = disc
                return
        if situation == "game":
            retry_column = int(input("This column is full. Please choose a different one: ")) - 1
            self.place_disc(disc, retry_column, "game")
        else:
            return "full"

    def remove_disc(self, disc, column):
        #loops backwards from top of column down to bottom
        for i in range(len(self.b[column]) - 1, -1, -1): 
            if self.b[column][i] == disc:
                self.b[column][i] = " "
                return

    def state_scanner(self, disc1, disc2, disc3, disc4):
        score = 0
        #east scan    
        for i in range(0, self.column_number - 3): #[0 - 3]
            for j in range(0, self.row_number): #[0 - 5]
                if (self.b[i][j] == disc1) and (self.b[i + 1][j] == disc2) and (self.b[i + 2][j] == disc3) and (self.b[i + 3][j] == disc4):
                    score += 1                 
        #north scan
        for i in range(0, self.column_number):
            for j in range(0, self.row_number - 3):
                if (self.b[i][j] == disc1) and (self.b[i][j + 1] == disc2) and (self.b[i][j + 2] == disc3) and (self.b[i][j + 3] == disc4):
                    score += 1
        #north east scan
        for i in range(0, self.column_number - 3):
            for j in range(0, self.row_number - 3):
                if (self.b[i][j] == disc1) and (self.b[i + 1][j + 1] == disc2) and (self.b[i + 2][j + 2] == disc3) and (self.b[i + 3][j + 3] == disc4):
                    score += 1 
        #north east reverse scan
        for i in range(0, self.column_number - 3):
            for j in range(0, self.row_number - 3):
                if (self.b[i + 3][j] == disc1) and (self.b[i + 2][j + 1] == disc2) and (self.b[i + 1][j + 2] == disc3) and (self.b[i][j + 3] == disc4):
                    score += 1
        return score

    def player_score(self, two_score, three_score, four_score, disc):
        player_score = 0
        player_score += self.state_scanner(disc, " ", " ", " ")
        player_score += self.state_scanner(" ", disc, " ", " ")
        player_score += self.state_scanner(" ", " ", disc, " ")
        player_score += self.state_scanner(" ", " ", " ", disc)
        player_score += two_score * self.state_scanner(disc, disc, " ", " ")
        player_score += two_score * self.state_scanner(disc, " ", disc, " ")
        player_score += two_score * self.state_scanner(disc, " ", " ", disc)
        player_score += two_score * self.state_scanner(" ", disc, " ", disc)
        player_score += two_score * self.state_scanner(" ", " ", disc, disc)
        player_score += two_score * self.state_scanner(" ", disc, disc, " ")
        player_score += three_score * self.state_scanner(disc, disc, disc, " ") 
        player_score += three_score * self.state_scanner(disc, disc, " ", disc) 
        player_score += three_score * self.state_scanner(disc, " ", disc, disc) 
        player_score += three_score * self.state_scanner(" ", disc, disc, disc) 
        player_score += four_score * self.state_scanner(disc, disc, disc, disc) 
        return player_score

    def check_for_win(self, player_disc):
        if self.state_scanner(player_disc, player_disc, player_disc, player_disc) > 0:
            return True
        else:
            return False