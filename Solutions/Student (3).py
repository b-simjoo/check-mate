from itertools import product       # parse_knight_red_sqaure
from sys import stderr

color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard

black_pieces = ["p", "r", "n", "b", "q", "k"]
white_pieces = ["P", "R", "N", "B", "Q", "K"]

opposed_king_squares = set()
global_red_squares = set()              # {(row, col)}
global_enemy_pieces_position = list()   # [("R", 1, 3), (piece, row, col)]

# ----------------------------- HELPER FUNCTIONS ----------------------------- #

def parse_to_set(output_set: set, r_index, c_index):        # only be used for kings
    if 0 <= r_index <= 7 and 0 <= c_index <= 7:
        square = chessboard[r_index][c_index]
        if color == "w" and square in ([" ", "K"] + black_pieces):
            output_set.add((r_index, c_index))
        elif color == "b" and square in ([" ", "k"] + white_pieces):
            output_set.add((r_index, c_index))


# ------------------------------ MAIN FUNCTIONS ------------------------------ #
def parse_pawn_red_squares(row_index, col_index):
    if color == "w":
        if col_index != 7:
            if chessboard[row_index+1][col_index+1] in (["K", " "] + black_pieces):
                global_red_squares.add((row_index+1, col_index+1))
        if col_index != 0:
            if chessboard[row_index+1][col_index-1] in (["K", " "] + black_pieces):
                global_red_squares.add((row_index+1, col_index-1))
    elif color == "b":
        if col_index != 7:
            if chessboard[row_index-1][col_index+1] in (["k", " "] + white_pieces):
                global_red_squares.add((row_index-1, col_index+1))
        if col_index != 0:
            if chessboard[row_index-1][col_index-1] in (["k", " "] + white_pieces):
                global_red_squares.add((row_index-1, col_index-1))


def parse_rook_red_squares(r_index, c_index):
    for _ in range(4):
        row_index = r_index
        col_index = c_index

        match _%4:
            case 0:     # up
                dir = "vertical"
                jump = -1
            case 1:     # right
                dir = "horizontal"
                jump = 1
            case 2:     # down
                dir = "vertical"
                jump = 1
            case 3:     # left
                dir = "horizontal"
                jump = -1

        while(True):
            if dir == "vertical":
                row_index += jump
            else:
                col_index += jump
                
            if not (0 <= row_index <= 7 and 0 <= col_index <= 7):
                break

            square = chessboard[row_index][col_index]
            if color == "w":  # add same color pieces pos so that king can take a piece to avoid check mate if possible
                if square in (["K", " "] + black_pieces):
                    global_red_squares.add((row_index, col_index))
                    if square in black_pieces: break        # encounter same color piece
            elif color == "b":  # add same color pieces pos so that king can take a piece to avoid check mate if possible
                if square in (["k", " "] + white_pieces):
                    global_red_squares.add((row_index, col_index))
                    if square in white_pieces: break        # encounter same color piece


def parse_knight_red_squares(r, c):
    squares = list(product([r-1, r+1], [c-2, c+2])) + list(product([r-2, r+2], [c-1, c+1]))
    squares = [(r, c) for r, c in squares if r >=0 and c >= 0 and r <= 7 and c <=7]
    if color == "w":
        squares = [(r, c) for r, c in squares if chessboard[r][c] in [" ", "K"]]
    elif color == "b":
        squares = [(r, c) for r, c in squares if chessboard[r][c] in [" ", "k"]]
    for square in squares:
        global_red_squares.add(square)


def parse_bishop_red_squares(r_index, c_index):

    for _ in range(4):
        col_index = c_index
        row_index = r_index

        match _%4:
            case 0:
                col_jump = -1
                row_jump = 1
            case 1:
                col_jump = 1
                row_jump = 1
            case 2:
                col_jump = 1
                row_jump = -1
            case 3:
                col_jump = -1
                row_jump = -1

        while(True):
            row_index += row_jump
            col_index += col_jump

            if not (0 <= row_index <= 7 and 0 <= col_index <= 7):
                break

            square = chessboard[row_index][col_index]
            if color == "w" and square in (["K", " "] + black_pieces):
                    global_red_squares.add((row_index, col_index))
            elif color == "b" and square in (["k", " "] + white_pieces):
                global_red_squares.add((row_index, col_index))

