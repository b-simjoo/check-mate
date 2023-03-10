# -*- coding: utf-8 -*-
"""simjoo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13JUPXUglTV1H0VWqsyUqcEJx5PI36sc9
"""

# doroud
import numpy as np

AKING = 33  # giving a value to my subjects.. (allay subjects are divisible by 3, while the enemy ones aren't.)
AQUEEN = 24
ABISHOP = 21
AKNIGHT = 15
APAWN = 27
AROOK = 9
EKING = 100
EQUEEN = 31
EROOK = 98
EPAWN = 11
EKNIGHT = 52
EBISHOP = 121
colour = input()
chessboard = [list(input()) for i in range(8)]
checkboard = np.zeros((8, 8))
j = 0
x = 0
if colour == "b":  # creating a standard form, allay subjects are defined in upper case, enemy ones are in lower case
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == "R":
                chessboard[i][j] = "r"
            elif chessboard[i][j] == "r":
                chessboard[i][j] = "R"
            elif chessboard[i][j] == "K":
                chessboard[i][j] = "k"
            elif chessboard[i][j] == "k":
                chessboard[i][j] = "K"
            elif chessboard[i][j] == "N":
                chessboard[i][j] = "n"
            elif chessboard[i][j] == "n":
                chessboard[i][j] = "N"
            elif chessboard[i][j] == "P":
                chessboard[i][j] = "p"
            elif chessboard[i][j] == "p":
                chessboard[i][j] = "P"
            elif chessboard[i][j] == "Q":
                chessboard[i][j] = "q"
            elif chessboard[i][j] == "q":
                chessboard[i][j] = "Q"
            elif chessboard[i][j] == "B":
                chessboard[i][j] = "b"
            elif chessboard[i][j] == "b":
                chessboard[i][j] = "B"

j = 0
# changing the values from str to int.. (remember that allay pieces are divisible by 3 While the enemy ones aren't)
for i in chessboard:
    for s in i:
        if s == "R":
            if 7 >= j >= 0:
                checkboard[x][j] = 9
                j += 1
            if j > 7:
                j = 0
                x += 1
        elif s == " ":  # empty positions are subjects of no value, so im gonna replace them with 0 in my array
            if 7 >= j >= 0:
                checkboard[x][j] = 0
                j += 1
            if j > 7:
                j = 0
                x += 1
        elif s == "K":
            if 7 >= j >= 0:
                checkboard[x][j] = 33
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "P":
            if 7 >= j >= 0:
                checkboard[x][j] = 27
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "Q":
            if 7 >= j >= 0:
                checkboard[x][j] = 24
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "B":
            if 7 >= j >= 0:
                checkboard[x][j] = 21
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "N":
            if 7 >= j >= 0:
                checkboard[x][j] = 12
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "k":
            if 7 >= j >= 0:
                checkboard[x][j] = 100
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "q":
            if 7 >= j >= 0:
                checkboard[x][j] = 31
            if 7 >= j >= 0:
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "r":
            if 7 >= j >= 0:
                checkboard[x][j] = 98
            if 7 >= j >= 0:
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "p":
            if 7 >= j >= 0:
                checkboard[x][j] = 11
            if 7 >= j >= 0:
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "n":
            if 7 >= j >= 0:
                checkboard[x][j] = 52
            if 7 >= j >= 0:
                j += 1
            if j > 7:
                j = 0
                x += 1

        elif s == "b":
            if 7 >= j >= 0:
                checkboard[x][j] = 121
            if 7 >= j >= 0:
                j += 1
            if j > 7:
                j = 0
                x += 1
# print(checkboard)
# locating the allay king, using argwhere i can create a 2d list of my kings whereabouts
# the index 0, 0 gives me the first value of that list which is my i (radif) and the index 0 1 gives me the kings j (soton)
a_king = np.argwhere(checkboard == AKING)
x = a_king[0][0]
y = a_king[0][1]
#print(checkboard)

