from sys import stderr


#------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard
#------------------------------

#------------------------------
# your code goes here
import numpy as np
board = np.array(chessboard) 
neighbors_check = []
if color == 'w':
    pos = np.where(board=='K')
elif color == 'b':
    pos = np.where(board=='k')
king_row = pos[0][0]        #be sorat tuple hst va mokhtasat king o zakhire mikone                           #
king_col = pos[1][0]        # pos[0] mishe tuple avali pos[0][0] mishe adad avali k to tuple

neighbors_pos = [(king_row-1, king_col-1), (king_row-1, king_col), (king_row-1, king_col+1), 
    (king_row, king_col-1), (king_row, king_col+1),
    (king_row+1, king_col-1), (king_row+1, king_col), (king_row+1, king_col+1)]
def rook_check(row, col, c = 'r'):
    if color == 'w':
        for i in range(8):  
            if board[i][col] == c:     #sotoni check mikone
                neighbors_check.append(1)
                return True            #check kne k kish hst kln ya na
        for i in range(8):
            if board[row][i] == c:     #ofoghi check mikone
                neighbors_check.append(1)
                return True
    else:
        for i in range(8):
            if board[i][col] == c.upper():
                neighbors_check.append(1)
                return True
        for i in range(8):
            if board[row][i] == c.upper():
                neighbors_check.append(1)
                return True
    return False
def bishop_check(row, col, c = 'b'):
    i, j = row, col
    if color == 'w':
        while i < 8 and j < 8:
            if board[i][j] == c:
                neighbors_check.append(1)
                return True
            i += 1
            j += 1
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == c:
                neighbors_check.append(1)
                return True
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < 8:
            if board[i][j] == c:
                neighbors_check.append(1)
                return True
            i -= 1
            j += 1
        i, j = row, col
        while i < 8 and j >= 0:
            if board[i][j] == c:
                neighbors_check.append(1)
                return True
            i += 1
            j -= 1
    else:
        while i < 8 and j < 8:
            if board[i][j] == c.upper():
                neighbors_check.append(1)
                return True
            i += 1
            j += 1
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == c.upper():
                neighbors_check.append(1)
                return True
            i -= 1
            j -= 1
        i, j = row, col
        while i >= 0 and j < 8:
            if board[i][j] == c.upper():
                neighbors_check.append(1)
                return True
            i -= 1
            j += 1
        i, j = row, col
        while i < 8 and j >= 0:
            if board[i][j] == c.upper():
                neighbors_check.append(1)
                return True
            i += 1
            j -= 1
    return False
def queen_check(row, col):
    r = rook_check(row, col, c = 'q')
    q = bishop_check(row, col, c = 'q')
    return r or q
def knight_check(row, col, c = 'n'):
    if color == c:
        if row-2 in range(0, 8) and col-1 in range(0, 8):
            if board[row-2][col-1] == c: 
                neighbors_check.append(1)
        if row-1 in range(0, 8) and col-2 in range(0, 8):
            if board[row-1][col-2] == c:
                neighbors_check.append(1)
        if row+1 in range(0, 8) and col-2 in range(0, 8):
            if board[row+1][col-2] == c: 
                neighbors_check.append(1)
        if row+2 in range(0, 8) and col-1 in range(0, 8):
            if board[row+2][col-1] == c: 
                neighbors_check.append(1)
        if row+2 in range(0, 8) and col+1 in range(0, 8):
            if board[row+2][col+1] == c: 
                neighbors_check.append(1)
        if row+1 in range(0, 8) and col+2 in range(0, 8):
            if board[row+1][col+2] == c: 
                neighbors_check.append(1)
        if row-1 in range(0, 8) and col+2 in range(0, 8):
            if board[row-1][col+2] == c: 
                neighbors_check.append(1)
        if row-2 in range(0, 8) and col+1 in range(0, 8):
            if board[row-2][col+1] == c: 
                neighbors_check.append(1)
    else:
        if row-2 in range(0, 8) and col-1 in range(0, 8):
            if board[row-2][col-1] == c.upper(): 
                neighbors_check.append(1)
        if row-1 in range(0, 8) and col-2 in range(0, 8):
            if board[row-1][col-2] == c.upper(): 
                neighbors_check.append(1)
        if row+1 in range(0, 8) and col-2 in range(0, 8):
            if board[row+1][col-2] == c.upper(): 
                neighbors_check.append(1)
        if row+2 in range(0, 8) and col-1 in range(0, 8):
            if board[row+2][col-1] == c.upper(): 
                neighbors_check.append(1)
        if row+2 in range(0, 8) and col+1 in range(0, 8):
            if board[row+2][col+1] == c.upper(): 
                neighbors_check.append(1)
        if row+1 in range(0, 8) and col+2 in range(0, 8):
            if board[row+1][col+2] == c.upper(): 
                neighbors_check.append(1)
        if row-1 in range(0, 8) and col+2 in range(0, 8):
            if board[row-1][col+2] == c.upper(): 
                neighbors_check.append(1)
        if row-2 in range(0, 8) and col+1 in range(0, 8):
            if board[row-2][col+1] == c.upper(): 
                neighbors_check.append(1)
def pawn_check(row, col, c = 'p'):
    if color == 'w':
        if board[row-1][col-1] == c:
            neighbors_check.append(1)
        if board[row-1][col+1] == c:
            neighbors_check.append(1)
    else:
        if board[row+1][col-1] == c.upper():
            neighbors_check.append(1)
        if board[row+1][col+1] == c.upper():
            neighbors_check.append(1)

        

king_check = False
checks = [rook_check, bishop_check, queen_check, knight_check, pawn_check]
for check in checks:
    if check(king_row, king_col) == True:
        king_check = True
        break
for row, col in neighbors_pos:
    if king_check == True:
        if row in range(0, 8) and col in range(0, 8):
            for check in checks:
                check(row, col)
            if board[row][col] != " " or board[row][col] != "":
                neighbors_check.append(1)
        else:
            neighbors_check.append(1)
if len(neighbors_check) >= 8:
    mate = True
else:
    mate = False

# debugger will scan outputs. So whatever your program prints the debugger will check it
# to print something without checking by debugger write this:
# print(<something>, file=stderr)
# replace <something> with anything you want, debugger will not check output of this line
# here is some examples, if user wants to check white this lines will write some debug lines

if color == 'w':
    print('Yo Mr.White', file=stderr)

# mate = False

#------------------------------

#------------------------------
# output
# your program should print 'mate' or 'not mate'
# you can set mate = True to print 'mate'
# and set False to print 'not mate'
# or just print them yourself
if mate:
    print('mate')
else:
    print('not mate')