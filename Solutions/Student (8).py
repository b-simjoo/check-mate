from builtins import print
from sys import stderr

# Mahdi sharifi (4013110660)

def Rook(chessboard,x,y):
    temp_x, temp_y = x, y
    while x + 1 <= 7:
        if chessboard[x + 1][y] == ' ' or chessboard[x + 1][y] == '1':
            chessboard[x + 1][y] = '1'
            x += 1
        else:
            break
    x = temp_x
    while x - 1 >= 0:
        if chessboard[x - 1][y] == ' ' or chessboard[x - 1][y] == '1':
            chessboard[x - 1][y] = '1'
            x -= 1
        else:
            break
    x = temp_x
    while y + 1 <= 7:
        if chessboard[x][y + 1] == ' ' or chessboard[x][y + 1] == '1':
            chessboard[x][y + 1] = '1'
            y += 1
        else:
            break
    y = temp_y
    while y - 1 >= 0:
        if chessboard[x][y - 1] == ' ' or chessboard[x][y - 1] == '1':
            chessboard[x][y - 1] = '1'
            y -= 1
        else:
            break
    y = temp_y
    return chessboard
def Knight(chessboard,x,y):
    if x + 2 <= 7 and y + 1 <= 7:
        if chessboard[x + 2][y + 1] == ' ' or chessboard[x + 2][y + 1] == '1':
            chessboard[x + 2][y + 1] = '1'
    if x + 2 <= 7 and y - 1 >= 0:
        if chessboard[x + 2][y - 1] == ' ' or chessboard[x + 2][y - 1] == '1':
            chessboard[x + 2][y - 1] = '1'
    if y + 2 <= 7 and x - 1 >= 0:
        if chessboard[x - 1][y + 2] == ' ' or chessboard[x - 1][y + 2] == '1':
            chessboard[x - 1][y + 2] = '1'
    if y + 2 <= 7 and x + 1 <= 7:
        if chessboard[x + 1][y + 2] == ' ' or chessboard[x + 1][y + 2] == '1':
            chessboard[x + 1][y + 2] = '1'
    if x - 2 >= 0 and y + 1 <= 7:
        if chessboard[x - 2][y + 1] == ' ' or chessboard[x - 2][y + 1] == '1':
            chessboard[x - 2][y + 1] = '1'
    if x - 2 >= 0 and y - 1 >= 0:
        if chessboard[x - 2][y - 1] == ' ' or chessboard[x - 2][y - 1] == '1':
            chessboard[x - 2][y - 1] = '1'
    if y - 2 >= 0 and x + 1 <= 7:
        if chessboard[x + 1][y - 2] == ' ' or chessboard[x + 1][y - 2] == '1':
            chessboard[x + 1][y - 2] = '1'
    if y - 2 >= 0 and x - 1 >= 0:
        if chessboard[x - 1][y - 2] == ' ' or chessboard[x - 1][y - 2] == '1':
            chessboard[x - 1][y - 2] = '1'
    return chessboard
def Bishop(chessboard,x,y):
    temp_x, temp_y = x, y
    while x - 1 >= 0 and y - 1 >= 0:
        if chessboard[x - 1][y - 1] == ' ' or chessboard[x - 1][y - 1] == '1':
            chessboard[x - 1][y - 1] = '1'
            x, y = x - 1, y - 1
        else:
            break
    x, y = temp_x, temp_y
    while x - 1 >= 0 and y + 1 <= 7:
        if chessboard[x - 1][y + 1] == ' ' or chessboard[x - 1][y + 1] == '1':
            chessboard[x - 1][y + 1] = '1'
            x, y = x - 1, y + 1
        else:
            break
    x, y = temp_x, temp_y
    while x + 1 <= 7 and y - 1 >= 0:
        if chessboard[x + 1][y - 1] == ' ' or chessboard[x + 1][y - 1] == '1':
            chessboard[x + 1][y - 1] = '1'
            x, y = x + 1, y - 1
        else:
            break
    x, y = temp_x, temp_y
    while x + 1 <= 7 and y + 1 <= 7:
        if chessboard[x + 1][y + 1] == ' ' or chessboard[x + 1][y + 1] == '1':
            chessboard[x + 1][y + 1] = '1'
            x, y = x + 1, y + 1
        else:
            break
    x, y = temp_x, temp_y
    return chessboard
