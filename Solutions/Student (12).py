from sys import stderr

#------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard
#------------------------------
# your code goes here
# debugger will scan outputs. So whatever your program prints the debugger will check it
# to print something without checking by debugger write this:
# print(<something>, file=stderr)
# replace <something> with anything you want, debugger will not check output of this line
# here is some examples, if user wants to check white this lines will write some debug lines

if color == 'w':
    print('Yo Mr.White', file=stderr)
elif color == 'b':
    print('Yo Mr.Black', file=stderr)

for i in range(8):
    print(chessboard[i], file=stderr )
#-------------------------------------------------
def kingfinder():           # To find the location of the king and save it
    global king_position    # Global definition "king_position" to have access in all functions
    king_position = () 
    if color == 'b':
        king = 'k'
        for i in range(8):                  # To move in row 
            for j in range(8):              # To move in the column
                if chessboard[i][j] == king:
                    king_position = (i,j)        # Add the position of the king in "king_position", "i" means row index and "j" means column index
    elif color == 'w':
        king = 'K'
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == king:
                    king_position = (i,j)
kingfinder()

def king_options():
    x = king_position[0]
    y = king_position[1]
    around_king_x =[]
    around_king_y = []
    i = x-1
    while (i<x+2):
        j = y-1
        while(j<y+2):
            if i >= 0 and j >= 0:
                if i <= 7 and j <= 7:
                    if i != x or j != y:
                        around_king_x.append(i)
                        around_king_y.append(j)
            j += 1
        i += 1

    global king_options_x
    king_options_x = []
    global king_options_y
    king_options_y = []
    for i in range(len(around_king_x)):     # len around_king_x and around_king_y not different, do not matter each one be here.
        if color == 'w':
            x = around_king_x[i]
            y = around_king_y[i]
            if chessboard[x][y].islower() or chessboard[x][y] == ' ':
                king_options_x.append(x)
                king_options_y.append(y)
        elif color == 'b':
            x = around_king_x[i]
            y = around_king_y[i]
            if chessboard[x][y].isupper() or chessboard[x][y] == ' ':
                king_options_x.append(x)
                king_options_y.append(y)

def enemy_character():
    global ene_rook; global ene_bishop; global ene_queen; global ene_knight; global ene_pawn;
    if color == 'w':
        ene_rook = 'r'; ene_bishop = 'b'; ene_queen = 'q'; ene_knight = 'n'; ene_pawn = 'p';
    elif color == 'b':
        ene_rook = 'R'; ene_bishop = 'B'; ene_queen = 'Q'; ene_knight = 'N'; ene_pawn = 'P';

def horizontal_vertical_menace(x=king_position[0], y=king_position[1]):
    menace = False
    # right side
    i = x
    j = y + 1
    while j < 8:
        if chessboard[i][j] == ene_rook or chessboard[i][j] == ene_queen:
            menace = True   
            break
        elif chessboard[i][j] != ' ':
            break
        j += 1
    if menace:
        return menace

    # left side
    i = x
    j = y - 1    
    while j >= 0:
        if chessboard[i][j] == ene_rook or chessboard[i][j] == ene_queen:
            menace = True    
            break
        elif chessboard[i][j] != ' ':    
            break
        j -= 1
    if menace:
        return menace

    # high side
    i = x - 1
    j = y
    while i >= 0:
        if chessboard[i][j] == ene_rook or chessboard[i][j] == ene_queen:
            menace = True 
            break
        elif chessboard[i][j] != ' ':    
            break
        i -= 1
    if menace:
        return menace

    # down side
    i = x + 1
    j = y
    while i < 8:
        if chessboard[i][j] == ene_rook or chessboard[i][j] == ene_queen:
            menace = True  
            break
        elif chessboard[i][j] != ' ':
            break
        i += 1
    if menace:
        return menace

def diagonal_menace(x=king_position[0],y=king_position[1]):
    menace = False
    # up right 
    i = x - 1
    j = y + 1
    while j < 8 and i >= 0:           
        if chessboard[i][j] == ene_bishop or chessboard[i][j] == ene_queen:
                menace = True
                break
        elif chessboard[i][j] != ' ':
            break
        i -= 1
        j += 1

    if menace:
        return menace
    
    # up left
    i = x - 1
    j = y - 1
    while j >= 0 and i >= 0:           
        if chessboard[i][j] == ene_bishop or chessboard[i][j] == ene_queen:
            menace = True
            break
        elif chessboard[i][j] != ' ':
            break
        i -= 1
        j -= 1

    if menace:
        return menace
    # down right
    i = x + 1
    j = y + 1
    while j < 8 and i < 8:            
        if chessboard[i][j] == ene_bishop or chessboard[i][j] == ene_queen:
                menace = True
                break
        elif chessboard[i][j] != ' ':
            break
        i += 1
        j += 1

    if menace:
        return menace
    
    # down left
    i = x + 1
    j = y - 1
    while i < 8 and j >= 0:            
        if chessboard[i][j] == ene_bishop or chessboard[i][j] == ene_queen:
                menace = True
                break
        elif chessboard[i][j] != ' ':
            break
        i += 1
        j -= 1

    if menace:
        return menace

def knight_menace(x=king_position[0], y=king_position[1]):
    menace = False
    i = x
    j = y
    kn_x = [i-1,i-2,i-2,i-1,i+1,i+2,i+2,i+1]
    kn_y = [j-2,j-1,j+1,j+2,j-2,j-1,j+1,j+2]

    for n in range(len(kn_x)):
        if 8 > kn_x[n] >= 0 and 8 > kn_y[n] >=0:
            if chessboard[kn_x[n]][kn_y[n]] == ene_knight:
                menace = True
                break
    return menace

def pawn_menace(x=king_position[0], y=king_position[1]):
    menace = False
    if color == 'w':
        i = x-1
        j = y-1
        while j <= y+1:
            if chessboard[i][j] == ene_pawn:
                menace = True
                break
            j += 2
    elif color == 'b':
        i = x+1
        j = y-1
        while j <= y+1:
            if chessboard[i][j] == ene_pawn:
                menace = True
                break
            j += 2
    return menace

def main():
    maate = False
    kish = None
    option_menace = None
    #kingfinder()
    king_options()
    enemy_character()
    while True:
        if horizontal_vertical_menace():
            kish = True
            break
        elif diagonal_menace():
            kish = True
            break
        elif knight_menace():
            kish = True
            break
        elif pawn_menace():
            kish = True
            break
        else:
            break
    
    if kish and len(king_options_x) > 0:
        for n in range(len(king_options_x)):
            while True:
                if horizontal_vertical_menace(king_options_x[n], king_options_y[n]):
                    option_menace = True
                    break
                elif diagonal_menace(king_options_x[n], king_options_y[n]):
                    option_menace = True
                    break
                elif knight_menace(king_options_x[n], king_options_y[n]):
                    option_menace = True
                    break
                elif pawn_menace(king_options_x[n], king_options_y[n]):
                    option_menace = True
                    break
                else:
                    break
            if option_menace == False:
                break
        if option_menace:
            maate = True
    elif kish and len(king_options_x) == 0:
        maate = True
    
    return maate

#________________________________________________________
main()

if main():
    mate = True
else:
    mate = False
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
