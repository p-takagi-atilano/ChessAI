# Paolo Takagi-Atilano, October 3rd

# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from IterativeDeepeningAI import IterativeDeepeningAI
from AlphaBetaAI import AlphaBetaAI, ReorderAlphaBetaAI, TransAlphaBetaAI
from ChessGame import ChessGame
from OpeningBookAI import OpeningBookAI

import heuristics

import sys


# Initial Given Test
'''
player1 = HumanPlayer()
player2 = RandomAI()
'''

# Minimax Test
'''
player1 = RandomAI()
player2 = MinimaxAI(heuristics.std_get_material, 3)
'''
#player1 = TransAlphaBetaAI(heuristics.std_get_material, 3)
#player1 = HumanPlayer()
#player2 = TransAlphaBetaAI(heuristics.std_get_material, 3)
#player2 = TransAlphaBetaAI(heuristics.std_get_material, 5)
#player2 = AlphaBetaAI(heuristics.std_get_material, 5)

#print(player2.depth)

#game = ChessGame(player1, player2)
'''
Board 1:
Default board, no need for FEN notation

Board 2:
game.board = chess.Board("r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 0 1")

Board 3:
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")

Board 4:
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")

Board 5:
game.board = chess.Board("7k/8/8/Q6q/8/PPPP4/PPPP4/K7 b - - 0 1")
'''

##################
# Minimax Tests: #
##################

# Board 1: #

# Depth 0
player1 = MinimaxAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 1
player1 = MinimaxAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 2
player1 = MinimaxAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 3
player1 = MinimaxAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Board 3: #

# Depth 0
player1 = MinimaxAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = MinimaxAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = MinimaxAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = MinimaxAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Board 4: #

# Depth 0
player1 = MinimaxAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = MinimaxAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = MinimaxAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = MinimaxAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

##############################
# Iterative Deepening Tests: #
##############################

# Board 2: #
player1 = IterativeDeepeningAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r1bqkb1r/pp2pppp/2np1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 0 1")
print(game)
game.make_move()

# Board 5: #
player1 = IterativeDeepeningAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 4)

game = ChessGame(player2, player1)
game.board = chess.Board("7k/8/8/Q6q/8/PPPP4/PPPP4/K7 b - - 0 1")
print(game)
game.make_move()


#####################
# Alpha Beta Tests: #
#####################

### Normal: ###

# Board 1: #

# Depth 0
player1 = AlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 1
player1 = AlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 2
player1 = AlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 3
player1 = AlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Board 3: #

# Depth 0
player1 = AlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = AlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = AlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = AlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Board 4: #

# Depth 0
player1 = AlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = AlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = AlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = AlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

### Move Reordering: ###

# Board 1: #

# Depth 0
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 1
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 2
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 3
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Board 3: #

# Depth 0
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Board 4: #

# Depth 0
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = ReorderAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

### Transposition Table: ###

# Board 1: #

# Depth 0
player1 = TransAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 1
player1 = TransAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 2
player1 = TransAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Depth 3
player1 = TransAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
print(game)
game.make_move()

# Board 3: #

# Depth 0
player1 = TransAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = TransAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = TransAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = TransAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("r2q3k/pn2bprp/4pNp1/2p1PbQ1/3p1P2/5NR1/PPP3PP/2B2RK1 w - - 0 1")
print(game)
game.make_move()

# Board 4: #

# Depth 0
player1 = TransAlphaBetaAI(heuristics.std_get_material, 0)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 1
player1 = TransAlphaBetaAI(heuristics.std_get_material, 1)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 2
player1 = TransAlphaBetaAI(heuristics.std_get_material, 2)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

# Depth 3
player1 = TransAlphaBetaAI(heuristics.std_get_material, 3)
player2 = MinimaxAI(heuristics.std_get_material, 3)

game = ChessGame(player1, player2)
game.board = chess.Board("8/pkP5/8/8/P7/6q1/3Q2p1/2R2rK1 w - - 0 1")
print(game)
game.make_move()

######################
# Opening Book Test: #
######################

player1 = HumanPlayer()
player2 = OpeningBookAI(heuristics.std_get_material, 3)
game = ChessGame(player1, player2)
while not game.is_game_over():
    print(game)
    game.make_move()


'''
player1 = HumanPlayer()
player2 = AlphaBetaAI(heuristics.std_get_material, 3)
game = ChessGame(player1, player2)
while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
'''

