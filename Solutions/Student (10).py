from sys import stderr
import numpy as np

#------------------------------
# use lines below to get inputs
# it is recommended to don't change this lines
color = input()                                       # get color
#------------------------------
if color == "w":
    shah = "King"
else:
    shah = "king"

name_chess = ["pawan", "rook", "kinght", "bishop", "gueen", "king", " "]

for i in range (8):              # get chessboard
    for j in range(8):
        chessboard[i][j] = input()            
        if shah in chessboard[i][j]:
            home_shah = chessboard[i][j]         # find king
            i_shah = i
            j_shah = j


if color == "b":
    name_chess = name_chese.capitalize()

i_shah = i_shah - 1
j_shah = j_shah - 1
i_king = i_shah
j_king = j_shah
kish = True
while kish :
    for n in range(3):
        for m in range(3):
            if i_shah >= 0 and j_shah >= 0:
                c = i_shah + 1
                s = j_shah + 1    
                for k in range(2):
                    if c > 7 or c < 0 or s > 7 or s < 0:                          # checking pawan
                        kish1 = False
                        print("kish nisti", file=stderr)  
                    else:
                        if name_chese[0] in chessboard[c][s]:
                            kish1 = True
                            print("kish hasti", file=stderr)
                            break
                        else:
                            kish1 = False
                            print("kish nisti", file=stderr)
                    s = s - 2 
                
                while -1 < i < 8 and -1 < j < 8 :       # checking rook
                    i = 0
                    j = j_shah
                    if name_chese[1] in chessboard[i][j]:
                        kish2= True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                if kish1 or kish2 is True:
                    kish1 = True
                while -1 > i > 8 and -1 > j > 8 :
                    j = 0
                    i = i_shah
                    if name_chese[1] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    j += 1
                if kish1 or kish2 is True:
                    kish1 = True

                j = j_shah + 2
                i = i_shah + 1
                for k in range(2):                        # checking kinght
                    if -1 < i < 8 and -1 < j < 8:
                        if name_chese[2] in chessboard[i][j]:
                            kish2 = True
                            print("kish hasti", file=stderr)
                            break
                        else:
                            kish2 = False
                            print("kish nisti", file=stderr)
                        i = i - 2
                if kish1 or kish2 is True:
                    kish1 = True

                j = j_shah - 2
                i = i_shah + 1
                for k in range (2):
                    if -1 < i < 8 and -1 < j < 8:
                        if name_chese[2] in chessboard[i][j]:
                            kish2 = True
                            print("kish hasti", file=stderr)
                            break
                        else:
                            kish2 = False
                            print("kish nisti", file=stderr)
                        i = i - 2
                if kish1 or kish2 is True:
                    kish1 = True

                i = i_shah + 2
                j = j_shah + 1
                for k in range (2):
                    if -1 < i < 8 and -1 < j < 8:
                        if name_chese[2] in chessboard[i][j]:
                            kish2 = True
                            print("kish hasti", file=stderr)
                            break
                        else:
                            kish2 = False
                            print("kish nisti", file=stderr)
                        j = j - 2  
                if kish1 or kish2 is True:
                    kish1 = True

                i = i_shah - 2
                j = j_shah + 1
                for k in range (2):
                    if -1 < i < 8 and -1 < j < 8:
                        if name_chese[2] in chessboard[i][j]:
                            kish2 = True
                            print("kish hasti", file=stderr)
                            break
                        else:
                            kish2 = False
                            print("kish nisti", file=stderr)
                        j = j - 2 
                if kish1 or kish2 is True:
                    kish1 = True

                i = i_shah
                j = j_shah
                while -1 < i < 8 and -1 < j < 8:                     # checking bishop
                    i -= 1
                    j -= 1
                while -1 < i < 8 and -1 < j < 8:
                    if name_chese[3] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                    j += 1
                if kish1 or kish2 is True:
                    kish1 = True

                while -1 < i < 8 and -1 < j < 8:
                    i -= 1
                    j += 1
                while -1 < i < 8 and -1 < j < 8:
                    if name_chese[3] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                    j -= 1
                if kish1 or kish2 is True:
                    kish1 = True
    
                while -1 < i < 8 and -1 < j < 8 :       # checking queen
                    i = 0
                    j = j_shah
                    if name_chese[4] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                if kish1 or kish2 is True:
                    kish1 = True

                while -1 < i < 8 and -1 < j < 8 :
                    j = 0
                    i = i_shah
                    if name_chese[4] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    j += 1
                if kish1 or kish2 is True:
                    kish1 = True

                i = i_shah
                j = j_shah
                while -1 < i < 8 and -1 < j < 8:                 
                    i -= 1
                    j -= 1
                while i < 7 and j < 7:
                    if name_chese[4] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                    j += 1
                if kish1 or kish2 is True:
                    kish1 = True

                while -1 < i < 8 and -1 < j < 8 :
                    i -= 1
                    j += 1
                while i < 7 and j < 7:
                    if name_chese[4] in chessboard[i][j]:
                        kish2 = True
                        print("kish hasti", file=stderr)
                        break
                    else:
                        kish2 = False
                        print("kish nisti", file=stderr)
                    i += 1
                    j -= 1
                if kish1 or kish2 is True:
                    kish = True
                    print("kish", file=stderr)
                else:
                    print("not kish", file=stderr)
                    break

            i_shah += 1

        i_shah = i_king
        j_shah += 1


if kish:
    print('mate')
else:
    print('not mate')