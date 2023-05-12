import pygame
from .constants import *
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid = {}

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
        else:
            piece = self.board.get_piece(row, column)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, column):
        # Moving selected piece to spot selected if no other piece is already there
        piece = self.board.get_piece(row, column)
        if self.selected and piece == 0 and (row, column) in self.valid_moves:
            self.board.move(self.selected, row, column)
            self.change_turn()
        else:
            return False

        return True

    def change_turn(self):
        # Changes moves back and forth
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED