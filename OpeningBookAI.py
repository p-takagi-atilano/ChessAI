# Paolo Takagi-Atilano, October 4


import chess
from random import randint
from AlphaBetaAI import TransAlphaBetaAI

# opening dictionaries for white and black
w_openings = {0: "e2e4 g1f3 b1c3", 1: "e2e4 g1f3 f1b5", 2: "e2e4 d1h5 f1c4", 3: "d2d4 c2c4 f1c3"}
b_openings = {0: "e7e5 g8f6 b8c6", 1: "g7g6 f8g7 d7d5", 2: "d7d5 a7a5 a8a6", 3: "d7d5 e7e5 g8f6"}


class OpeningBookAI:
    def __init__(self, heuristic_fn, depth):
        self.ai = TransAlphaBetaAI(heuristic_fn, depth)
        self.opening = randint(0, 3)
        self.moves = 0
        self.moves_list = None

    def choose_move(self, board):
        move = None

        # first move, must decide opening to play
        if self.moves == 0:
            if board.turn == chess.WHITE: # player is white
                self.moves_list = w_openings[self.opening].split()
            else:                         # player is black
                self.moves_list = b_openings[self.opening].split()
        # still playing openings
        if self.moves < 3:
            move = chess.Move.from_uci(self.moves_list[self.moves])

        # opening is done, start using AI
        else:
            move = self.ai.choose_move(board)

        # increment moves, return move
        self.moves += 1
        return move
