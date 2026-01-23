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

    app.lastRow = 0
    app.lastCol = 0

    app.done = False

def redrawAll(app):
    drawImage(app.boardUrl, 25, 25)

    # draw side instructions and reset button
    if app.turn==1:
        drawImage(app.whiteUrl, 700, 175, width = 100, height = 100)
    else:
        drawImage(app.blackUrl, 700, 175, width = 100, height = 100)

    drawRect(700, 500, 100, 50, fill = "red")
    drawLabel("reset", 750, 525, size = 20)

    # draw pieces
    for i in range(0, 19):
        for j in range(0, 19):
            if app.board[i][j] == 1:
                drawImage(app.whiteUrl, 27+32*i, 27+32*j)
            if app.board[i][j] == 2:
                drawImage(app.blackUrl, 27+32*i, 27+32*j)
    
    # draw win screen or not
    if app.done:
        drawLabel("yippee", 750, 300)
    else:
        drawLabel("not yet", 750, 300)

def onMouseMove(app, mouseX, mouseY):
    pass
    # possibly make a green arrow to show what area you're hovered over?

def onMouseRelease(app, mouseX, mouseY):
    boxNumX = (mouseX-27)//32
    boxNumY = (mouseY-27)//32

    if 0 <= boxNumX < 19 and 0 <= boxNumY < 19 and app.board[boxNumX][boxNumY] == 0 and not app.done:
        app.board[boxNumX][boxNumY] = app.turn
        app.lastRow = boxNumX
        app.lastCol = boxNumY
        swapTurn(app)
        checkWon(app, app.lastRow, app.lastCol)
    if 700<mouseX<800 and 500<mouseY<550:
        reset(app)

def swapTurn(app):
    if app.turn == 1:
        app.turn =2
    elif app.turn ==2:
        app.turn=1

def checkWon(app, lastRow, lastCol):
    directions = [[0,1], [1,0], [1,-1], [1, 1]]
    for dir in directions:
        if app.turn ==1:
            lastTurn = 2
        elif app.turn ==2:
            lastTurn =1
        i = 1
        count = 1
        while 0<=lastRow + dir[0]*i <=18 and 0<=lastCol+dir[1]*i<=18:
            if app.board[lastRow+dir[0]*i][lastCol+dir[1]*i] != lastTurn:
                break
            count+=1
            i+=1
        i=1
        while 0<=lastRow - dir[0]*i <=18 and 0<=lastCol-dir[1]*i<=18:
            if app.board[lastRow-dir[0]*i][lastCol-dir[1]*i] != lastTurn:
                break
            count+=1
            i+=1
        if count >=5:
            app.done = True
            return True
    return False
        

def reset(app):
    app.board = [[0]*19 for i in range(0, 19)]
    app.turn=1
    app.done = False

def main():
    runApp()

main()

