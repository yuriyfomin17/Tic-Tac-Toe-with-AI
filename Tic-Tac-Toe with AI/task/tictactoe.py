# write your code here
from collections import deque


class Board:
    def __init__(self):
        self.top = " ---------"
        self.bot = "---------"
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.next_figure = "O"

    def fill_board(self, coordinate, string):
        [x, y] = coordinate
        self.board[x][y] = string

    def print_board(self):
        print(self.top)
        for curr_row in range(3):
            curr_string = deque([])
            for curr_col in range(3):
                if self.board[curr_row][curr_col] == "X" or self.board[curr_row][curr_col] == "O":
                    curr_string.append(self.board[curr_row][curr_col])
                else:
                    curr_string.append(" ")
            curr_string.append("|")
            curr_string.appendleft("|")
            print(' '.join(curr_string))
        print(self.bot)

    def check_winner(self):
        for x in range(3):
            if self.board[x][0] == self.board[x][1] == self.board[x][2]:
                print("" + str(self.board[x][0]) + " wins")
                return True
            if self.board[0][x] == self.board[1][x] == self.board[2][x]:
                print("" + str(self.board[0][x]) + " wins")
                return True
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                print("" + str(self.board[1][1]) + " wins")
                return True
            if self.board[2][0] == self.board[1][1] == self.board[0][2]:
                print("" + str(self.board[1][1]) + " wins")
                return True
        all_string = [str(x).isnumeric() for curr_row in self.board for x in curr_row]
        if all(all_string):
            return "Draw"
        print("Game not finished")
        return None


board = Board()
cells = input("Enter the cells")
cells = list(cells)
for row in range(3):
    for col in range(3):
        sum = row * 3 + col
        if cells[sum] != "_":
            board.fill_board([row, col], cells[sum])
board.print_board()
while board.check_winner() is None:
    coordinates = input("Enter the coordinates:")
    coordinates = coordinates.strip()
    count_x = 0
    count_o = 0
    for i in range(len(cells)):
        if cells[i] == "O":
            count_o += 1
        if cells[i] == "X":
            count_x += 1
        if count_x == count_o:
            board.next_figure = "X"
        if count_x > count_o:
            board.next_figure = "O"
    if coordinates != '':
        coordinates = coordinates.split(" ")
        new_coordinates = [int(x) if x.isnumeric() else False for x in coordinates]
        if len(new_coordinates) == 2 and all(new_coordinates):
            [x, y] = new_coordinates
            if x < 0 or x > 3 or y < 0 or y > 3:
                print("Coordinates should be from 1 to 3!")
            elif board.board[x - 1][y - 1] == "O" or board.board[x - 1][y - 1] == "X":
                print("This cell is occupied! Choose another one!")
            else:
                if board.next_figure == "X":
                    board.fill_board([x - 1, y - 1], "X")
                    board.next_figure = "O"
                elif board.next_figure == "O":
                    board.fill_board([x - 1, y - 1], "O")
                    board.next_figure = "X"
                board.print_board()
        elif not all(new_coordinates):
            print("You should enter numbers!")
