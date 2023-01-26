from sys import stderr
import numpy as np


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
# to print something without checshah by debugger write this:
# print(<something>, file=stderr)
# replace <something> with anything you want, debugger will not check output of this line
# here is some examples, if user wants to check white this lines will write some debug lines

mate = False
# -------------- Yaftane makane Shah -------------- #
if color == 'w':
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == "K":
                shah = [i,j]
if color == "b":
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == "k":
                shah = [i,j]

# -------------- Yaftane khane haye farare Shah  
loc = []
esc = []
i = shah[0]
j = shah[1]
if -1 < i-1 < 8 and -1 < j-1 < 8:
    if chessboard[i-1,j-1] == " ":
        loc.append(i-1) , loc.append(j-1)
        esc.append(loc)
loc = []
if -1 < i-1 < 8 and -1 < j < 8:      
    if chessboard[i-1,j] == " ":
        loc.append(i-1) , loc.append(j)
        esc.append(loc)
loc = []
if -1 < i-1 < 8 and -1 < j+1 < 8:
    if chessboard[i-1,j+1] == " ":
        loc.append(i-1) , loc.append(j+1)
        esc.append(loc)
loc = []
if -1 < i < 8 and -1 < j+1 < 8:       
    if chessboard[i,j+1] == " ":
        loc.append(i) , loc.append(j+1)
        esc.append(loc)
loc = []
if -1 < i+1 < 8 and -1 < j+1 < 8:       
    if chessboard[i+1,j+1] == " ":
        loc.append(i+1) , loc.append(j+1)
        esc.append(loc)
loc = []
if -1 < i+1 < 8 and -1 < j < 8:       
    if chessboard[i+1,j] == " ":
        loc.append(i+1) , loc.append(j)
        esc.append(loc)
loc = []
if -1 < i+1 < 8 and -1 < j-1 < 8:       
    if chessboard[i+1,j-1] == " ":
        loc.append(i+1) , loc.append(j-1)
        esc.append(loc)
loc = []
if -1 < i < 8 and -1 < j-1 < 8:       
    if chessboard[i,j-1] == " ":
        loc.append(i) , loc.append(j-1)
        esc.append(loc)
          
          
# ------------------- Tarife tahdid haye Sarbaz ------------------- #
def Sarbaz_check(shah, sarbaz):
    if color == "b":
        if sarbaz[0]-1 == shah[0] and sarbaz[1]+1 == shah[1]:
            mate = True
            return mate
        elif sarbaz[0]-1 == shah[0] and shah[1]-1 == shah[1]:
            mate = True
            return mate
    if color == "w":
        if sarbaz[0]+1 == shah[0] and sarbaz[1]-1 == shah[1]:
            mate = True
            return mate
        elif shah[0]+1 == shah[0] and shah[1]+1 == sarbaz[1]:
            mate = True
            return mate
        
        
# ------------------- Tarife tahdid haye Asb ------------------- #
def Asb_check(shah, asb):
    if asb[0]+2 == shah[0] and asb[1]+1 == shah[1]:
            mate = True
            return mate
    elif asb[0]+2 == shah[0] and asb[1]-1 == shah[1]:
            mate = True
            return mate
    elif asb[0]-2 == shah[0] and asb[1]+1 == shah[1]:
            mate = True
            return mate
    elif asb[0]-2 == shah[0] and asb[1]-1 == shah[1]:
            mate = True
            return mate
    elif asb[0]+1 == shah[0] and asb[1]+2 == shah[1]:
            mate = True
            return mate
    elif asb[0]-1 == shah[0] and asb[1]+2 == shah[1]:
            mate = True
            return mate
    elif asb[0]+1 == shah[0] and asb[1]-2 == shah[1]:
            mate = True
            return mate
    elif asb[0]-1 == shah[0] and asb[1]-2 == shah[1]:
            mate = True
            return mate


# ------------------- Tarife tahdid haye Rokh ------------------- #
def Rokh_check(rokh, shah, chessboard):
    mate = False
    i = rokh[0]
    j = rokh[1]

    i = rokh[0] +1
    while i != 8 :
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        i += 1

    i = rokh[0] - 1
    j = rokh[1]
    while i != -1 :
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        i -= 1

    i = rokh[0]
    j = rokh[1] + 1
    while j != 8:
        if chessboard[i][j] != " ":
            if  i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        j += 1

    i = rokh[0]
    j = rokh[1] - 1
    while j != -1:
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        j -= 1
    return mate

# ------------------- Tarife tahdid haye Fil ------------------- #
def Fil_check(shah, fil, chessboard): 
    mate = False

    i = fil[0]
    j = fil[1]

    i = fil[0]-1
    j = fil[1]+1
    while i>=0 and j<8:
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        i-=1
        j+=1
    i = fil[0]+1
    j = fil[1]+1  
    while i != 8 and j != 8:
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:    
                mate = True
                return mate
            else:
                break
        i += 1
        j += 1
    i = fil[0]+1
    j = fil[1]-1
    while i!=8 and j!=-1:
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:
                mate = True
                return mate
            else:
                break
        i+=1
        j-=1
    i = fil[0]-1
    j = fil[1]-1
    while i != -1 and j != -1:
        if chessboard[i][j] != " ":
            if i == shah[0] and j == shah[1]:       
                mate = True
                return mate
            else:
                break
        i-=1
        j-=1
    return mate


# ----- Tarife tahdid haye Vazir(ke mitune tarkibe tahdide Rokh va Fil bashe.) ----- #
def Vazir_check(shah, vazir, chessboard):
    Danger = Fil_check(shah, vazir, chessboard)
    if Danger == False:
        return Rokh_check(shah, vazir, chessboard)
    return Danger


# ------------------- Barresie Mate / Not Mate ------------------- #
def Check_Mate(chessboard, shah):
    
    # - Baraye Shahe sefid:
    if color == 'w':
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "p":
                    sarbaz = [i,j]
                    if Sarbaz_check(shah, sarbaz) == True:
                        return "mate"                

                if chessboard[i][j] == "r":
                    rokh = [i,j]
                    if Rokh_check(shah, rokh, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "n":
                    asb = [i,j]
                    if Asb_check(shah, asb) == True:
                        return "mate"

                if chessboard[i][j] == "b":
                    fil = [i,j]
                    if Fil_check(shah, fil, chessboard) == True:
                        return "mate"

                if chessboard[i][j] == "q":
                    vazir = [i,j]
                    if Vazir_check(shah, vazir, chessboard) == True:
                        return "mate"
        else:
            return "not mate"

    # - Baraye Shahe sefid:
    if color == 'b':
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "N":
                    asb = [i,j]
                    if Asb_check(shah, asb) == True:
                        return "mate"
                if chessboard[i][j] == "B":
                    fil = [i,j]
                    if Fil_check(shah, fil, chessboard) == True:
                        return "mate"
                if chessboard[i][j] == "R":
                    rokh = [i,j]
                    if Rokh_check(shah, rokh, chessboard) == True:
                        return "mate"
                if chessboard[i][j] == "Q":
                    vazir = [i,j]
                    if Vazir_check(shah, vazir, chessboard) == True:
                        return "mate"
                if chessboard[i][j] == "P":
                    sarbaz = [i,j]
                    if Sarbaz_check(shah, sarbaz) == True:
                        return "mate"
        else:
            return "not mate"

if mate == True:
    for shah in esc:
        if Check_Mate(chessboard, shah) == "not mate":
            mate = False
            break

#------------------------------

if color == 'w':
    print('Yo Mr.White', file=stderr)

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