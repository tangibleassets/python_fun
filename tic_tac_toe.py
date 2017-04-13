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
my_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
game_over = False

import os


def print_board(v):
    os.system('cls' if os.name == 'nt' else 'clear')
    print '-----------------------'
    print ' ' + v[1] + ' | ' + v[2] + ' | ' + v[3] + '       1|2|3'
    print '-----------      ------'
    print ' ' + v[4] + ' | ' + v[5] + ' | ' + v[6] + '       4|5|6'
    print '-----------      ------'
    print ' ' + v[7] + ' | ' + v[8] + ' | ' + v[9] + '       7|8|9'
    print '-----------------------'
    print ''


def make_a_move(location, value):
    my_board[location] = value
    print_board(my_board)
    check_game_status(my_board)


def clear_the_board():
    for keys in my_board:
        my_board[keys] = ' '


# Check if the game is won,tied, lost, or ongoing.
def check_game_status(b):
    winning_position_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    global game_over
    for pos in winning_position_combos:
        x = b[pos[0]].strip().lower()
        y = b[pos[1]].strip().lower()
        z = b[pos[2]].strip().lower()
        if x != '' and y != '' and z != '':
            if x == y == z:
                print 'Player "' + x + '" you win !!!!'
                print 'If you would like to play again - enter \'y\' at the next prompt'
                game_over = True
                break
    if not game_over:
        count = 0
        for value in b:
            if b[value].strip() == '':
                count += 1
        if count == 0:
            print "Tie Game :(  Try again?"
            game_over = True


def yes_lets_play():
    global game_over
    game_over = False
    return raw_input("Would you like to play a game? y/n:").lower().startswith('y')



def get_int_1_to_9(prompt):
    while True:
        try:
            value = int(raw_input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 1 or value > 9:
            print("Sorry, your response must be a number between 1 and 9.")
            continue
        else:
            break
    return value


def get_str_x_or_o(prompt):
    while True:
        try:
            value = str(raw_input(prompt)).lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value != 'x' and value != 'o':
            print("Sorry, your response must be 'x' or 'o':")
            continue
        else:
            break
    return value


while yes_lets_play():
    clear_the_board()
    print_board(my_board)
    while yes_lets_play:
        x_or_o = get_str_x_or_o("Enter either x or o:")
        position = get_int_1_to_9("Enter position a number [1-9]:")
        if my_board[position].strip() == '':
            make_a_move(position, x_or_o)
        else:
            print 'That position has already been played - try again.'
            continue
        if game_over:
            break
else:
    print 'Thanks for playing - have a nice day!'

