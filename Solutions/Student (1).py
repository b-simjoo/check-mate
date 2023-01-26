from sys import stderr

# Find the location of the chess piece
def location(chessboard, icon):
    for i in range(8):
        while True:
            try:
                index = chessboard[i].index(icon)
                return [i, index]

            except:
                break


# Kish places by chess
def Rook(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    for i in range(8):
        line = x + (i + 1)
        if line < 8:
            if (
                chessboard[line][y] == " "
                or chessboard[line][y] == "kish"
                or chessboard[line][y] == color_king
            ):
                chessboard[line][y] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        line = x - (i + 1)
        if line >= 0:
            if (
                chessboard[line][y] == " "
                or chessboard[line][y] == "kish"
                or chessboard[line][y] == color_king
            ):
                chessboard[line][y] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        column = y + (i + 1)
        if column < 8:
            if (
                chessboard[x][column] == " "
                or chessboard[x][column] == "kish"
                or chessboard[x][column] == color_king
            ):
                chessboard[x][column] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        column = y - (i + 1)
        if column >= 0:
            if (
                chessboard[x][column] == " "
                or chessboard[x][column] == "kish"
                or chessboard[x][column] == color_king
            ):
                chessboard[x][column] = "kish"
            else:
                break
        else:
            break
    return chessboard


def Bishop(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    for i in range(8):
        line = x + (i + 1)
        column = y + (i + 1)
        if line < 8 and column < 8:
            if (
                chessboard[line][column] == " "
                or chessboard[line][column] == "kish"
                or chessboard[line][column] == color_king
            ):
                chessboard[line][column] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        line = x - (i + 1)
        column = y - (i + 1)
        if line >= 0 and column >= 0:
            if (
                chessboard[line][column] == " "
                or chessboard[line][column] == "kish"
                or chessboard[line][column] == color_king
            ):
                chessboard[line][column] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        line = x + (i + 1)
        column = y - (i + 1)
        if line < 8 and column >= 0:
            if (
                chessboard[line][column] == " "
                or chessboard[line][column] == "kish"
                or chessboard[line][column] == color_king
            ):
                chessboard[line][column] = "kish"
            else:
                break
        else:
            break

    for i in range(8):
        line = x - (i + 1)
        column = y + (i + 1)
        if column < 8 and line >= 0:
            if (
                chessboard[line][column] == " "
                or chessboard[line][column] == "kish"
                or chessboard[line][column] == color_king
            ):
                chessboard[line][column] = "kish"
            else:
                break
        else:
            break
    return chessboard


def Queen(chessboard, x, y, color):
    chessboard = Rook(chessboard, x, y, color)
    chessboard = Bishop(chessboard, x, y, color)
    return chessboard


def king(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    line = x + 1
    if line < 8:
        if (
            chessboard[line][y] == " "
            or chessboard[line][y] == "kish"
            or chessboard[line][y] == color_king
        ):
            chessboard[line][y] = "kish"

    line = x - 1
    if line >= 0:
        if (
            chessboard[line][y] == " "
            or chessboard[line][y] == "kish"
            or chessboard[line][y] == color_king
        ):
            chessboard[line][y] = "kish"

    column = y + 1
    if column < 8:
        if (
            chessboard[x][column] == " "
            or chessboard[x][column] == "kish"
            or chessboard[x][column] == color_king
        ):
            chessboard[x][column] = "kish"

    column = y - 1
    if column >= 0:
        if (
            chessboard[x][column] == " "
            or chessboard[x][column] == "kish"
            or chessboard[x][column] == color_king
        ):
            chessboard[x][column] = "kish"

    line = x + 1
    column = y + 1
    if line < 8 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x - 1
    column = y - 1
    if line >= 0 and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x + 1
    column = y - 1
    if line < 8 and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x - 1
    column = y + 1
    if line >= 0 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    return chessboard


def Knight(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    line = x + 2
    column = y + 1
    if line < 8 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x + 2
    column = y - 1
    if line < 8 and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x - 2
    column = y + 1
    if line >= 0 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x - 2
    column = y - 1
    if line and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    column = y + 2
    line = x + 1
    if column < 8 and line < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    column = y + 2
    line = x - 1
    if column < 8 and line >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    column = y - 2
    line = x + 1
    if column >= 0 and line < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    column = y - 2
    line = x - 1
    if column >= 0 and line >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    return chessboard


def Pawn(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    line = x - 1
    column = y + 1
    if line >= 0 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x - 1
    column = y - 1
    if line >= 0 and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    return chessboard


def pawn(chessboard, x, y, color):
    if color == "w":
        color_king = "K"
    else:
        color_king = "k"

    line = x + 1
    column = y + 1
    if line < 8 and column < 8:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    line = x + 1
    column = y - 1
    if line < 8 and column >= 0:
        if (
            chessboard[line][column] == " "
            or chessboard[line][column] == "kish"
            or chessboard[line][column] == color_king
        ):
            chessboard[line][column] = "kish"

    return chessboard


# Checker of kish places by chess pieces
def checker(chessboard, color):
    if color == "w":
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "r":
                    chessboard = Rook(chessboard, i, j, color)

                elif chessboard[i][j] == "b":
                    chessboard = Bishop(chessboard, i, j, color)

                elif chessboard[i][j] == "q":
                    chessboard = Queen(chessboard, i, j, color)

                elif chessboard[i][j] == "n":
                    chessboard = Knight(chessboard, i, j, color)

                elif chessboard[i][j] == "k":
                    chessboard = king(chessboard, i, j, color)

                elif chessboard[i][j] == "p":
                    chessboard = pawn(chessboard, i, j, color)

    else:
        for i in range(8):
            for j in range(8):
                if chessboard[i][j] == "R":
                    chessboard = Rook(chessboard, i, j, color)

                elif chessboard[i][j] == "B":
                    chessboard = Bishop(chessboard, i, j, color)

                elif chessboard[i][j] == "Q":
                    chessboard = Queen(chessboard, i, j, color)

                elif chessboard[i][j] == "N":
                    chessboard = Knight(chessboard, i, j, color)

                elif chessboard[i][j] == "K":
                    chessboard = king(chessboard, i, j, color)

                elif chessboard[i][j] == "P":
                    chessboard = Pawn(chessboard, i, j, color)

    return chessboard


# king status checker
def mate(chessboard, x, y):
    mate = "mate"

    line = x + 1
    if line < 8:
        if chessboard[line][y] == " ":
            mate = "not mate"
            return mate

    line = x - 1
    if line >= 0:
        if chessboard[line][y] == " ":
            mate = "not mate"
            return mate

    column = y + 1
    if column < 8:
        if chessboard[x][column] == " ":
            mate = "not mate"
            return mate

    column = y - 1
    if column >= 0:
        if chessboard[x][column] == " ":
            mate = "not mate"
            return mate

    line = x + 1
    column = y + 1
    if line < 8 and column < 8:
        if chessboard[line][column] == " ":
            mate = "not mate"
            return mate

    line = x - 1
    column = y - 1
    if line >= 0 and column >= 0:
        if chessboard[line][column] == " ":
            mate = "not mate"
            return mate

    line = x + 1
    column = y - 1
    if line < 8 and column >= 0:
        if chessboard[line][column] == " ":
            mate = "not mate"
            return mate

    line = x - 1
    column = y + 1
    if line >= 0 and column < 8:
        if chessboard[line][column] == " ":
            mate = "not mate"
            return mate

    return mate


# color and chessboard input
color = input()
chessboard = [list(input()) for _ in range(8)]

if color == "w":
    print("Yo Mr.White", file=stderr)

# find the location of the king
if color == "w":
    place = location(chessboard, "K")
else:
    place = location(chessboard, "k")

chessboard = checker(chessboard, color)

# check the status of the king
if chessboard[place[0]][place[1]] == "kish":
    answer = mate(chessboard, place[0], place[1])
    print(answer)
else:
    print("not mate")
