# File for handling user input and displaying current game state
import pygame as p
from chess import chessEngine
# Define some constants
# Initialise our pygame package
p.init()
WIDTH = 500
HEIGHT = 500
DIMENSION = 8
SQUARE_SIZE = WIDTH // DIMENSION
# Do not load the images for every operation - load once and save it once as key-value pairs
IMAGES = {}


def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bK', 'bQ', 'bP', 'wR', 'wN', 'wB', 'wK', 'wQ', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def drawBoard(screen):
    # Play around with the color scheme
    colors = [p.Color("burlywood"), p.Color("darkorange4")]
    # The top left of the board is always a light square
    # Starting from 0,0 - all light squares are divisible by 2 when you add their row and column
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col)%2)]
            p.draw.rect(screen, color, p.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            # Based on the value we are taking from the board in engine.py put the corresponding image
            piece = board[row][col]
            if piece != "xx":
                # Image needs to be added in these squares
                screen.blit(IMAGES[piece], p.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawGameState(screen, gs):
    # First draw board, then pieces since the pieces get covered if done the other way around
    # Draw the squares on the chessboard
    drawBoard(screen)
    # Add the piece images onto the board
    drawPieces(screen, gs.board)


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chessEngine.GameState()
    loadImages()
    # print(gs.board) works!
    # Keep track of selected square - row and column
    selected_square = ()
    # 2 tuples containing the selected piece's current location and where the user moves it to
    player_clicks = []


    flag = True

    while flag:
        for e in p.event.get():
            if e.type == p.QUIT:
                flag = False
            elif e.type == p.KEYDOWN:
                # Undo functionality - press z key 
                if e.key == p.K_z:
                    gs.undoMove()

            elif e.type == p.MOUSEBUTTONDOWN:
                # Grab the mouse location to move the piece
                location = p.mouse.get_pos()
                col = location[0]//SQUARE_SIZE
                row = location[1]//SQUARE_SIZE
                # Do not let the user click the same square twice
                # If the action occurs, undo the move
                if selected_square == (row, col):
                    selected_square = ()
                    player_clicks = []
                else:
                    selected_square = (row, col)
                    player_clicks.append(selected_square)

                # After the second click, perform the move and reset the player_clicks
                if len(player_clicks) == 2:
                    move = chessEngine.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    # Reset the move clicks so length becomes 0 again
                    selected_square = ()
                    player_clicks = []


        drawGameState(screen, gs)
        clock.tick(20) # Kept 20 Frames per second
        p.display.flip()


if __name__ == "__main__":
    main()
