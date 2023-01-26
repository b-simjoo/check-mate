from sys import stderr
color = input()
chessboard = [list(input()) for i in range(8)]
# location var
rook_loc = []
bishop_loc = []
knight_loc = []
king_loc = []
queen_loc = []
pawn_loc = []
# main var
check = []
# piece location finder
if color == "w":
    for i in range(8):
        for j in range(8):
            match chessboard[i][j]:
                case "r":
                    rook_loc.extend([i, j])
                case "n":
                    knight_loc.extend([i, j])
                case "b":
                    bishop_loc.extend([i, j])
                case "p":
                    pawn_loc.extend([i, j])
                case "K":
                    king_loc.extend([i, j])
                case "q":
                    queen_loc.extend([i, j])
elif color == "b":
    for i in range(8):
        for j in range(8):
            match chessboard[i][j]:
                case "R":
                    rook_loc.extend([i, j])
                case "N":
                    knight_loc.extend([i, j])
                case "B":
                    bishop_loc.extend([i, j])
                case "P":
                    pawn_loc.extend([i, j])
                case "k":
                    king_loc.extend([i, j])
                case "Q":
                    queen_loc.extend([i, j])
# knight scope
for i in range(0, len(knight_loc), 2):
    for j in range(8):
        ni, nj = knight_loc[i], knight_loc[i + 1]
        match j:
            case 0:
                ni = ni - 2
                nj = nj + 1
            case 1:
                ni = ni - 2
                nj = nj - 1
            case 2:
                ni = ni + 2
                nj = nj + 1
            case 3:
                ni = ni + 2
                nj = nj - 1
            case 4:
                ni = ni - 1
                nj = nj + 2
            case 5:
                ni = ni + 1
                nj = nj + 2
            case 6:
                ni = ni - 1
                nj = nj - 2
            case 7:
                ni = ni + 1
                nj = nj - 2
        if -1 < ni < 8 and -1 < nj < 8:
            cord = f"{ni},{nj}"
            check.append(cord)
# bishop scope
def bishop_scope(a, b):
    for j in range(4):
        bi, bj= a, b
        while j == 0:
            bi = bi + 1
            bj = bj + 1
            if bi > 7 or bj > 7:
                break
            cord = f"{bi},{bj}"
            check.append(cord)
            if chessboard[bi][bj] != " ":
                break
        while j == 1:
            bi = bi + 1
            bj = bj - 1
            if bi < 0 or bj < 0:
                break
            if bi > 7 or bj > 7:
                break
            cord = f"{bi},{bj}"
            check.append(cord)
            if chessboard[bi][bj] != " ":
                break
        while j == 2:
            bi = bi - 1
            bj = bj + 1
            if bi < 0 or bj < 0:
                break
            if bi > 7 or bj > 7:
                break
            cord = f"{bi},{bj}"
            check.append(cord)
            if chessboard[bi][bj] != " ":
                break
        while j == 3:
            bi = bi - 1
            bj = bj - 1
            if bi < 0 or bj < 0:
                break
            cord = f"{bi},{bj}"
            check.append(cord)
            if chessboard[bi][bj] != " ":
                break
for i in range(0, len(bishop_loc), 2):
    bishop_scope(bishop_loc[i], bishop_loc[i + 1])
# rook scope
def rook_scope(a, b):
    for j in range(4):
        ri, rj = a, b
        while j == 0:
            ri = ri - 1
            if ri < 0:
                break
            cord = f"{ri},{rj}"
            check.append(cord)
            if chessboard[ri][rj] != " ":
                break
        while j == 1:
            ri = ri + 1
            if ri > 7:
                break
            cord = f"{ri},{rj}"
            check.append(cord)
            if chessboard[ri][rj] != " ":
                break
        while j == 2:
            rj = rj - 1
            if rj < 0:
                break
            cord = f"{ri},{rj}"
            check.append(cord)
            if chessboard[ri][rj] != " ":
                break
        while j == 3:
            rj = rj + 1
            if rj > 7:
                break
            cord = f"{ri},{rj}"
            check.append(cord)
            if chessboard[ri][rj] != " ":
                break
for i in range(0, len(rook_loc), 2):
    rook_scope(rook_loc[i], rook_loc[i + 1])
# queen scope
for i in range(0, len(queen_loc), 2):
    bishop_scope(queen_loc[i], queen_loc[i + 1])
    rook_scope(queen_loc[i], queen_loc[i + 1])
# pawn scope
for i in range(0, len(pawn_loc), 2):
    for j in range(2):
        pi, pj = pawn_loc[i], pawn_loc[i + 1]
        if color == "w":
            if j == 0:
                pi = pi + 1
                pj = pj + 1
            elif j == 1:
                pi = pi + 1
                pj = pj - 1
            if -1 < pi < 8 and -1 < pj < 8:
                cord = f"{pi},{pj}"
                check.append(cord)
        elif color == "b":
            if j == 0:
                pi = pi - 1
                pj = pj + 1
            elif j == 1:
                pi = pi - 1
                pj = pj - 1
            if -1 < pi < 8 and -1 < pj < 8:
                cord = f"{pi},{pj}"
                check.append(cord)
# king free zones checker
king_sqr = []
ki, kj = king_loc[0], king_loc[1]
king_sqr.append(f"{ki},{kj}")
for j in range(8):
    ki, kj = king_loc[0], king_loc[1]
    match j:
        case 0:
            ki = ki - 1
            kj = kj - 1
        case 1:
            ki = ki - 1
        case 2:
            ki = ki - 1
            kj = kj + 1
        case 3:
            kj = kj - 1
        case 4:
            kj = kj + 1
        case 5:
            ki = ki + 1
            kj = kj - 1
        case 6:
            ki = ki + 1
        case 7:
            ki = ki + 1
            kj = kj + 1
    if -1 < ki < 8 and -1 < kj < 8 and chessboard[ki][kj] == " ":
        cord = f"{ki},{kj}"
        king_sqr.append(cord)
# mate or not mate checker
mate_arr = []
no_dupe_mate_arr = []
for i in check:
    if i == king_sqr[0]:
        for j in check:
            if j in king_sqr:
                mate_arr.append(j)
for i in mate_arr:
    if i not in no_dupe_mate_arr:
        no_dupe_mate_arr.append(i)
no_dupe_mate_arr.sort()
king_sqr.sort()
if no_dupe_mate_arr == king_sqr and len(no_dupe_mate_arr) == len(king_sqr):
    print("mate")
else:
    print("not mate")
