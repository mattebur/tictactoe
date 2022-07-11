import error as err
import functions as fun


board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
         'ML': ' ', 'MM': ' ', 'MR': ' ',
         'BL': ' ', 'BM': ' ', 'BR': ' '}

availableMoves = ['TL', 'TM', 'TR','ML', 'MM', 'MR','BL','BM','BR']
turn = 'X'
fun.printing_board(board)


for i in range(9):
    try:
            move = input('Player ' + turn + ' Enter your move: ')
            if move not in availableMoves:
                raise err.InvalidUserInput
            board[move] = turn

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            fun.printing_board(board)

    except err.InvalidUserInput:
        print('Thats not position')