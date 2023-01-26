from sys import stderr


#------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard
#------------------------------

#------------------------------
# your code goes here
#
# debugger will scan outputs. So whatever your program prints the debugger will check it
# to print something without checking by debugger write this:
# print(<something>, file=stderr)
# replace <something> with anything you want, debugger will not check output of this line
# here is some examples, if user wants to check white this lines will write some debug lines

def Pawn(pawn, king):
    if color == "w":
        if pawn[0]+1 == king[0] and pawn[1]-1 == king[1]:
            mate = True
            return mate
        elif pawn[0]+1 == king[0] and pawn[1]+1 == king[1]:
            mate = True
            return mate
    if color == "b":
        if pawn[0]-1 == king[0] and pawn[1]+1 == king[1]:
            mate = True
            return mate
        elif pawn[0]-1 == king[0] and pawn[1]-1 == king[1]:
            mate = True
            return mate

def Rook(rook, king, chessboard):
    mate = False
    i = rook[0]
    j = rook[1]

    i = rook[0] +1
    while i != 8 :
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        i += 1

    i = rook[0] - 1
    j = rook[1]
    while i != -1 :
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        i -= 1

    i = rook[0]
    j = rook[1] + 1
    while j != 8:
        if chessboard[i][j] != " ":
            if  i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        j += 1

    i = rook[0]
    j = rook[1] - 1
    while j != -1:
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        j -= 1

    return mate

def Bishop(bishop, king, chessboard): 
    mate = False
    i = bishop[0]
    j = bishop[1]

    i = bishop[0] - 1
    j = bishop[1] + 1
    while (i > -1 and j < 8):
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        i -= 1
        j += 1
    i = bishop[0] + 1
    j = bishop[1] - 1
    while i != 8 and j != -1:
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:
                mate = True
                return mate
            else:
                break
        i += 1
        j -= 1
    i = bishop[0] - 1
    j = bishop[1] - 1
    while i != -1 and j != -1:
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:       
                mate = True
                return mate
            else:
                break
        i -= 1
        j -= 1
    i = bishop[0] + 1
    j = bishop[1] + 1  
    while i != 8 and j != 8:
        if chessboard[i][j] != " ":
            if i == king[0] and j == king[1]:    
                mate = True
                return mate
            else:
                break
        i += 1
        j += 1
    return mate

def Queen(queen, king, chessboard):
    B = Bishop(queen, king, chessboard)
    if B == False:
        return Rook(queen, king,chessboard)
    return B

def Knight(knight, king):
    if knight[0]+2 == king[0] and knight[1]+1 == king[1]:
            mate = True
            return mate
    elif knight[0]+2 == king[0] and knight[1]-1 == king[1]:
            mate = True
            return mate
    elif knight[0]-2 == king[0] and knight[1]+1 == king[1]:
            mate = True
            return mate
    elif knight[0]-2 == king[0] and knight[1]-1 == king[1]:
            mate = True
            return mate
    elif knight[0]+1 == king[0] and knight[1]+2 == king[1]:
            mate = True
            return mate
    elif knight[0]-1 == king[0] and knight[1]+2 == king[1]:
            mate = True
            return mate
    elif knight[0]+1 == king[0] and knight[1]-2 == king[1]:
            mate = True
            return mate
    elif knight[0]-1 == king[0] and knight[1]-2 == king[1]:
            mate = True
            return mate

def check_mate(chessboard, king):
    if color == 'w':
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "p":
                    pawn = [i,j]
                    if Pawn(pawn, king) == True:
                        return "mate"                

                if chessboard[i][j] == "r":
                    rook = [i,j]
                    if Rook(rook, king, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "n":
                    knight = [i,j]
                    if Knight(knight, king) == True:
                        return "mate"

                if chessboard[i][j] == "b":
                    bishop = [i,j]
                    if Bishop(bishop, king, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "q":
                    queen = [i,j]
                    if Queen(queen, king, chessboard) == True:
                        return "mate"
        else:
            return "not mate"

    if color == 'b':
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "P":
                    pawn = [i,j]
                    if Pawn(pawn, king) == True:
                        return "mate"  

                if chessboard[i][j] == "R":
                    rook = [i,j]
                    if Rook(rook, king, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "N":
                    knight = [i,j]
                    if Knight(knight, king) == True:
                        return "mate"

                if chessboard[i][j] == "B":
                    bishop = [i,j]
                    if Bishop(bishop, king, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "Q":
                    queen = [i,j]
                    if Queen(queen, king, chessboard) == True:
                        return "mate"
        else:
            return "not mate"

# پیدا کردن شاه و  برسی شاه
if color == 'w':
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == "K":
                king = [i, j]
if color == "b":
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == "k":
                king = [i, j]
mate = False
if check_mate(chessboard, king) == "mate":
    mate = True

# پیدا کردن خانه های امن اطراف شاه
def find_safe_places(chessboard, king):
    safe_places = []
    i = king[0]
    j = king[1]
    if -1 < i-1 < 8 and -1 < j-1 < 8 and chessboard[i - 1][j - 1] == " ":
        safe_places.append([i-1 , j-1])

    if -1 < i-1 < 8 and -1 < j < 8 and chessboard[i - 1][j] == " ":
        safe_places.append([i-1 , j])

    if -1 < i-1 < 8 and -1 < j+1 < 8 and chessboard[i - 1][j + 1] == " ":
        safe_places.append([i-1 , j+1])

    if -1 < i < 8 and -1 < j+1 < 8 and chessboard[i][j + 1] == " ":
        safe_places.append([i , j+1])

    if -1 < i+1 < 8 and -1 < j+1 < 8 and chessboard[i + 1][j + 1] == " ":
        safe_places.append([i+1 , j+1])

    if -1 < i+1 < 8 and -1 < j < 8 and chessboard[i + 1][j] == " ":
        safe_places.append([i+1 , j])

    if -1 < i+1 < 8 and -1 < j-1 < 8 and chessboard[i + 1][j - 1] == " ":
        safe_places.append([i+1 , j-1])

    if -1 < i < 8 and -1 < j-1 < 8 and chessboard[i][j - 1] == " ":
        safe_places.append([i , j-1])                               # output class is list
    return safe_places

# برسی خانه های امن اطراف شاه
if mate == True:
    for king in find_safe_places(chessboard, king):
        chessboard[king[0]][king[1]] = "S"
        if check_mate(chessboard, king) == "not mate":
            mate = False
            break
        chessboard[king[0]][king[1]] = " "

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