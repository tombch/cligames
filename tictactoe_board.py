class TicTacToeBoard:
    def __init__(self):
        self.b = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]    
        self.column_number = len(self.b) #3
        self.row_number = len(self.b[0]) #3   
        self.num_diff_moves = 9

    def print_board(self):  
        print("|---|---|---|\n"
            "| " + self.b[0][0] + " | " + self.b[0][1] + " | " + self.b[0][2] + " | " + "1 \n"
            "|---|---|---|\n"
            "| " + self.b[1][0] + " | " + self.b[1][1] + " | " + self.b[1][2] + " | " + "2 \n"
            "|---|---|---|\n"
            "| " + self.b[2][0] + " | " + self.b[2][1] + " | " + self.b[2][2] + " | " + "3 \n"
            "|---|---|---|\n"
            "  1   2   3 \n")

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