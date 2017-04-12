# We need to print a board.
# Take in player input.
# Place their input on the board.
# Check if the game is won,tied, lost, or ongoing.
# Repeat c and d until the game has been won or tied.
# Ask if players want to play again.
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board


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

print_board(my_board)

def make_a_move(location, value):
    my_board[location] = value
    print_board(my_board)
    check_game_status(my_board)

def clear_the_board():
    for keys in my_board:
        my_board[keys] = ' '
    print_board(my_board)
    
# Check if the game is won,tied, lost, or ongoing.
def check_game_status(b):
    winning_position_combos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]    
    for pos in winning_position_combos:
        x = b[pos[0]].strip().lower()
        y = b[pos[1]].strip().lower()
        z = b[pos[2]].strip().lower()
        if x != '' and y != '' and z != '':
            if x == y == z:
                print 'Player "' + x + '" you win !!!!'
                clear_the_board()
                print 'Ready to play again?'
                break
    count = 0
    for value in b:
        if b[value].strip() == '':
            count += 1
    if count == 0:
        print "Tie Game :(  Try again?"
        clear_the_board()