def parse_queen_red_squares(r_index, c_index):
    for _ in range(8):
        col_index = c_index
        row_index = r_index

        match _%8:
            case 0:
                col_jump = -1
                row_jump = 0
            case 1:
                col_jump = -1
                row_jump = 1
            case 2:
                col_jump = 0
                row_jump = 1
            case 3:
                col_jump = 1
                row_jump = 1
            case 4:
                col_jump = 1
                row_jump = 0
            case 5:
                col_jump = 1
                row_jump = -1
            case 6:
                col_jump = 0
                row_jump = -1
            case 7:
                col_jump = -1
                row_jump = -1

        while(True):
            row_index += row_jump
            col_index += col_jump

            if not (0 <= row_index <= 7 and 0 <= col_index <= 7):
                break

            square = chessboard[row_index][col_index]
            if color == "w" and square in (["K", " "] + black_pieces):
                    global_red_squares.add((row_index, col_index))
            elif color == "b" and square in (["k", " "] + white_pieces):
                global_red_squares.add((row_index, col_index))


def parse_king_red_squares(r_index, c_index):
    positions = list(product([r_index-1, r_index+1, r_index], [c_index-1, c_index+1, c_index]))
    for pos in positions:
        parse_to_set(global_red_squares, pos[0], pos[1])


def find_enemy_pieces_sqaures():
    row_index = 0
    col_index = 0
    for row in chessboard:
        col_index = 0
        for square in row:
            if color == "w" and square in black_pieces:
                global_enemy_pieces_position.append((square, row_index, col_index))
            elif color == "b" and square in white_pieces:
                global_enemy_pieces_position.append((square, row_index, col_index))
            col_index += 1
        row_index += 1


def parse_king_pos():
    row_index = 0
    col_index = 0
    for row in chessboard:
        col_index = 0
        for square in row:
            if color == "w" and square == "K":
                return row_index, col_index
            elif color == "b" and square == "k":
                return (row_index, col_index)
            col_index += 1
        row_index += 1


def parse_king_squares(r_index, c_index):
    positions = list(product([r_index-1, r_index+1, r_index], [c_index-1, c_index+1, c_index]))
    for pos in positions:
        parse_to_set(opposed_king_squares, pos[0], pos[1])

# ------------------------------- MAIN SECTION ------------------------------- #

find_enemy_pieces_sqaures()     # puts every enemy pieces with pos in a set

for piece in global_enemy_pieces_position:      # fill global_red_squares
    if piece[0] == "p" or piece[0] == "P":
        parse_pawn_red_squares(piece[1], piece[2])
    elif piece[0] == "r" or piece[0] == "R":
        parse_rook_red_squares(piece[1], piece[2])
    elif piece[0] == "n" or piece[0] == "N":
        parse_knight_red_squares(piece[1], piece[2])
    elif piece[0] == "b" or piece[0] == "B":
        parse_bishop_red_squares(piece[1], piece[2])
    elif piece[0] == "q" or piece[0] == "Q":
        parse_queen_red_squares(piece[1], piece[2])
    elif piece[0] == "k" or piece[0] == "K":
        parse_king_red_squares(piece[1], piece[2])

king_pos = parse_king_pos()

mate = False

if king_pos in global_red_squares:      # if king square was not red -> no need to compute
    parse_king_squares(king_pos[0], king_pos[1])

    mate_counter = 0        # if 9 it's mated
    for square in opposed_king_squares:
        if square in global_red_squares:
            mate_counter += 1

    if mate_counter == len(opposed_king_squares): mate = True


if mate:
    print("mate")
else:
    print('not mate')