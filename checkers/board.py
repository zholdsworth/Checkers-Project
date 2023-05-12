import pygame
from .constants import *
from .pieces import Pieces


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, column):
        # Swamps values by reversing
        self.board[piece.row][piece.column], self.board[row][column] = \
            self.board[row][column], self.board[piece.row][piece.column]
        piece.move(row, column)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1

    def get_piece(self, row, column):
        return self.board[row][column]

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

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.column - 1
        right = piece.column + 1
        row = piece.row

        if piece.color == RED or piece.king:
            moves.update(self._move_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._move_right(row - 1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._move_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._move_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _move_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.updates(self._move_left(r + step, row, step, color, left - 1, skipped=last))
                    moves.updates(self._move_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1

        return moves

    def _move_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLUMNS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)

                    moves.updates(self._move_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.updates(self._move_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1

        return moves
