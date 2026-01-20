import pygame

pygame.init()
screen = pygame.display.set_mode((904, 654))
clock = pygame.time.Clock()
running = True

def checkWon(board, turn, lastRow, lastCol):
    directions = [[0,1], [1,0], [1,-1], [1, 1]]
    for dir in directions:
        if turn ==1:
            lastTurn = 2
        elif turn ==2:
            lastTurn =1
        i = 1
        count = 1
        while 0<=lastRow + dir[0]*i <=18 and 0<=lastCol+dir[1]*i<=18:
            if board[lastRow+dir[0]*i][lastCol+dir[1]*i] != lastTurn:
                break
            count+=1
            i+=1
        i=1
        while 0<=lastRow - dir[0]*i <=18 and 0<=lastCol-dir[1]*i<=18:
            if board[lastRow-dir[0]*i][lastCol-dir[1]*i] != lastTurn:
                break
            count+=1
            i+=1
        if count >=5:
            return True
    return False

turn = 1

boardUrl = pygame.image.load("images/gomoku.png")
whiteUrl = pygame.image.load("images/white-piece.png")
blackUrl = pygame.image.load("images/black-piece.png")

bWhiteUrl = pygame.image.load("images/bWhite.png")
bBlackUrl = pygame.image.load("images/bBlack.png")

turnUrl = pygame.image.load("images/turn.png")
titleUrl = pygame.image.load("images/title.png")
resetUrl = pygame.image.load("images/reset.png")
winUrl = pygame.image.load("images/win.png")

board = [[0]*19 for i in range(0, 19)]

lastRow = 0
lastCol = 0

done = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            boxNumX = (mousePos[0]-27)//32
            boxNumY = (mousePos[1]-27)//32

            if 700<mousePos[0]<850 and 530<mousePos[1]<600:
                # resets game
                board = [[0]*19 for i in range(0, 19)]
                turn = 1
                done = False
                print("game was reset")
            if 0 <= boxNumX < 19 and 0 <= boxNumY < 19 and board[boxNumX][boxNumY] == 0 and not done:
                board[boxNumX][boxNumY] = turn
                lastRow = boxNumX
                lastCol = boxNumY
                if turn==1:
                    turn=2
                else:
                    turn=1


    screen.fill("white")
    screen.blit(boardUrl, (25, 25))

    # show whose turn
    if checkWon(board, turn, lastRow, lastCol):
        done = True
        screen.blit(winUrl, (0,0))
        if turn==1:
            screen.blit(bBlackUrl, 680, 150)
        else:
            screen.blit(bWhiteUrl, (680, 150))
    else:
        screen.blit(turnUrl, (0, 0))
        if turn==1:
            screen.blit(bWhiteUrl, (680, 150))
        else:
            screen.blit(bBlackUrl, (680, 150))

        # ghost pieces?
        mousePos = pygame.mouse.get_pos()
        boxNumX = (mousePos[0]-27)//32
        boxNumY = (mousePos[1]-27)//32
        if 0 <= boxNumX < 19 and 0 <= boxNumY < 19 and board[boxNumX][boxNumY] == 0 and not done:
            if turn==1:
                # draw white ghost piece
            if turn==2:
                # draw black ghost piece

    # draw in title and reset button (always visible)
    screen.blit(titleUrl, (0, 0))
    screen.blit(resetUrl, (0,0))

    # draw in pieces
    for i in range(0, 19):
        for j in range(0, 19):
            if board[i][j] ==1:
                screen.blit(whiteUrl, (27+32*i, 27+32*j))
            if board[i][j]==2:
                screen.blit(blackUrl, (27+32*i, 27+32*j))

    # write in wins?

    pygame.display.flip()
    clock.tick(60)
pygame.quit()