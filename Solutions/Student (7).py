from sys import stderr
import time
#______________________
Colour  =  input()                                       
Chess_Board  =  [list(input()) for i in range(8)]        
#______________________

W_Piece = ["K","Q","N","B","R","P"]
B_Piece = ["k","q","n","b","r","p"]
W_King_Log = []
B_King_Log = []
W_King = False
B_King = False
Horse = []

def Chess_Dimension(Height, Width): #Dimension of the map
        if 0 <= Height < 8 and 0 <=Width< 8:
            return True
        return False 
def Pieces(Piece,Height,Width):
    for i in range(len(Piece)):
        if Chess_Board [Height] [Width] == Piece [i]:
            return Piece[i]
for Height in range(8):
    for Width in range(8):
        Chess_Board [Height] [Width]
        if Chess_Board [Height] [Width] == "K":
            a = ("K"+str(Height)+str(Width))
            W_King_Log.append(a)
        if Chess_Board[Height][Width]=="k":
            b = ("k"+str(Height)+str(Width))
            B_King_Log.append(b)

def king_logcheckboard(Height,Width):
    if 1 <= Height < 7:
        if Height == 6:
            Height = 6
            r = 6
        else:
            r = Height-1
    if Height == 0:
        r = 0
    if Height == 7:
        Height = Height-1
        r = Height
    if 1 <= Width < 7:
        if Width == 6:
            Width = 6
            c = 6
        else:
            c = Width-1
    if Width == 0:
        c = 0
    if Width == 7:
        Width = Width-1
        c = Width
    return r,c,Height,Width
def Checkmate (Height_King, Width_King, King, piece):
    r,c,Height_King,Width_King = king_logcheckboard(Height_King,Width_King)   
    for Height in range(r,Height_King+2):
        for Width in range(c,Width_King+2):
            if Chess_Board [Height] [Width] == ' ' or Chess_Board[Height][Width]==Pieces(piece,Height,Width):
                King = False
            elif Chess_Board[Height][Width]=="redsquare":
                King = True
            for h in range(len(Horse)):
                a = Horse[h]
                if Chess_Board [Height] [Width] == Pieces(piece,Height,Width) and a [0] == "n" or a [0] == "N":    
                    King=True  
    return King
def king_house(row,col,king,row_king,col_king,piece,oppiece):
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)
    if r<=row<row_king+2 and c<=col<col_king+2 and Chess_Board[row][col]!=Pieces(piece,row,col) and Chess_Board[row][col]!=Pieces(oppiece,row,col):
        Chess_Board[row][col]="redsquare"   
    if Chess_Board[row][col]=="k" or Chess_Board[row][col]=="K":
        king=Checkmate(row_king,col_king,king,piece)

def ver_hoz(row,col,piece,oppiece,king,row_king,col_king):
    for i in range(0,8):
        if Chess_Board[i][col]==Pieces(piece,i,col) and Chess_Board[row][i]==Pieces(piece,row,i):
            continue
        if Chess_Board[i][col]==Pieces(oppiece,i,col) and Chess_Board[row][i]==Pieces(oppiece,row,i):
            continue
        king_house(row,i,king,row_king,col_king,piece,oppiece)
        king_house(i,col,king,row_king,col_king,piece,oppiece)
        
def call_piece(ppoint,i,j,king,piece,oppiece,row_king,col_king,wK):
        if ppoint[0]=="q" or  ppoint[0]=="Q":
            queen(i,j,king,piece,oppiece,row_king,col_king)
        elif ppoint[0]=="r" or  ppoint[0]=="R":
            rock(i,j,king,piece,oppiece,row_king,col_king)
        elif ppoint[0]=="b" or  ppoint[0]=="B":
            bishop(i,j,king,piece,oppiece,row_king,col_king)         
        elif ppoint[0]=="n" or  ppoint[0]=="N":
            knight(king,row_king,col_king,piece,wK)
        elif ppoint[0]=="p" or  ppoint[0]=="P":
            pawn(row_king,col_king,king,piece) 
def find_picecking(row,row1,col,col1,piece,oppiece,king,row_king,col_king,wK):
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)
    for i in range(row,row1+2):
        for j in range(col,col1+2):
            if row==0 and row1==6:
                if r<i<row_king+2:
                    continue
            if Chess_Board[i][j]==Pieces(piece,i,j) or Chess_Board[i][j]=="k" or Chess_Board[i][j]=="K":
                continue
            if Chess_Board[i][j]==Pieces(oppiece,i,j):
                call_piece(Chess_Board[i][j],i,j,king,piece,oppiece,row_king,col_king,wK)
                
def dignoal_point(row,col):
    if row<=col:
        i=0
        j=col-row
        i1=0
        j1=col+row
    if row>col:
        i=row-col
        j=0
        i1=0
        j1=row+col
    if j1>=8:
        while j1>7:
            j1-=1
            i1+=1
    return(i,j,i1,j1)
