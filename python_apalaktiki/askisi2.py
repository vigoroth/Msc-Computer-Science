import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))

def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):
            l.append((i, j))
    return(l)

# Select a random place for the player
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    if board[current_loc]==0:
        board[current_loc] = player
    elif board[current_loc]==1 and player>1:
        board[current_loc] = player
    elif board[current_loc]==1 and player<=1:
        current_loc = random.choice(selection)
    elif board[current_loc]==2 and player>2:
        board[current_loc] = player
    elif board[current_loc]==2 and player<=2:
        current_loc = random.choice(selection)
    elif board[current_loc]==3 and player<=3:
        current_loc = random.choice(selection)
    return(board)


def evaluate(board):
    winner = 0
    if board[0][0] and board[0][1] and board[0][2] != 0 :
        if second_evaluation_row(board)==1:
            print("win first row")
            winner = 1
    elif board[1][0] and board[1][1] and board[1][2] != 0 :
        if second_evaluation_row(board)==1:
            print("win second row")
            winner = 1
    elif board[2][0] and board[2][1] and board[2][2] != 0 :
        if second_evaluation_row(board)==1:
            print("win third row")
            winner = 1
    elif board[0][0] and board[1][1] and board[2][2] != 0 :
        if second_evaluation_diag_right(board)==1:
            print("win daigonial right")
            winner = 1
    elif board[2][0] and board[1][1] and board[0][2] != 0 :
        if second_evaluation_diag_left(board)==1:
            print("win daigonial left")
            winner = 1
    elif board[0][0] and board[1][0] and board[2][0] != 0 :
        if second_evaluation_col(board)==1:
            print("Win first column")
            winner = 1
    elif board[0][1] and board[1][1] and board[2][1] != 0 :
        if second_evaluation_col(board)==1:
            print("Win second column")
            winner = 1
    elif board[0][2] and board[1][2] and board[2][2] != 0 :
        if second_evaluation_col(board)==1:
            print("Win third column")
            winner = 1
    return winner


def second_evaluation_diag_right(board):
    winner=0
    if board[0][0]==1 and board[1][1]==1 and board[2][2]==1:
            winner = 1
    elif board[0][0]==2 and board[1][1]==2 and board[2][2]==2:
            winner = 1
    elif board[0][0]==3 and board[1][1]==3 and board[2][2]==3:
            winner = 1
    elif board[0][0]==1 and board[1][1]==2 and board[2][2]==3:
            winner = 1
    elif board[0][0]==3 and board[1][1]==2 and board[2][2]==1:
            winner = 1
    return(winner)
def second_evaluation_diag_left(board):
    winner=0
    if board[0][2]==1 and board[1][1]==1 and board[2][0]==1:
            winner = 1
    elif board[0][2]==2 and board[1][1]==2 and board[2][0]==2:
            winner = 1
    elif board[0][2]==3 and board[1][1]==3 and board[2][0]==3:
            winner = 1
    elif board[0][2]==1 and board[1][1]==2 and board[2][0]==3:
            winner = 1
    elif board[0][2]==3 and board[1][1]==2 and board[2][0]==1:
            winner = 1
    return(winner)
def second_evaluation_row(board):
    winner=0
    if board[0][0]==1 and board[0][1]==2 and board[0][2]==3:
      winner=1
    elif board[1][0]==1 and board[1][1]==2 and board[1][2]==3:
      winner=1
    elif board[2][0]==1 and board[2][1]==2 and board[2][2]==3:
      winner=1
    elif board[0][0]==1 and board[0][1]==1 and board[0][2]==1:
      winner=1
    elif board[1][0]==1 and board[1][1]==1 and board[1][2]==1:
      winner=1
    elif board[2][0]==1 and board[2][1]==1 and board[2][2]==1:
      winner=1
    elif board[0][0]==2 and board[0][1]==2 and board[0][2]==2:
      winner=1
    elif board[1][0]==2 and board[1][1]==2 and board[1][2]==2:
      winner=1
    elif board[2][0]==2 and board[2][1]==2 and board[2][2]==2:
      winner=1
    elif board[0][0]==3 and board[0][1]==3 and board[0][2]==3:
      winner=1
    elif board[1][0]==3 and board[1][1]==3 and board[1][2]==3:
      winner=1
    elif board[2][0]==3 and board[2][1]==3 and board[2][2]==3:
      winner=1
    elif board[0][0]==3 and board[0][1]==2 and board[0][2]==1:
      winner=1
    elif board[1][0]==3 and board[1][1]==2 and board[1][2]==1:
      winner=1
    elif board[2][0]==3 and board[2][1]==2 and board[2][2]==1:
      winner=1
    return(winner)
def second_evaluation_col(board):
    winner=0
    if board[0][0]==1 and board[1][0]==2 and board[2][0]==3:
      winner=1
    elif board[0][1]==1 and board[1][1]==2 and board[2][1]==3:
      winner=1
    elif board[0][2]==1 and board[1][2]==2 and board[2][2]==3:
      winner=1
    elif board[0][0]==1 and board[1][0]==1 and board[2][0]==1:
      winner=1
    elif board[0][1]==1 and board[1][1]==1 and board[2][1]==1:
      winner=1
    elif board[0][2]==1 and board[1][2]==1 and board[2][2]==1:
      winner=1
    elif board[0][0]==2 and board[1][0]==2 and board[2][0]==2:
      winner=1
    elif board[0][1]==2 and board[1][1]==2 and board[2][1]==2:
      winner=1
    elif board[0][2]==2 and board[1][2]==2 and board[2][2]==2:
      winner=1
    elif board[0][0]==3 and board[1][0]==3 and board[2][0]==3:
      winner=1
    elif board[0][1]==3 and board[1][1]==3 and board[2][1]==3:
      winner=1
    elif board[0][2]==3 and board[1][2]==3 and board[2][2]==3:
      winner=1
    elif board[0][0]==3 and board[1][0]==2 and board[2][0]==1:
      winner=1
    elif board[0][1]==3 and board[1][1]==2 and board[2][1]==1:
      winner=1
    elif board[0][2]==3 and board[1][1]==2 and board[2][2]==1:
      winner=1
    return(winner)



# Main function to start the game
def play_game():
    caps= [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]
    random_index = random.randrange(len(caps))
    board, winner, counter = create_board(), 0, 1
    a=[]
    while winner == 0:
            player=caps[random_index]
            board = random_place(board, player)
            if counter>=3:
                winner = evaluate(board)
                if winner != 0:
                    a.append(counter)
                    break
                if caps==0:
                    break
            counter += 1
    return(counter)
b=[]
for i in range(100):
    print(str(play_game()))
    temp= play_game()
    b.append(temp)
    print(len(b))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("the average steps to win is :\n",sum(b)/len(b))
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
