# Global var to store board values
my_board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

def print_board(v):
    print '-----------------------'
    print ' ' + v[1] + ' | ' + v[2] + ' | ' + v[3] + '       1|2|3'
    print '-----------      ------'
    print ' ' + v[4] + ' | ' + v[5] + ' | ' + v[6] + '       4|5|6'
    print '-----------      ------'
    print ' ' + v[7] + ' | ' + v[8] + ' | ' + v[9] + '       7|8|9'
    print '-----------------------'


# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board

print_board(my_board)

def make_a_move(location, value):
    my_board[location] = value
    print_board(my_board)

def clear_the_board():
    for keys in my_board:
        my_board[keys] = ' '
    print_board(my_board)
