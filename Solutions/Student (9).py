from sys import stderr

def not_same_color(king_color, chess_piece):
    if king_color == 'b' and chess_piece.isupper():
        return True

    elif king_color == 'w' and chess_piece.islower():
        return True


def find_king(color):
    if color == 'b':
        k = 'k'
    elif color == 'w':
        k = 'K'
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == k:
                return i,j              

def is_kish(k_i,k_j, color):

    # go to up
    for i in range(k_i-1,-1,-1): # k_i - 1 becuase ignore king
        piece = chessboard[i][k_j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'r' or piece == 'R' or piece == 'q' or piece == 'Q':
                    return True
                else:
                    break
            else:
                break


    # go to down
    for i in range(k_i+1,8): # k_i + 1 becuase ignore king
        piece = chessboard[i][k_j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'r' or piece == 'R' or piece == 'q' or piece == 'Q':
                    return True
                else:
                    break
            else:
                break

    # go to right
    for j in range(k_j + 1, 8):
        piece = chessboard[k_i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'r' or piece == 'R' or piece == 'q' or piece == 'Q':
                    return True
                else:
                    break
            else:
                break

    # go to left
    for j in range(k_j -1, -1, -1):
        piece = chessboard[k_i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'r' or piece == 'R' or piece == 'q' or piece == 'Q':
                    return True
                else:
                    break
            else:
                break


    # go to up right
    i = k_i-1
    j = k_j+1
    while i >= 0 and j <= 7:
        piece = chessboard[i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'b' or piece == 'B' or piece == 'q' or piece == 'Q':
                    return True
                elif  (piece == 'p' or piece == 'P') and (k_j - j == -1 and k_i - i == 1 ):
                    return True
                else:
                    break
            else:
                break
        i -= 1
        j += 1

    #go to up left
    i = k_i-1
    j = k_j-1
    while i>=0 and j>=0:
        piece = chessboard[i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'b' or piece == 'B' or piece == 'q' or piece == 'Q':
                    return True
                elif (piece == 'p' or piece == 'P') and (k_j - j == 1 and k_i - i == 1 ):
                    return True
                else:
                    break
            else:
                break
        i-=1
        j-=1

    #go to down right
    i = k_i+1
    j = k_j+1
    while i<=7 and j<=7:
        piece = chessboard[i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'b' or piece == 'B' or piece == 'q' or piece == 'Q':
                    return True
                elif (piece == 'p' or piece == 'P') and (k_j - j == -1 and k_i - i == -1 ):
                    return True
                else:
                    break
            else:
                break
        i+=1
        j+=1

    #go to down left
    i = k_i+1
    j = k_j-1
    while i<=7 and j>=0:
        piece = chessboard[i][j]
        if piece != " ":
            if not_same_color(color, piece):
                if piece == 'b' or piece == 'B' or piece == 'q' or piece == 'Q':
                    return True
                elif (piece == 'p' or piece == 'P') and (k_j - j == 1 and k_i - i == -1 ):
                    return True
                else:
                    break
            else:
                break
        i+=1
        j-=1

    # check knight
    horse_positions = [
        [k_i-1, k_j+2],
        [k_i+1, k_j+2],
        [k_i-2, k_j+1],
        [k_i-2, k_j-1],
        [k_i-1, k_j-2],
        [k_i+1, k_j-2],
        [k_i+2, k_j-1],
        [k_i+2, k_j+1]
        ]

    for pos in horse_positions:
        h_i = pos[0]
        h_j = pos[1]
        if 0 <= h_i <=7 and 0 <= h_j <= 7:
            piece = chessboard[h_i][h_j]
            if not_same_color(color, piece):
                if piece == 'n' or piece == 'N':
                    return True

    return False

def is_mate(k_i, k_j, color):
    king_position = [
        [k_i-1, k_j],
        [k_i-1, k_j+1],
        [k_i, k_j+1],
        [k_i+1, k_j+1],
        [k_i+1, k_j],
        [k_i+1, k_j-1],
        [k_i, k_j-1],
        [k_i-1, k_j-1],
    ]

    if is_kish(k_i, k_j, color) is False:
        return False

    for pos in king_position:
        i_index = pos[0]
        j_index = pos[1]
        if 0 <= i_index <=7 and 0 <= j_index <= 7:
            piece = chessboard[i_index][j_index]
            if piece == " ":
                if is_kish(i_index,j_index,color) is False :
                    return False
    
    return True


color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard


if color == 'w':
    print('Yo Mr.White', file=stderr)

mate = False
k_pos = find_king(color)
mate = is_mate(k_pos[0], k_pos[1], color)

if mate:
    print('mate')
else:
    print('not mate')