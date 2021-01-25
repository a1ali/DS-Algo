class TicTacToe:
    '''Management of a Tic-Tac-Toe game'''

    def __init__(self):
        '''start a new game'''
        self._board = [[' ']*3 for j in range(3)] #list comprehension to make empty board game
        self._player = 'X'

    def mark(self, i , j):
        '''put an X or O mark at position (i,j) for next players turn '''
        if not (0 <= i <= 2 and 0<= j <= 2):
            raise ValueError('Invalid board position')
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O' #switch to other player
        else:
            self._player = 'X'
        
    def _is_win(self, mark):
        '''check whether the board configuration is a win for the given player. '''
        board = self._board # local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) # rev diag

    def winner(self):
        '''Return mark of winning player on none to indicate a tie.'''
        for mark in 'XO':
            if self._is_win(mark):
                return mark 
        return None 

    def __str__(self):
        '''return string representation of current board game'''
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

game = TicTacToe()
while True:
    x = int(input(f'Enter x coordiante for {game._player}  plater:'))
    y = int(input(f'Enter Y coordinate for {game._player} player:'))
    game.mark(x, y)
    print(game)
    if (game._is_win('X')):
        print('Game over X wins')
        break
    elif(game._is_win('O')):
        print('Game over O wins')
        break

'''

Enter x coordiante for X  plater:1
Enter Y coordinate for X player:2
 | | 
-----
 | |X
-----
 | |
Enter x coordiante for O  plater:2
Enter Y coordinate for O player:2
 | | 
-----
 | |X
-----
 | |O
Enter x coordiante for X  plater:1
Enter Y coordinate for X player:1
 | | 
-----
 |X|X
-----
 | |O
Enter x coordiante for O  plater:2
Enter Y coordinate for O player:1
 | | 
-----
 |X|X
-----
 |O|O
Enter x coordiante for X  plater:1
Enter Y coordinate for X player:0
 | | 
-----
X|X|X
-----
 |O|O
Game over X wins


'''