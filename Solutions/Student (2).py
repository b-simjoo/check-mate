import numpy as np

# a = [[" ","P"," "," "," "," ","B","P"],[" "," ","b","r","n"," "," "," "],[" ","N"," "," ","K","q","N"," "],[" "," "," ","p","Q"," ","r"," "],[" ","p","n"," "," ","p","P","P"],[" "," "," "," "," ","p","b","k"]]

# get_color
color = input()
a = [list(input()) for _ in range(8)]
b = np.zeros((8, 9))
# get_loc
for i in range(6):
    for j in range(8):
        if a[i][j] == "P":
            b[i][j] = 2
        elif a[i][j] == "p":
            b[i][j] = 20
        elif a[i][j] == "R":
            b[i][j] = 3
        elif a[i][j] == "r":
            b[i][j] = 30
        elif a[i][j] == "B":
            b[i][j] = 5
        elif a[i][j] == "b":
            b[i][j] = 50
        elif a[i][j] == "N":
            b[i][j] = 4
        elif a[i][j] == "n":
            b[i][j] = 40
        elif a[i][j] == "Q":
            b[i][j] = 6
        elif a[i][j] == "q":
            b[i][j] = 60
        elif a[i][j] == "K":
            b[0][8] = i
            b[1][8] = j
        elif a[i][j] == "k":
            b[6][8] = i
            b[7][8] = j
# r = 3 , p = 2 ,  n = 4 ,  q = 6 , b = 5 , k = 0
# def check and r_move and b_move and n_move
def check():
    if b[i][j] == 0:
        print("not mate")
    elif i - 1 > -1 and j - 1 > -1 and b[i - 1][j - 1] == 0:
        print("not mate")
    elif i + 1 < 8 and j - 1 > -1 and b[i + 1][j - 1] == 0:
        print("not mate")
    elif i - 1 > -1 and j + 1 < 8 and b[i - 1][j + 1] == 0:
        print("not mate")
    elif i + 1 < 8 and j + 1 < 8 and b[i + 1][j + 1] == 0:
        print("not mate")
    elif j + 1 < 8 and b[i][j + 1]:
        print("not mate")
    elif j - 1 > -1 and b[i][j - 1] == 0:
        print("not mate")
    elif i - 1 > -1 and b[i - 1][j] == 0:
        print("not mate")
    elif i + 1 < 8 and b[i + 1][j] == 0:
        print("not mate")
    else:
        print("mate")


def r_move():
    for c in range(j + 1, 8):
        if b[i][c] == 0:
            b[i][c] = 33
        else:
            break
    for c in range(j - 1, -1, -1):
        if b[i][c] == 0:
            b[i][c] = 33
        else:
            break
    for c in range(i + 1, 8):
        if b[c][j] == 0:
            b[c][j] = 33
        else:
            break
    for c in range(i - 1, -1, -1):
        if b[c][j] == 0:
            b[c][j] = 33
        else:
            break


def b_move():
    for c in range(i + 1, 8):
        for v in range(j + 1, 8):
            if b[c][v] == 0:
                b[c][v] = 55
            else:
                break
        if b[c][v] != 0:
            break
    for c in range(i - 1, -1, -1):
        for v in range(j - 1, -1, -1):
            if b[c][v] == 0:
                b[c][v] = 55
            else:
                break
        if b[c][v] != 0:
            break
    for c in range(i + 1, 8):
        for v in range(j - 1, -1, -1):
            if b[c][v] == 0:
                b[c][v] = 55
            else:
                break
        if b[c][v] != 0:
            break
    for c in range(i - 1, -1, -1):
        for v in range(j + 1, 8):
            if b[c][v] == 0:
                b[c][v] = 55
            else:
                break
        if b[c][v] != 0:
            break


def n_move():
    if i + 2 < 8 and j - 1 > -1 and b[i + 2][j - 1] == 0:
        b[i + 2][j - 1] = 44
    elif i + 2 < 8 and j + 1 < 8 and b[i + 2][j + 1] == 0:
        b[i + 2][j + 1] = 44
    elif i - 2 > -1 and j + 1 < 8 and b[i - 2][j + 1] == 0:
        b[i - 2][j + 1] = 44
    elif i - 2 > -1 and j - 1 > -1 and b[i - 2][j - 1] == 0:
        b[i - 2][j - 1] = 44
    elif j + 2 < 8 and i - 1 > -1 and b[i - 1][j + 2] == 0:
        b[i - 1][j + 2] = 44
    elif j + 2 < 8 and i + 1 < 8 and b[i + 1][j + 2] == 0:
        b[i + 1][j + 2] = 44
    elif j - 2 > -1 and i + 1 < 8 and b[i + 1][j - 2] == 0:
        b[i + 1][j - 2] = 44
    elif j - 2 > -1 and i - 1 > -1 and b[i - 1][j - 2] == 0:
        b[i - 1][j - 2] = 44


if color == "w":
    for i in range(8):
        for j in range(8):
            # P_move
            if b[i][j] == 2:
                if i - 1 > -1 and j - 1 > -1 and b[i - 1][j - 1] == 0:
                    b[i - 1][j + 1] = 22
                elif i - 1 > -1 and j + 1 < 8 and b[i - 1][j + 1] == 0:
                    b[i - 1][j - 1] = 22
            # R_move
            elif b[i][j] == 3:
                r_move()
            # B_move
            elif b[i][j] == 5:
                b_move()
            # N_move
            elif b[i][j] == 4:
                n_move()
            # Q_move = R_move + B_move
            elif b[i][j] == 6:
                r_move()
                b_move()
    # mate_not mate
    i = int(b[6][8])
    j = int(b[7][8])
    check()
else:
    for i in range(8):
        for j in range(8):
            # P_move
            if b[i][j] == 20:
                if i + 1 > -1 and j - 1 > -1 and b[i + 1][j - 1] == 0:
                    b[i + 1][j - 1] = 2
                if i + 1 > -1 and j + 1 < 8 and b[i + 1][j + 1] == 0:
                    b[i + 1][j + 1] = 2
            # R_move
            elif b[i][j] == 30:
                r_move()
            # B_move
            elif b[i][j] == 50:
                b_move()
            # N_move
            elif b[i][j] == 40:
                n_move()
            # Q_move = R_move + B_move
            elif b[i][j] == 60:
                r_move()
                b_move()
    # mate_not mate
    i = int(b[0][8])
    j = int(b[1][8])
    check()