def dignoal_piece(piece,oppiece,king,row_king,col_king,wK):
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)
    for row_r in range(0,8):
        for col_r in range(0,8):
            if r<=row_r<row_king+2 or 0<=col_r<8:
                continue
            if 0<=row_r<8 or c<=col_r<col_king+2 or Chess_Board[row_r][col_r]=="k" or Chess_Board[row_r][col_r]=="K":
                continue
            elif Chess_Board[row_r][col_r]==Pieces(piece,row_r,col_r):
                continue
            if Chess_Board[row_r][col_r]==Pieces(oppiece,row_r,col_r):
                call_piece(Chess_Board[row_r][col_r],row_r,col_r,king,piece,oppiece,row_king,col_king,wK) 
                
def dignoal_move(row,col,piece,oppiece,king,row_king,col_king):
    i,j,i1,j1=dignoal_point(row,col) 
    while Chess_Dimension(i,j)==True:
        if j==col and i==row:
            i+=1    
            j+=1
            continue
        elif Chess_Board[i][j]=="k" or Chess_Board[i][j]=="K":
            king=Checkmate(row_king,col_king,king,piece)
            i+=1    
            j+=1
            continue
        elif Chess_Board[i][j]==Pieces(piece,i,j) or Chess_Board[i][j]==Pieces(oppiece,i,j): 
            i+=1    
            j+=1
            break
        king_house(i,j,king,row_king,col_king,piece,oppiece)
        i+=1    
        j+=1
    while Chess_Dimension(i1,j1)==True:
        if j1==col and i1==row:
            i1+=1    
            j1-=1
            continue
        elif Chess_Board[i1][j1]=="k" or Chess_Board[i1][j1]=="K":
            king=Checkmate(row_king,col_king,king,piece)
            i1+=1    
            j1-=1
            continue
        elif Chess_Board[i1][j1]==Pieces(piece,i1,j1) or Chess_Board[i1][j1]==Pieces(oppiece,i1,j1): 
            i1+=1    
            j1-=1
            break
        king_house(i1,j1,king,row_king,col_king,piece,oppiece)
        i1+=1
        j1-=1
        
def kinglog(wK,piece,oppiece,king):
    row_king=int(wK[1])     
    col_king=int(wK[2])
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)    
    find_picecking(r,row_king,0,6,piece,oppiece,king,row_king,col_king,wK)
    find_picecking(0,6,c,col_king,piece,oppiece,king,row_king,col_king,wK)
    dignoal_piece(W_Piece,B_Piece,king,row_king,col_king,wK)
    king=Checkmate(row_king,col_king,king,piece)
    return king

def get_knight(i,j,king,row_king,col_king,piece):
    if Chess_Dimension(i,j):
        if Chess_Board[i][j]=="n":     
            Horse.append("n"+str(i)+str(j))
        if Chess_Board[i][j]=="N":
            Horse.append("N"+str(i)+str(j))
        king=Checkmate(row_king,col_king,king,piece)
    return king
def queen(i,j,king,piece,oppiece,row_king,col_king):
    ver_hoz(i,j,piece,oppiece,king,row_king,col_king)
    dignoal_move(i,j,piece,oppiece,king,row_king,col_king)
        
def rock(i,j,king,piece,oppiece,row_king,col_king):
    ver_hoz(i,j,piece,oppiece,king,row_king,col_king)
    
def bishop(i,j,king,piece,oppiece,row_king,col_king):
    dignoal_move(i,j,piece,oppiece,king,row_king,col_king)
    
def pawn(row_king,col_king,king,piece):
    if Chess_Board[row_king-1][col_king-1]=="p" or Chess_Board[row_king-1][col_king+1]=="p":
        king=Checkmate(row_king,col_king,king,piece)
    if Chess_Board[row_king-1][col_king-1]=="P" or Chess_Board[row_king-1][col_king+1]=="P":
        king=Checkmate(row_king,col_king,king,piece)
        
def knight(king,row_king,col_king,piece,wK):
    row_king=int(wK[1])     
    col_king=int(wK[2])
    for i in range(row_king-2,row_king+3):
        if row_king-i%2:
            h=col_king-1
            e=h+3
        else:
            h=col_king-2
            e=h+5  
        for j in range(h,e,2):
            if i==row_king or j==col_king:
                continue
            if Chess_Dimension(i,j):
                get_knight(i,j,king,row_king,col_king,piece)           
            else:
                break 
        
W_King=kinglog(wK= W_King_Log[0],piece=W_Piece,oppiece=B_Piece,king= W_King)   
B_King=kinglog(wK= B_King_Log[0],piece=B_Piece,oppiece=W_Piece,king=B_King)
if W_King==False and B_King==False:
    print("not mate")
    time.sleep(1)
if W_King==True:
    print("mate")
    time.sleep(1)
if B_King==True:
    print("mate")
    time.sleep(1)

