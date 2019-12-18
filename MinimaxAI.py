# Paolo Takagi-Atilano, October 3rd

import chess
from math import inf

class MinimaxAI:
    def __init__(self, heuristic_fn, depth):
        self.depth = depth
        self.heuristic_fn = heuristic_fn
        self.function_calls = 0
        self.depth_fix = (depth % 2 == 0)

    def choose_move(self, board):
        self.function_calls = 0
        moves = list(board.legal_moves)

        # setup
        final_move = None  # temporarily set to None, must change to a move object
        final_value = float('-inf')

        # starts the loop off
        for move in moves:
            board.push(move)
            move_value = self.min_value(0, board)
            board.pop()

            #print("MOVE: ", move)
            #print("SCORE: ", move_value)

            if move_value > final_value:
                final_value = move_value
                final_move = move

        #print("FINAL MOVE: ", final_move)
        print("FINAL SCORE: ", final_value)
        print("Minimax AI recommending move " + str(final_move) + " after " + str(
            self.function_calls) + " function calls")
        return final_move

    # simulate max player
    def max_value(self, depth, board):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find maximum possible value assuming min plays optimally
        v = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            v = max(v, self.min_value(depth + 1, board))
            board.pop()

        return v

    # simulate min player
    def min_value(self, depth, board):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find minimum possible value assuming max plays optimally
        v = float('inf')
        for move in board.legal_moves:
            board.push(move)
            v = min(v, self.max_value(depth + 1, board))
            board.pop()

        return v

    # basic cutoff test
    def cutoff_test(self, depth, board):
        return self.depth <= depth or board.is_game_over()

    # redo depth fix for iteratative deepening
    def reset_depth_fix(self):
        self.depth_fix = (self.depth % 2 == 0)
