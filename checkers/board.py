import pygame
from .constants import *
from .pieces import Pieces

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLUMNS):
                # Determines where to place checker pieces
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Pieces(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Pieces(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.squares(win)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pieces = self.board[row][col]
                if pieces != 0:
                    pieces.draw(win)