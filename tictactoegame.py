# Python Tic Tac Toe

import random

# Game Board
board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

def checkAll(char):
    if checkLine(char, 0, 1, 2):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True

def show():
    print board[0], '|', board[1], '|', board[2]
    print '---------'
    print board[3], '|', board[4], '|', board[5]
    print '---------'
    print board[6], '|', board[7], '|', board[8]


while True:
    input = int(raw_input("Select a spot 0-8: "))

    if board[input] != 'x' and board[input] != 'o':
        board[input] = 'x'

        # Check for winner
        if checkAll('x'):
            print "X wins!"
            break

        while True: 
            opponent = random.randint(0, 8)
            if board[opponent] != 'o' and board[opponent] != 'x':
                board[opponent] = 'o'

                if checkAll('o'):
                    print "O wins!"
                    break

                break

    else:
        print "This spot is taken!"

    show()

