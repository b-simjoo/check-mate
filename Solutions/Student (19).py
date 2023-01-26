from sys import stderr


#------------------------------
color = input()                                       
chessboard = [list(input()) for i in range(8)]        
#------------------------------

#------------------------------
white_piece=["K","Q","N","B","R","P"]
black_piece=["k","q","n","b","r","p"]
kinglog_w=[]
kinglog_b=[]
white_king=False
black_king=False
horse=[]

def isonboard(row,col):
        if 0 <=row< 8 and 0 <=col< 8:
            return True
        return False 
    
def pieces(piec,row,col):
    for i in range(len(piec)):
        if chessboard[row][col]==piec[i]:
            return piec[i]
        
for row in range(8):
    for col in range(8):
        chessboard[row][col]
        if chessboard[row][col]=="K":
            a=("K"+str(row)+str(col))
            kinglog_w.append(a)
        if chessboard[row][col]=="k":
            b=("k"+str(row)+str(col))
            kinglog_b.append(b)

def king_logcheckboard(row,col):
    if 1<=row<7:
        if row==6:
            row=6
            r=6
        else:
            r=row-1
    if row==0:
        r=0
    if row==7:
        row=row-1
        r=row
    if 1<=col<7:
        if col==6:
            col=6
            c=6
        else:
            c=col-1
    if col==0:
        c=0
    if col==7:
        col=col-1
        c=col
    return r,c,row,col

def king_mate(row_king,col_king,king,piece):
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)   
    for row in range(r,row_king+2):
        for col in range(c,col_king+2):
            if chessboard[row][col]==" " or chessboard[row][col]==pieces(piece,row,col):
                king=False
            elif chessboard[row][col]=="redsquare":
                king=True
            for h in range(len(horse)):
                a=horse[h]
                if chessboard[row][col]==pieces(piece,row,col) and a[0]=="n"or a[0]=="N":    
                    king=True  
                else:
                    king=False
    return king

def king_house(row,col,king,row_king,col_king,piece,oppiece):
    r,c,row_king,col_king=king_logcheckboard(row_king,col_king)
    if r<=row<row_king+2 and c<=col<col_king+2 and chessboard[row][col]!=pieces(piece,row,col) and chessboard[row][col]!=pieces(oppiece,row,col):
        chessboard[row][col]="redsquare"   
    if chessboard[row][col]=="k" or chessboard[row][col]=="K":
        king=king_mate(row_king,col_king,king,piece)
        
def move_verhozrd(row,col,direction,piece,oppiece,king,row_king,col_king):
    if direction=="r":  
        h=col+1
        i=row
    if direction=="d":
        i=row+1
        h=col
        while 0<=h<8 and 0<=i<8:
            if chessboard[i][h]=="k" or chessboard[i][h]=="K":
                king=king_mate(row_king,col_king,king,piece)
            elif chessboard[i][h]==pieces(piece,i,h) or chessboard[i][h]==pieces(oppiece,i,h):
                break
            king_house(i,h,king,row_king,col_king,piece,oppiece)
            if direction=="d":
                i+=1 
            else:
                h+=1
            
def move_verhozlu(row,col,direction,piece,oppiece,king,row_king,col_king):
    if direction=="u":  
        h=col
        i=row-1
    if direction=="l":
        i=row
        h=col-1
    while 0<=h<8 and 0<=i<8:
        if chessboard[i][h]=="k" or chessboard[i][h]=="K":
            king=king_mate(row_king,col_king,king,piece)
        elif chessboard[i][h]==pieces(piece,i,h) or chessboard[i][h]==pieces(oppiece,i,h):
            break
        king_house(i,h,king,row_king,col_king,piece,oppiece)
        if direction=="u":
            i-=1 
        else:
            h-=1
            
def ver_hoz(row,col,piece,oppiece,king,row_king,col_king):
    move_verhozrd(row,col,"r",piece,oppiece,king,row_king,col_king)
    move_verhozrd(row,col,"d",piece,oppiece,king,row_king,col_king)
    move_verhozlu(row,col,"u",piece,oppiece,king,row_king,col_king)
    move_verhozlu(row,col,"l",piece,oppiece,king,row_king,col_king)    
    
def call_piece(ppoint,i,j,king,piece,oppiece,row_king,col_king):
        if ppoint[0]=="q" or  ppoint[0]=="Q":
            queen(i,j,king,piece,oppiece,row_king,col_king)
        elif ppoint[0]=="r" or  ppoint[0]=="R":
            rock(i,j,king,piece,oppiece,row_king,col_king)
        elif ppoint[0]=="b" or  ppoint[0]=="B":
            bishop(i,j,king,piece,oppiece,row_king,col_king)         
        elif ppoint[0]=="n" or  ppoint[0]=="N":
            knight(i,j,king,row_king,col_king,piece,oppiece)
        elif ppoint[0]=="p" or  ppoint[0]=="P":
            pawn(row_king,col_king,king,piece) 
            
