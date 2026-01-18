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
            if app.board[i][j] == 2:
                drawImage(app.blackUrl, 27+32*i, 27+32*j)
    
    # draw win screen or not
    if checkWon():
        pass
    else:
        pass

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

def checkWon():
    return False

def reset():
    app.board = [[0]*19 for i in range(0, 19)]

def main():
    runApp()

main()

