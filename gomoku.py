import copy
from cmu_graphics import *

def onAppStart(app):
    app.width = 904
    app.height = 654
    
    # turn variable, 1 = white, 2 = black, 0 = none
    app.turn = 1

    # initialize all images
    app.boardUrl = "images/gomoku.png"
    app.whiteUrl = "images/white-piece.png"
    app.blackUrl = "images/black-piece.png"

    # intialize board, 0=empty, 1=white, 2=black
    app.board = [[0]*19 for i in range(0, 19)]
    app.board[0][0] = 1
    app.board[6][6] = 2

def redrawAll(app):
    drawImage(app.boardUrl, 25, 25)

    # draw pieces
    for i in range(0, 19):
        for j in range(0, 19):
            if app.board[i][j] == 1:
                drawImage(app.whiteUrl, 27+32*i, 27+32*j)
                lastRow = i
                lastCol = j
            if app.board[i][j] == 2:
                drawImage(app.blackUrl, 27+32*i, 27+32*j)
                lastRow = i
                lastCol = j
    
    # draw win screen or not
    if checkWon(app, lastRow, lastCol):
        drawLabel("yippee", 750, 300)
    else:
        drawLabel("not yet", 750, 300)

def onMouseMove(app, mouseX, mouseY):
    pass
    # possibly make a green arrow to show what area you're hovered over?

def onMouseRelease(app, mouseX, mouseY):
    boxNumX = (mouseX-27)//32
    boxNumY = (mouseY-27)//32

    if 0 <= boxNumX < 19 and 0 <= boxNumY < 19 and app.board[boxNumX][boxNumY] == 0:
        app.board[boxNumX][boxNumY] = app.turn
        swapTurn(app)
    pass

def swapTurn(app):
    if app.turn == 1:
        app.turn =2
    elif app.turn ==2:
        app.turn=1

def checkWon(app, lastRow, lastCol):
    directions = [[0,1], [1,0], [1,-1], [1, 1]]
    found = True
    
    for dir in directions:
        for i in range(4, -1, -1):
            startRow = lastRow - (abs(dir[0])*i)
            startCol = lastCol - (abs(dir[1])*i) 
            if 0<=startRow<= 15 and 0<=startCol<=15:
                found = True
                for j in range(0, 5):
                    if app.turn==1:
                        if app.board[startRow+j][startCol+j] != 1:
                            found = False
                    elif app.turn==2:
                        if app.board[startRow+j][startCol+j] !=2:
                            found = False
                if found:
                    return True
                
    return False
                            


def reset():
    app.board = [[0]*19 for i in range(0, 19)]

def main():
    runApp()

main()

