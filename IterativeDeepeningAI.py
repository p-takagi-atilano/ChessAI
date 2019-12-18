import chess
from MinimaxAI import MinimaxAI


class IterativeDeepeningAI():
    def __init__(self, heuristic_fn, depth):
        self.depth = depth
        self.heuristic_fn = heuristic_fn

    def choose_move(self, board):
        best_move = None                              # best_move temporarily set to None
        minimax_ai = MinimaxAI(self.heuristic_fn, 0)  # depth temporarily set to 0

        # iterates though depths
        for depth in range(0, self.depth + 1):

            # changes and fixes depth
            minimax_ai.depth = depth
            minimax_ai.reset_depth_fix()

            # stores and prints the best move for this depth
            best_move = minimax_ai.choose_move(board)
            print(str(depth) + ": " + str(best_move))

        return best_move
