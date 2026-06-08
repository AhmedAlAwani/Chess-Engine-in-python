# UI and user data
import pygame as p
import  engine

width = height = 512
dimension = 8
sq_size= height//dimension
max_fps= 15
images={}

#load images
def load_images():
    pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR','wp','bp','bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR']
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load('images/'+piece+'.png'),(sq_size,sq_size))

#main driver for the code and updating the graphics
def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs=engine.GameState()
    load_images()
    running = True
    while running:
        for i in p.event.get():
            if i.type == p.QUIT:
                running = False
            clock.tick(max_fps)
            p.display.flip()
            drawGameState(screen, gs)

#For the graphics in the current game
def drawGameState(screen,gs):
    drawBoard(screen)
    drawPieces(screen,gs.board)


#Drawing the board
def drawBoard(screen):
    colors =[p.Color('white'), p.Color('gray')]
    for r in range(dimension):
        for c in range(dimension):
            color=colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*sq_size, r*sq_size, sq_size, sq_size))

#Drawing the pieces
def drawPieces(screen,board ):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != '--':
                screen.blit(images[piece],p.Rect(c*sq_size, r*sq_size, sq_size, sq_size))





if __name__ == '__main__':
    main()


