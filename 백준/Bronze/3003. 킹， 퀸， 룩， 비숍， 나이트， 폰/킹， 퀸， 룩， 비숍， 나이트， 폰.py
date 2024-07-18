chess_pieces = [1, 1, 2, 2, 2, 8]
chess_pieces_input = list(map(int, input().split()))
# chess_king == chess_pieces[0]
# chess_queen == chess_pieces[1]
# chess_rook == chess_pieces[2]
# chess_bishop == chess_pieces[3]
# chess_knight == chess_pieces[4]
# chess_pawn == chess_pieces[5]


for i in range(len(chess_pieces)):
    chess_pieces_input[i] = chess_pieces[i] - chess_pieces_input[i]

print(*chess_pieces_input)