def find_picecking(piece,oppiece,king,row_king,col_king):
    for i in range(8):
        for j in range(8):
            if chessboard[i][j]==pieces(piece,i,j) or chessboard[i][j]=="k" or chessboard[i][j]=="K":
                continue 
            if chessboard[i][j]==pieces(oppiece,i,j):
                call_piece(chessboard[i][j],i,j,king,piece,oppiece,row_king,col_king)     
                       
def move_dignoaludr(row,col,direction,piece,oppiece,king,row_king,col_king):
    if direction=="ur":  
        h=col+1
        i=row-1
    if direction=="dr":
        i=row+1
        h=col+1
        while 0<=h<8 and 0<=i<8:
            if chessboard[i][h]=="k" or chessboard[i][h]=="K":
                king=king_mate(row_king,col_king,king,piece)
            elif chessboard[i][h]==pieces(piece,i,h) or chessboard[i][h]==pieces(oppiece,i,h):
                break
            king_house(i,h,king,row_king,col_king,piece,oppiece)
            if direction=="dr":
                i+=1
                h+=1 
            else:
                h+=1
                i-=1
            
def move_dignoaldul(row,col,direction,piece,oppiece,king,row_king,col_king):
    if direction=="ul":  
        h=col-1
        i=row-1
    if direction=="dl":
        i=row+1
        h=col-1
    while 0<=h<8 and 0<=i<8:
        if chessboard[i][h]=="k" or chessboard[i][h]=="K":
            king=king_mate(row_king,col_king,king,piece)
        elif chessboard[i][h]==pieces(piece,i,h) or chessboard[i][h]==pieces(oppiece,i,h):
            break
        king_house(i,h,king,row_king,col_king,piece,oppiece)
        if direction=="ul":
            i-=1 
            h-=1
        else:
            h-=1
            i+=1
            
def dignoal_move(row,col,piece,oppiece,king,row_king,col_king):
    move_dignoaludr(row,col,"ur",piece,oppiece,king,row_king,col_king)
    move_dignoaludr(row,col,"dr",piece,oppiece,king,row_king,col_king)
    move_dignoaldul(row,col,"ul",piece,oppiece,king,row_king,col_king)
    move_dignoaldul(row,col,"dl",piece,oppiece,king,row_king,col_king) 

def kinglog(wK,piece,oppiece,king):
    row_king=int(wK[1])     
    col_king=int(wK[2])  
    find_picecking(piece,oppiece,king,row_king,col_king)
    king=king_mate(row_king,col_king,king,piece)
    return king

def queen(i,j,king,piece,oppiece,row_king,col_king):
    ver_hoz(i,j,piece,oppiece,king,row_king,col_king)
    dignoal_move(i,j,piece,oppiece,king,row_king,col_king)
        
def rock(i,j,king,piece,oppiece,row_king,col_king):
    ver_hoz(i,j,piece,oppiece,king,row_king,col_king)
    
def bishop(i,j,king,piece,oppiece,row_king,col_king):
    dignoal_move(i,j,piece,oppiece,king,row_king,col_king)
    
def pawn(row_king,col_king,king,piece):
    #king white
    if isonboard(row_king-1,col_king-1) and chessboard[row_king-1][col_king-1]=="p" or isonboard(row_king-1,col_king+1) and chessboard[row_king-1][col_king+1]=="p":
        king=king_mate(row_king,col_king,king,piece)
    #king black
    if isonboard(row_king+1,col_king-1) and chessboard[row_king+1][col_king-1]=="P" or isonboard(row_king+1,col_king+1) and chessboard[row_king+1][col_king+1]=="P":
        king=king_mate(row_king,col_king,king,piece)
        
def knight(i,j,king,row_king,col_king,piece,oppiece):
    for row in range(i-2,i+3):
        if row==i:
            continue
        if i%2==True:
            if row%2==False:
                h=j-2
                e=h+5
                f=4
            else:
                h=j-1
                e=h+3
                f=2  
        else:
            if row%2==False:
                h=j-1
                e=h+3
                f=2
            else:
                h=j-2
                e=h+5
                f=4  
        for col in range(h,e,f):
            if isonboard(row,col):
                if row==row_king and col==col_king:
                    if chessboard[i][j]=="n":     
                        horse.append("n"+str(i)+str(j))
                    if chessboard[i][j]=="N":
                        horse.append("N"+str(i)+str(j))
                    king=king_mate(row_king,col_king,king,piece)            
                elif chessboard[row][col]==pieces(piece,row,col) or chessboard[row][col]==pieces(oppiece,row,col):
                    continue
                else:
                    king_house(row,col,king,row_king,col_king,piece,oppiece)
            else:
                break
        
white_king=kinglog(wK= kinglog_w[0],piece=white_piece,oppiece=black_piece,king= white_king)   
black_king=kinglog(wK= kinglog_b[0],piece=black_piece,oppiece=white_piece,king=black_king)
if white_king==False and black_king==False:
    print("not mate")
elif white_king==True:
    print("mate")
elif black_king==True:
    print("mate")
    
#------------------------------

#------------------------------