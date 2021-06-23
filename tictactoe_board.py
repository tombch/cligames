class TictactoeBoard:
    def __init__(self):
        self.b = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]    
        self.column_number = len(self.b) #3
        self.row_number = len(self.b[0]) #3   
        self.moves = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]

    def print_board(self):  
        print("  |---|---|---|\n"
            "0 | " + self.b[0][0] + " | " + self.b[0][1] + " | " + self.b[0][2] + " | \n"
            "  |---|---|---|\n"
            "1 | " + self.b[1][0] + " | " + self.b[1][1] + " | " + self.b[1][2] + " | \n"
            "  |---|---|---|\n"
            "2 | " + self.b[2][0] + " | " + self.b[2][1] + " | " + self.b[2][2] + " | \n"
            "  |---|---|---|\n"
            "    0   1   2 \n")

    def board_full(self):
        for i in range (0, self.column_number):
            for j in range(0, self.row_number):
                if self.b[i][j] == " ":
                    return False
        return True

    def reset_board(self):
        for i in range(0, self.column_number):
            for j in range(0, self.row_number):
                self.b[i][j] = " "

    def place_disc(self, disc, position, situation):
        position0 = int(position[0])
        position1 = int(position[1])

        if self.b[position0][position1] == " ":
            self.b[position0][position1] = disc
            return
        if situation == "game":
            retry_position = tuple(input("This position is full. Please choose a different one: "))
            self.place_disc(disc, retry_position, "game")
        else:
            return "full"

    def remove_disc(self, disc, position):
        position0 = int(position[0])
        position1 = int(position[1])
        if self.b[position0][position1]== disc:
            self.b[position0][position1] = " "
            return

    def state_scanner(self, disc1, disc2, disc3, disc4):
        score = 0
        #east scan    
        for j in range(0, self.row_number):
            if (self.b[0][j] == disc1) and (self.b[1][j] == disc2) and (self.b[2][j] == disc3):
                score += 1                 
        #north scan
        for i in range(0, self.column_number):
                if (self.b[i][0] == disc1) and (self.b[i][1] == disc2) and (self.b[i][2] == disc3):
                    score += 1
        #north east scan
        if (self.b[0][0] == disc1) and (self.b[1][1] == disc2) and (self.b[2][2] == disc3):
            score += 1 
        #north east reverse scan
        if (self.b[0][2] == disc1) and (self.b[1][1] == disc2) and (self.b[2][0] == disc3):
            score += 1
        return score

    def player_score(self, two_score, three_score, four_score, disc):
        player_score = 0
        player_score += two_score * self.state_scanner(disc, " ", " ", " ")
        player_score += two_score * self.state_scanner(" ", disc, " ", " ")
        player_score += two_score * self.state_scanner(" ", " ", disc, " ")
        player_score += three_score * self.state_scanner(disc, disc, " ", " ")
        player_score += three_score * self.state_scanner(disc, " ", disc, " ")
        player_score += three_score * self.state_scanner(" ", disc, disc, " ")
        player_score += four_score * self.state_scanner(disc, disc, disc, " ")
        return player_score

    def check_for_win(self, player_disc):
        if self.state_scanner(player_disc, player_disc, player_disc, " ") > 0:
            return True
        else:
            return False