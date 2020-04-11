# A Basic Tic-Tac-Toe Game

board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

for i in board: 
    print(' '.join(i))

def print_board(board = board):
    for i in board:
        print(' '.join(i))

def move(player, x, y):
    '''
    player: 1, 2 (1 == 'X', 2 == 'O')
    x = left-to-right
    y = top-to-bottom
    '''
    ret_val = board[y][x] == '_'
    if (board[y][x] == '_'):
        board[y][x] = 'X' if player == 1 else 'O'
    else: 
        print("That's an illegal move!")
    print_board()
    return ret_val # True if good move, False if bad move

def isWin():
    '''
    Finds Winner
    '''
    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]):
        return board[0][0]
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        return board[1][0]
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        return board[2][0]
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        return board[0][0]
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        return board[0][1]
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return board[0][2]
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    elif (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return board[1][1]
    else:
        return False # No winners yet

player = 1
while True: 
    print("Hello, Player " + str(player) + "! Please make your move!")
    posx = int(input("Please input the X value of your move: "))
    posy = int(input("Please input the Y value of your move: "))
    if move(player, posx, posy):
        player = 1 if player == 2 else 2
    winner = isWin() # Store the winning character if there is a win, else it'll be false
    if type(winner) == str and not winner == '_':
        print("Congrats, Player " + ("2" if winner == 'O' else "1") + "! You won!")
        break
    

'''
_ _ _ <-- 0
_ _ _ <-- 1
_ _ _ <-- 2
^ ^ ^
0 1 2
'''
