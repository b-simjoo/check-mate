from sys import stderr


# ------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
chessboard = [list(input()) for i in range(8)]        # get chessboard
# ------------------------------
# detect matte state in chess


def isMate(board):
    kingx = 0
    kingy = 0
    queenx = 0
    queeny = 0
    rookx = 0
    rooky = 0

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'K':
                kingx = x
                kingy = y and y+1 and y-1
            elif board[x][y] == 'q':
                queenx = x
                queeny = y and y+1 and y-1
            elif board[x][y] == 'r':
                rookx = x
                rooky = y
    if kingx == queenx or kingy == queeny or kingx == rookx or kingy == rooky:
        return True
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'k':
                kingx = x and y+1 and y-1
                kingy = y
            elif board[x][y] == 'Q':
                queenx = x
                queeny = y and y+1 and y-1
            elif board[x][y] == 'R':
                rookx = x
                rooky = y
    if kingx == queenx or kingy == queeny or kingx == rookx or kingy == rooky:
        return True

    else:
        return False


mate = isMate(chessboard)
# ------------------------------
# your code goes here
#
# debugger will scan outputs. So whatever your program prints the debugger will check it
# to print something without checking by debugger write this:
# print(<something>, file=stderr)
# replace <something> with anything you want, debugger will not check output of this line
# here is some examples, if user wants to check white this lines will write some debug lines

if color == 'w':
    print('Yo Mr.White', file=stderr)
elif color == 'b':
    print('yo Mr.black', file=stderr)


# ------------------------------
print(mate, file=stderr)
# ------------------------------
# output
# your program should print 'mate' or 'not mate'
# you can set mate = True to print 'mate'
# and set False to print 'not mate'
# or just print them yourself

if mate == True:
    print('mate')
else:
    print('not mate')