def King(chessboard,x,y):
    if x - 1 >= 0:
        if chessboard[x - 1][y] == ' ' or chessboard[x - 1][y] == '1':
            chessboard[x - 1][y] = '1'
    if x + 1 <= 7:
        if chessboard[x + 1][y] == ' ' or chessboard[x + 1][y] == '1':
            chessboard[x + 1][y] = '1'
    if y - 1 >= 0:
        if chessboard[x][y - 1] == ' ' or chessboard[x][y - 1] == '1':
            chessboard[x][y - 1] = '1'
    if y + 1 <= 7:
        if chessboard[x][y + 1] == ' ' or chessboard[x][y + 1] == '1':
            chessboard[x][y + 1] = '1'
    if x - 1 >= 0 and y - 1 >= 0:
        if chessboard[x - 1][y - 1] == ' ' or chessboard[x - 1][y - 1] == '1':
            chessboard[x - 1][y - 1] = '1'
    if x - 1 >= 0 and y + 1 <= 7:
        if chessboard[x - 1][y + 1] == ' ' or chessboard[x - 1][y + 1] == '1':
            chessboard[x - 1][y + 1] = '1'
    if x + 1 <= 7 and y + 1 <= 7:
        if chessboard[x + 1][y + 1] == ' ' or chessboard[x + 1][y + 1] == '1':
            chessboard[x + 1][y + 1] = '1'
    if x + 1 <= 7 and y - 1 >= 0:
        if chessboard[x + 1][y - 1] == ' ' or chessboard[x + 1][y - 1] == '1':
            chessboard[x + 1][y - 1] = '1'
    return chessboard

color = input()
chessboard = [list(input()) for i in range(8)]
mate = True

if color == 'w':
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'K':
                king_x, king_y = i, j
                chessboard[i][j] = ' '

    for x in range(8):
        for y in range(8):
            if chessboard[x][y] == 'p':
                if x + 1 <= 7 and y + 1 <= 7:
                    if chessboard[x + 1][y + 1] == ' ' or chessboard[x + 1][y + 1] == '1':
                        chessboard[x + 1][y + 1] = '1'
                if x + 1 <= 7 and y - 1 >= 0:
                    if chessboard[x + 1][y - 1] == ' ' or chessboard[x + 1][y - 1] == '1':
                        chessboard[x + 1][y - 1] = '1'
            elif chessboard[x][y] == 'r':
                chessboard = Rook(chessboard, x, y)
            elif chessboard[x][y] == 'n':
                chessboard = Knight(chessboard, x, y)
            elif chessboard[x][y] == 'b':
                chessboard = Bishop(chessboard, x, y)
            elif chessboard[x][y] == 'q':
                chessboard = Rook(chessboard, x, y)
                chessboard = Bishop(chessboard, x, y)
            elif chessboard[x][y] == 'k':
                chessboard = King(chessboard, x, y)

if color == 'b':
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'k':
                king_x, king_y = i, j
                chessboard[i][j] = ' '

    for x in range(8):
        for y in range(8):
            if chessboard[x][y] == 'P':
                if x - 1 >= 0:
                    if y + 1 <= 7:
                        if chessboard[x - 1][y + 1] == ' ' or chessboard[x - 1][y + 1] == '1':
                            chessboard[x - 1][y + 1] = '1'
                    if y - 1 >= 0:
                        if chessboard[x - 1][y - 1] == ' ' or chessboard[x - 1][y - 1] == '1':
                            chessboard[x - 1][y - 1] = '1'
            elif chessboard[x][y] == 'R':
                chessboard = Rook(chessboard, x, y)
            elif chessboard[x][y] == 'N':
                chessboard = Knight(chessboard, x, y)
            elif chessboard[x][y] == 'B':
                chessboard = Bishop(chessboard, x, y)
            elif chessboard[x][y] == 'Q':
                chessboard = Rook(chessboard, x, y)
                chessboard = Bishop(chessboard, x, y)
            elif chessboard[x][y] == 'K':
                chessboard = King(chessboard, x, y)

x, y = king_x, king_y
if chessboard[x][y] == '1':
    if x-1 >= 0:
        if chessboard[x-1][y] == ' ':
            mate = False
    if x+1 <= 7:
        if chessboard[x+1][y] == ' ':
            mate = False
    if y-1 >= 0:
        if chessboard[x][y-1] == ' ':
            mate = False
    if y+1 <= 7:
        if chessboard[x][y+1] == ' ':
            mate = False
    if x-1 >= 0 and y-1 >= 0:
        if chessboard[x-1][y-1] == ' ':
            mate = False
    if x+1 <= 7 and y-1 >= 0:
        if chessboard[x+1][y-1] == ' ':
            mate = False
    if x+1 <= 7 and y+1 <= 7:
        if chessboard[x+1][y+1] == ' ':
            mate = False
    if x-1 >= 0 and y+1 <= 7:
        if chessboard[x-1][y+1] == ' ':
            mate = False
else:
    mate = False

if mate:
    print('mate')
else:
    print('not mate')