def is_white_checked(checkboard, x, y):
    is_check = False  # defining a boolean value that determines if my king is in checked position or not
    # checking the ORTHOGONAL positions for any allay sujects.. OR the enemys rook/queen.
    for index in range(x - 1, -1, -1):
        if checkboard[index][y] % 3 == 0 and checkboard[index][y] != 0:  # checking for allay pieces,
            break
        elif checkboard[index][y] % 3 != 0:
              if checkboard[index][y] == EROOK or checkboard[index][y] == EQUEEN:
                is_check = True
              break

    if 7 > y >= 0:
        yindex = y + 1
        for index in range(x - 1, -1,
                           -1):  # checking the diagonal position for allay subjects or enemys bishop / queen.
            # print(x)
            if checkboard[index][yindex] % 3 == 0 and checkboard[index][yindex] != 0:
                break
            elif checkboard[index][yindex] % 3 != 0:
              if checkboard[index][yindex] == EBISHOP or checkboard[index][yindex] == EQUEEN:
                is_check = True
              break
            elif 7 > yindex >= 0:
                yindex = yindex + 1
            else:
                break

    for index in range(y + 1, 8):  # checking the horizontal positions
        if checkboard[x][index] % 3 == 0 and checkboard[x][index] != 0:
            break
        elif checkboard[x][index] % 3 != 0:
              if checkboard[x][index] == EROOK or checkboard[x][index] == EQUEEN:
                is_check = True
              break
    
    if 7 > y >= 0:
        yindex = y + 1
        for index in range(x + 1, 8):
            if checkboard[index][yindex] % 3 == 0 and checkboard[index][yindex] != 0:
                break
            elif checkboard[index][yindex] % 3 != 0:
              if checkboard[index][yindex] == EBISHOP or checkboard[index][yindex] == EQUEEN:
                is_check = True
              break
            elif 7 > yindex >= 0:
                yindex = yindex + 1
            else:
                break

    for index in range(x + 1, 8):
        if checkboard[index][y] % 3 == 0 and checkboard[index][y] != 0:
            break
        elif checkboard[index][y] % 3 != 0:
              if checkboard[index][y] == EROOK or checkboard[index][y] == EQUEEN:
                is_check = True
              break

    if 7 >= y > 0:
        yindex = y - 1
        for index in range(x + 1, 8):
            if checkboard[index][yindex] % 3 == 0 and checkboard[index][yindex] != 0:
                break
            elif checkboard[index][yindex] % 3 != 0:
              if checkboard[index][yindex] == EBISHOP or checkboard[index][yindex] == EQUEEN:
                is_check = True
              break
            elif 7 >= yindex > 0:
                yindex = yindex - 1
            else:
                break

    for index in range(y - 1, -1, -1):
        if checkboard[x][index] % 3 == 0 and checkboard[x][index] != 0:
            break
        elif checkboard[x][index] % 3 != 0:
              if checkboard[x][index] == EROOK or checkboard[x][index] == EQUEEN:
                is_check = True
              break
    if 7 >= y > 0:
        yindex = y - 1
        for index in range(x - 1, -1, -1):
            if checkboard[index][yindex] % 3 == 0 and checkboard[index][yindex] != 0:
                break
            elif checkboard[index][yindex] % 3 != 0:
              if checkboard[index][yindex] == EBISHOP or checkboard[index][yindex] == EQUEEN:
                is_check = True
              break
            elif 7 >= yindex > 0:
                yindex = yindex - 1
            else:
                break
    # for knights, since knights (and chess ovar all) are so incredibly boring i haave to waste 30 something lines on them to check their moves. since this mf can move in a weird ass way.. godd i hate chess.
    i = x - 2
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x - 2
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x - 1
    j = y + 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x + 1
    j = y + 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x + 2
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True
    i = x + 2
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True
    i = x - 1
    j = y + 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x + 1
    j = y - 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x - 1
    j = y - 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True

    i = x + 1
    j = y - 2
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EKNIGHT:
            is_check = True
    # for pawns i just need to check 2 positions.. pawns are useless.. just like my degree.
    i = x - 1
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EPAWN or checkboard[i][j] == EQUEEN:
            is_check = True
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == EPAWN or checkboard[i][j] == EQUEEN:
            is_check = True

    return is_check


is_check = is_white_checked(checkboard, x, y)
# print(is_check)
# if  is_check == False:
# print("not mate")
c = 0
for i in range(x - 1,x + 2):  # counting the possible positions, that my king can move into in case it was in a checked position
    for j in range(y - 1, y + 2):
        if 7 >= i >= 0 and 7 >= j >= 0:
            if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
                c += 1
            elif checkboard[i][j] == checkboard[x][y]:
                c +=1
#print(c)

check = 0
if is_check:
    i = x
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:  # now at this point, mohre man to halat kish qarar dre, pas mn miam khone haye atrafesh ro check mikonm ta bbinm shahm mitone ba harkat krdn be yeki az in khone ha az kish dar biad ya na, man mokhtasat khone hayi ke khalian ya mohre enemy toshon qarar dre ro midm be function. va dobare check mishe ta bbinim in khone ha dar maraaz check hstn ya na.
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check1 = is_white_checked(checkboard, i, j)
            if check1:
                # print("check1")
                check += 1
    i = x - 1
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check2 = is_white_checked(checkboard, i, j)
            if check2:
                # print("check2")
                check += 1
    i = x - 1
    j = y
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check3 = is_white_checked(checkboard, i, j)
            if check3:
                # print("check3")
                check += 1
    i = x - 1
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check4 = is_white_checked(checkboard, i, j)
            if check4:
                # print("check4")
                check += 1
    i = x
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check5 = is_white_checked(checkboard, i, j)
            if check5:
                # print("check5")
                check += 1
    i = x + 1
    j = y - 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check6 = is_white_checked(checkboard, i, j)
            if check6:
                # print("check6")
                check += 1
    i = x + 1
    j = y
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check7 = is_white_checked(checkboard, i, j)
            if check7:
                # print("check7")
                check += 1
    i = x + 1
    j = y + 1
    if 7 >= i >= 0 and 7 >= j >= 0:
        if checkboard[i][j] == 0 or checkboard[i][j] % 3 != 0:
            check8 = is_white_checked(checkboard, i, j)
            if check8:
                # print("check8")
                check += 1
    
    check9 = is_white_checked(checkboard,x,y)
    if check9:
      #print("j")
      check +=1
        

#print(check, c)
#print(checkboard)
#print(x, y)

if check == c:
  print("mate")
else:
  print("not mate")