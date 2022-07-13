import random
import error as err
def printing_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('------')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('------')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])



def check_if_win(board):
    check = False
    if board['TL'] == board['TM'] == board['TR'] != ' ':
        check = True
    elif board['TL'] == board['MM'] == board['BR'] != ' ':
        check = True
    elif board['TL'] == board['ML'] == board['BL'] != ' ':
        check = True
    elif board['ML'] == board['MM'] == board['MR'] != ' ':
        check = True
    elif board['BL'] == board['MM'] == board['TR'] != ' ':
        check = True
    elif board['BL'] == board['BM'] == board['BR'] != ' ':
        check = True
    elif board['TM'] == board['MM'] == board['BM'] != ' ':
        check = True
    elif board['TR'] == board['MR'] == board['BR'] != ' ':
        check = True

    return check

def game(board):

    players = ['O', 'X']
    turn = random.choice(players)  # random selecting who starts

    movecounter = 0

    availablemoves = ['TL', 'TM', 'TR', 'ML', 'MM', 'MR', 'BL', 'BM', 'BR']
    printing_board(board)
    while movecounter < 9:
        try:
            move = input('Player ' + turn + ' Enter your move: ')
            if move not in availablemoves:
                raise err.InvalidUserInput
            while True:
                if board[move] == ' ':
                    board[move] = turn
                    movecounter += 1
                    break
                else:
                    print('place taken!')
                    break

            if check_if_win(board):
                printing_board(board)
                print()
                print('The winner is ' + turn)
                break

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            printing_board(board)

        except err.InvalidUserInput:
            printing_board(board)
            print('That\'s not position')
