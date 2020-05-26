#from IPython.display import clear_output

print("Let's have a game of tic tac toe!" +
      "\n\nIn order to play just use the number pad for your selections:" +
      "\n1 being the bottom left corner and nine being the top right hand corner.")

player1 = input("\nReady player 1....do you want to be X's or O's?: ")

# Input check to ensure only x's and o's are entered.
while player1.lower() != 'x' and player1.lower() != 'o':
    player1 = input("\nYou entered an incorrect character. Please select either 'x' or 'o': ")

# Below code assigns player characters to later determine order
if player1.lower() == 'x':
    player1 = 'x'
    player2 = 'o'
else:
    player1 = 'o'
    player2 = 'x'

# Defining list to be used as the framework of tic tac toe board
l = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Creating funciton to capture, validate, and store player1's moves on the board
def play1(move):
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        move = input("\nIncorrect input player 1. Please enter a value between 1 - 9: ")

    while l[int(move)] != ' ':
        move = input("\nIncorrect input. Board spot is taken. Try again player 1 : ")
        while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input("\nIncorrect input player 1. Please enter a value between 1 - 9: ")
    else:
        l[int(move)] = player1

    # Creating funciton to capture, validate, and store player2's moves on the board


def play2(move):
    while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        move = input("\nIncorrect input player 2. Please enter a value between 1 - 9: ")

    while l[int(move)] != ' ':
        move = input("\nIncorrect input. Board spot is taken. Try again player 2: ")
        while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input("\nIncorrect input player 2. Please enter a value between 1 - 9: ")
    else:
        l[int(move)] = player2

    # Creating function to call the board and display


def board():
    #clear_output()
    print('\n{}|{}|{}'.format(l[7], l[8], l[9]) +
          '\n-----' +
          '\n{}|{}|{}'.format(l[4], l[5], l[6]) +
          '\n-----' +
          '\n{}|{}|{}'.format(l[1], l[2], l[3]))


# For loop to restrict the game to a maximum of 9 turns
for n in range(0, 9):

    # First nested if/ then statement to check if there's a winner.
    if ''.join(l[1:4]) != 'xxx' and ''.join(l[1:4]) != 'ooo' and \
            ''.join(l[4:7]) != 'xxx' and ''.join(l[4:7]) != 'ooo' and \
            ''.join(l[7::]) != 'xxx' and ''.join(l[7::]) != 'ooo' and \
            ''.join(l[1] + l[4] + l[7]) != 'xxx' and ''.join(l[1] + l[4] + l[7]) != 'ooo' and \
            ''.join(l[2] + l[5] + l[8]) != 'xxx' and ''.join(l[2] + l[5] + l[8]) != 'ooo' and \
            ''.join(l[3] + l[6] + l[9]) != 'xxx' and ''.join(l[3] + l[6] + l[9]) != 'ooo' and \
            ''.join(l[1] + l[5] + l[9]) != 'xxx' and ''.join(l[1] + l[5] + l[9]) != 'ooo' and \
            ''.join(l[3] + l[5] + l[7]) != 'xxx' and ''.join(l[3] + l[5] + l[7]) != 'ooo':

        # If the there's no winner then bottom code execute to receive player input(x's and o's)
        # Another if/else statement is used to toggle between player 1 and player 2. This toggle is /
        # managed through a modulo operator
        if player1 == 'x':
            if (n + 1) % 2 == 0:

                move = input('Player 2, your move: ')

                play2(move)

                board()
                player = 'Player 2'
                n += 1
            else:
                move = input('Player 1, your move: ')

                play1(move)

                board()
                player = 'Player 1'
                n += 1
        else:
            if (n + 1) % 2 == 0:

                move = input('Player 1, your move: ')

                play1(move)

                board()
                player = 'Player 1'
                n += 1
            else:
                move = input('Player 2, your move: ')

                play2(move)

                board()
                player = 'Player 2'
                n += 1

    # if first if/else statement returns false. Then bottom code executes to break out of the loop
    # and declare a winner.
    else:
        print("\n")
        print('Congratulations ' + player + ' you won this round!')
        break