# Paolo Takagi-Atilano, October 3rd

import chess
from heapq import heappush, heappop
from math import inf


class AlphaBetaAI:
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
            move_value = self.min_value(0, board, float('-inf'), float('inf'))
            board.pop()

            #print("MOVE: ", move)
            #print("SCORE: ", move_value)

            if move_value > final_value:
                final_value = move_value
                final_move = move

        #print("FINAL MOVE: ", final_move)
        print("FINAL SCORE: ", final_value)
        print("AlphaBeta AI recommending move " + str(final_move) + " after " + str(self.function_calls) + " function calls")
        return final_move

    # simulate max player
    def max_value(self, depth, board, alpha, beta):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find maximum possible value assuming min plays optimally
        v = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            v = max(v, self.min_value(depth + 1, board, alpha, beta))
            board.pop()

            # pruning
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    # simulate min player
    def min_value(self, depth, board, alpha, beta):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find minimum possible value assuming max plays optimally
        v = float('inf')
        for move in board.legal_moves:
            board.push(move)
            v = min(v, self.max_value(depth + 1, board, alpha, beta))
            board.pop()

            # pruning
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    def cutoff_test(self, depth, board):
        return self.depth <= depth or board.is_game_over()


# Alpha Beta with basic move reordering
class ReorderAlphaBetaAI:
    def __init__(self, heuristic_fn, depth):
        self.depth = depth
        self.heuristic_fn = heuristic_fn
        self.function_calls = 0
        self.depth_fix = (depth % 2 == 0)

    def choose_move(self, board):
        self.function_calls = 0
        moves_list = list(board.legal_moves)
        moves_heap = self.reorder(moves_list, board)

        # setup
        final_move = None  # temporarily set to None, must change to a move object
        final_value = float('-inf')

        # starts the loop off
        while moves_heap:
            move_pq = heappop(moves_heap)
            board.push(move_pq.move)
            move_value = self.min_value(0, board, float('-inf'), float('inf'))
            board.pop()

            #print("MOVE: ", move)
            #print("SCORE: ", move_value)

            if move_value > final_value:
                final_value = move_value
                final_move = move_pq.move

        #print("FINAL MOVE: ", final_move)
        print("FINAL SCORE: ", final_value)
        print("ReorderAlphaBeta AI recommending move " + str(final_move) + " after " + str(
            self.function_calls) + " function calls")
        return final_move

    # simulate max player
    def max_value(self, depth, board, alpha, beta):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find maximum possible value if min plays optimally
        v = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            v = max(v, self.min_value(depth + 1, board, alpha, beta))
            board.pop()

            # pruning
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    # simulate min player
    def min_value(self, depth, board, alpha, beta):

        # increment function calls count
        self.function_calls += 1

        # checks to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find maximum possible value if min plays optimally
        v = float('inf')
        for move in board.legal_moves:
            board.push(move)
            v = min(v, self.max_value(depth + 1, board, alpha, beta))
            board.pop()

            # pruning
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    # cutoff test, returns true if depth limit is reached or game is over, false otherwise
    def cutoff_test(self, depth, board):
        return self.depth <= depth or board.is_game_over()

    # uses provided heuristic to order moves
    def reorder(self, moves_list, board):

        # the empty heap
        ordered = []

        # building the heap
        for move in moves_list:
            board.push(move)
            priority = self.heuristic_fn(board, self.depth_fix)
            heappush(ordered, MovePq(move, priority))
            board.pop()

        return ordered


# Alpha Beta AI with move reordering and transposition table
class TransAlphaBetaAI:
    def __init__(self, heuristic_fn, depth):
        self.depth = depth
        self.heuristic_fn = heuristic_fn
        self.function_calls = 0
        self.depth_fix = (depth % 2 == 0)

    def choose_move(self, board):
        self.function_calls = 0
        moves_list = list(board.legal_moves)
        moves_heap = self.reorder(moves_list, board)
        transposition_table = {}

        # setup
        final_move = None  # temporarily set to None, must change to a move object
        final_value = float('-inf')

        # starts the loop off
        while moves_heap:
            move_pq = heappop(moves_heap)
            board.push(move_pq.move)
            move_value = self.min_value(0, board, float('-inf'), float('inf'), transposition_table)
            board.pop()

            #print("MOVE: ", move)
            #print("SCORE: ", move_value)

            if move_value > final_value:
                final_value = move_value
                final_move = move_pq.move

        #print("FINAL MOVE: ", final_move)
        print("FINAL SCORE: ", final_value)
        print("TransAlphaBeta AI recommending move " + str(final_move) + " after " + str(
            self.function_calls) + " function calls")

        return final_move

    # simulate max player
    def max_value(self, depth, board, alpha, beta, transposition_table):

        # increment function calls count
        self.function_calls += 1

        # check to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find maximum possible value if min plays optimally
        v = float('-inf')
        for move in board.legal_moves:
            board.push(move)

            # transposition table checks
            board_str = str(board)
            if board_str not in transposition_table.keys() or transposition_table[board_str] < v:
                v = max(v, self.min_value(depth + 1, board, alpha, beta, transposition_table))
                transposition_table[board_str] = v
            else:
                v = transposition_table[board_str]
            board.pop()

            # pruning
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    # simulate min player
    def min_value(self, depth, board, alpha, beta, transposition_table):

        # increment function calls count
        self.function_calls += 1

        # check to see if it is a cutoff
        if self.cutoff_test(depth, board):
            return self.heuristic_fn(board, self.depth_fix)

        # find minimum possible value if max plays optimally
        v = float('inf')
        for move in board.legal_moves:
            board.push(move)

            # transposition table checks
            board_str = str(board)
            if board_str not in transposition_table.keys() or transposition_table[board_str] < v:
                v = min(v, self.max_value(depth + 1, board, alpha, beta, transposition_table))
                transposition_table[board_str] = v
            else:
                v = transposition_table[board_str]
            board.pop()

            # pruning
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    # cutoff test, returns true if depth limit is reached or game is over, false otherwise
    def cutoff_test(self, depth, board):
        return self.depth <= depth or board.is_game_over()

    # uses provided heuristic to order moves
    def reorder(self, moves_list, board):
        ordered = []
        for move in moves_list:
            board.push(move)
            priority = self.heuristic_fn(board, self.depth_fix)
            heappush(ordered, MovePq(move, priority))
            board.pop()
        return ordered


# class used to rank nodes for move reordering
class MovePq:
    def __init__(self, move, priority):
        self.move = move
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority
