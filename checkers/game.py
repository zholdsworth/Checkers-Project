import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid = {}

    def winner(self):
        return self.board.winner

    def reset(self):
        self._init()

    def select(self, row, column):
        # If able to move there, piece will move. If not, piece will be unselected
        if self.selected:
            result = self._move(row, column)
            if not result:
                self.selected = None
                self.select(row, column)
        # If move is valid, return true. Else, return false.
        piece = self.board.get_piece(row, column)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, column):
        # Moving selected piece to spot selected if no other piece is already there
        piece = self.board.get_piece(row, column)
        if self.selected and piece == 0 and (row, column) in self.valid:
            self.board.move(self.selected, row, column)
            skipped = self.valid[(row, column)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, column = move
            pygame.draw.circle(self.win, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        # Changes moves back and forth
        self.valid = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
