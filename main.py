# Example file showing a basic pygame "game loop"
import pygame

# Init Constants
BOX_AREA = 20
BOARD_WITH = 800
BOARD_LENGTH = 800
NUM_BOX = int(BOARD_WITH/20)

def initRealBoard(board):
    for x in range(0,NUM_BOX):
        for y in range(0,NUM_BOX):
            board[x][y] = 0
    
    board[3][4] = 1
    board[4][4] = 1
    board[5][4] = 1
    return board

def copyBoard(board, oldBoard):
    for x in range(0,NUM_BOX):
        for y in range(0,NUM_BOX):
            oldBoard[x][y] = board[x][y] 

def switchStatusBox(x, y, board):
    board[x][y] = not board[x][y] 

def actuBoard(realBoard, oldBoard):
    for x in range(0,NUM_BOX):
        for y in range(0,NUM_BOX):
            if oldBoard[x][y] == 1:
                if not alive(x,y, oldBoard):
                    switchStatusBox(x, y, realBoard)
            else:
                if revive(x,y, oldBoard):
                    switchStatusBox(x, y, realBoard)

def alive(x, y, board):
    number = countNum(x,y,board, 1)
    return (number == 2 or number == 3)


def revive(x,y, board):
    number = countNum(x,y,board, 1)
    return number == 3

def countNum(x,y,board, num):
    count = 0
    if notOverFlowIndex(x+1, y+1) and board[x+1][y+1] == num:
        count+=1
    if notOverFlowIndex(x-1, y+1) and board[x-1][y+1] == num:
        count+=1
    if notOverFlowIndex(x+1, y-1) and board[x+1][y-1] == num:
        count+=1
    if notOverFlowIndex(x-1, y-1) and board[x-1][y-1] == num:
        count+=1
    if notOverFlowIndex(x+1, y) and board[x+1][y] == num:
        count+=1
    if notOverFlowIndex(x-1, y) and board[x-1][y] == num:
        count+=1
    if notOverFlowIndex(x, y+1)and board[x][y+1] == num:
        count+=1
    if notOverFlowIndex(x, y-1) and board[x][y-1] == num:
        count+=1   
    return count

def notOverFlowIndex(x, y):
    return x <= NUM_BOX-1 and x >= 0 and y <= NUM_BOX-1 and y >= 0
if __name__ == '__main__':
    pygame.init()
    size = [840,840]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    color = (0, 255, 0)

    realBoard = [list(range(NUM_BOX)) for _ in range(NUM_BOX)]
    realBoard = initRealBoard(realBoard)
    oldBoard = [list(range(NUM_BOX)) for _ in range(NUM_BOX)]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x = int(event.pos[0]/BOX_AREA)
                y = int(event.pos[1]/BOX_AREA)
                if notOverFlowIndex(x,y):
                    switchStatusBox(x, y, realBoard)

        screen.fill("black")
        for i in range(0, BOARD_LENGTH, BOX_AREA):
            x = int(i/BOX_AREA)
            for j in range(0, BOARD_WITH, BOX_AREA):
                y = int(j/BOX_AREA)
                if realBoard[x][y]:
                    color = (255, 255, 0)
                else:
                    color = (0,255,0)
                pygame.draw.rect(screen, color, [i,j,BOX_AREA,BOX_AREA ],0)
        pygame.display.flip()
        clock.tick(2)
        copyBoard(realBoard, oldBoard)
        actuBoard(realBoard, oldBoard)
    pygame.quit()
