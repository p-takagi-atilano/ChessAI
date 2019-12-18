# Paolo Takagi-Atilano, October 3rd

import chess

# Material Value Systems: #

STANDARD_VALUES = {"pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": 200}


# Heuristics: #

# material count according to the STANDARD_VALUES dictionary
def std_get_material(board, depth_fix):

    # white pieces
    w_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
    w_knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
    w_bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
    w_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
    w_queens = len(board.pieces(chess.QUEEN, chess.WHITE))
    w_kings = len(board.pieces(chess.KING, chess.WHITE))

    # black pieces
    b_pawns = len(board.pieces(chess.PAWN, chess.BLACK))
    b_knights = len(board.pieces(chess.KNIGHT, chess.BLACK))
    b_bishops = len(board.pieces(chess.BISHOP, chess.BLACK))
    b_rooks = len(board.pieces(chess.ROOK, chess.BLACK))
    b_queens = len(board.pieces(chess.QUEEN, chess.BLACK))
    b_kings = len(board.pieces(chess.KING, chess.BLACK))

    # tally up the entire score
    material = (w_pawns - b_pawns) * STANDARD_VALUES["pawn"]
    material += (w_knights - b_knights) * STANDARD_VALUES["knight"]
    material += (w_bishops - b_bishops) * STANDARD_VALUES["bishop"]
    material += (w_rooks - b_rooks) * STANDARD_VALUES["rook"]
    material += (w_queens - b_queens) * STANDARD_VALUES["queen"]
    material += (w_kings - b_kings) * STANDARD_VALUES["king"]

    # reverse the material score if it is black's turn
    if board.turn == chess.BLACK:
        material *= -1

    # conduct depth fix
    if depth_fix:
        material *= -1

    return material
