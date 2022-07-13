
board = {'TL': 'X', 'TM': 'X', 'TR': 'X',
         'ML': 'O', 'MM': 'O', 'MR': 'O',
         'BL': 'X', 'BM': 'O', 'BR': 'X'}

ret = True

test_val = list(board.values())[0]

for elements in board:
    if board[elements] != test_val:
        ret = False
        break

print(test_val)