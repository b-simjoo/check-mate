from sys import stderr

def limit_num(num):
     if num > 7:
          return 7
     elif num < 0:
          return 0
     else:
          return num
def index_chessboard(row , column):
    if (0 <= row <= 7) and (0 <= column <= 7):
          return chessboard[row][column]
    else:
          return None
def chess_piece(piece,color):
     if color == 'w':
          return piece.upper()
     elif color == 'b':
          return piece.lower()
#------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard
#------------------------------
checkboard = [list(chessboard[i]) for i in range(8)]
if color == 'w':
     oppcolor = 'b'
     king = 'K'
elif color == 'b':
     oppcolor = 'w'
     king = 'k'
for row in range(8):
     for column in range(8):
          if chessboard[row][column] == king:
               king_row = row
               king_column = column
for row in range(limit_num(king_row-1) , limit_num(king_row+1)+1):
     for column in range(limit_num(king_column-1) , limit_num(king_column+1)+1):
        #Block
        if chessboard[row][column] != ' ' and chessboard[row][column] != king:
            checkboard[row][column] = 1
            continue
        #Pawn
        if color == 'w':
            if index_chessboard(row - 1, column - 1) == chess_piece('p', oppcolor)\
            or index_chessboard(row - 1, column + 1) == chess_piece('p', oppcolor):
                checkboard[row][column] = 1
                continue
        if color == 'b':
            if index_chessboard(row + 1, column - 1) == chess_piece('p', oppcolor)\
            or index_chessboard(row + 1, column + 1) == chess_piece('p', oppcolor):
                checkboard[row][column] = 1
                continue
        #Knight
        elif index_chessboard(row - 2 , column - 1) == chess_piece('n', oppcolor)\
        or index_chessboard(row - 1 , column - 2) == chess_piece('n', oppcolor)\
        or index_chessboard(row + 1 , column - 2) == chess_piece('n', oppcolor)\
        or index_chessboard(row + 2 , column - 1) == chess_piece('n', oppcolor)\
        or index_chessboard(row - 2 , column + 1) == chess_piece('n', oppcolor)\
        or index_chessboard(row - 1 , column + 2) == chess_piece('n', oppcolor)\
        or index_chessboard(row + 1 , column + 2) == chess_piece('n', oppcolor)\
        or index_chessboard(row + 2 , column + 1) == chess_piece('n', oppcolor):
               checkboard[row][column] = 1
               continue
        #King
        for i in range(limit_num(row - 1),limit_num(row + 1)+1):
            for j in range (limit_num(column -1),limit_num(column + 1)+1):
                if i == row and j == column:
                    continue
                elif index_chessboard(i,j) == chess_piece('k', oppcolor):
                    checkboard[row][column] = 1
        if checkboard == 1:
            continue
          #Queen&Rook
        for i in range(limit_num(row-1),0,-1):
            if (index_chessboard(i,column) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,column) == chess_piece('r',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,column) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,column) != chess_piece('r',oppcolor)) and\
            index_chessboard(i,column) != ' ':
                break
        if checkboard == 1:
               continue
        for i in range(limit_num(row+1),8):
            if (index_chessboard(i,column) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,column) == chess_piece('r',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,column) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,column) != chess_piece('r',oppcolor)) and\
            index_chessboard(i,column) != ' ':
                break
        if checkboard == 1:
            continue
        for i in range(limit_num(column-1),0,-1):
            if (index_chessboard(row,i) == chess_piece('q',oppcolor)) or\
            (index_chessboard(row,i) == chess_piece('r',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(row,i) != chess_piece('q',oppcolor)) and\
            (index_chessboard(row,i) != chess_piece('r',oppcolor)) and\
            index_chessboard(row,i) != ' ':
                break
        if checkboard == 1:
            continue
        for i in range(limit_num(column+1),8):
            if (index_chessboard(row,i) == chess_piece('q',oppcolor)) or\
            (index_chessboard(row,i) == chess_piece('r',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(row,i) != chess_piece('q',oppcolor)) and\
            (index_chessboard(row,i) != chess_piece('r',oppcolor)) and\
            index_chessboard(row,i) != ' ':
                break
        if checkboard == 1:
            continue
        #Queen&Bishop
        i = row - 1
        j = column - 1
        while index_chessboard(i,j) != None:
            if (index_chessboard(i,j) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,j) == chess_piece('b',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,j) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,j) != chess_piece('b',oppcolor)) and\
            index_chessboard(i,j) != ' ':
                break
            i -= 1
            j -= 1
        if checkboard == 1:
            continue
        i = row + 1
        j = column - 1
        while index_chessboard(i,j) != None:
            if (index_chessboard(i,j) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,j) == chess_piece('b',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,j) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,j) != chess_piece('b',oppcolor)) and\
            index_chessboard(i,j) != ' ':
                break
            i += 1
            j -= 1
        if checkboard == 1:
            continue
        i = row - 1
        j = column + 1
        while index_chessboard(i,j) != None:
            if (index_chessboard(i,j) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,j) == chess_piece('b',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,j) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,j) != chess_piece('b',oppcolor)) and\
            index_chessboard(i,j) != ' ':
                break
            i -= 1
            j += 1
        if checkboard == 1:
            continue
        i = row + 1
        j = column + 1
        while index_chessboard(i,j) != None:
            if (index_chessboard(i,j) == chess_piece('q',oppcolor)) or\
            (index_chessboard(i,j) == chess_piece('b',oppcolor)):
                checkboard[row][column] = 1
                break
            elif (index_chessboard(i,j) != chess_piece('q',oppcolor)) and\
            (index_chessboard(i,j) != chess_piece('b',oppcolor)) and\
            index_chessboard(i,j) != ' ':
                    break
            i += 1
            j += 1
        if checkboard == 1:
            continue
mate = True
for row in range(limit_num(king_row-1) , limit_num(king_row+1)+1):
     for column in range(limit_num(king_column-1) , limit_num(king_column+1)+1):
          if checkboard[row][column] !=  1:
               mate = False
if mate:
    print('mate')
else:
    print('not mate')
