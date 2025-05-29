from random import randrange

# for i in range(100):
#     print(randrange(1, 8))
# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        print(("+" + "-" * 7) * 3 + "+")
        print(("|" + " " * 7) * 3 + "|")
        for column in row:
            print("|" + " " * 3 + str(column) + " " * 3, end="")
        print("|")
        print(("|" + " " * 7) * 3 + "|")
    print(("+" + "-" * 7) * 3 + "+")
    print()

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free_squares = make_list_of_free_fields(board)

    while True:
        try:
            print("Free Squares: ", str(free_squares))

            user_move = int(input('Your move: '))
            
            if user_move <= 0 or user_move >= 10:
                print("Move must be 1 to 9 only.")
            elif user_move not in free_squares:
                print("Move must be belong in free squares.")
            else:
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == user_move:
                            board[i][j] = "O"
                            if victory_for(board, "O") == None:
                                return draw_move(board)
        except ValueError:
            print("Move must be 1 to 9 only.")
    
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in ["O", "X"]:
                    free_squares.append((i, j))
    
    if len(free_squares) == 0:
        print("The game ended with a tie!")
        exit()
    
    free_squares_values = []
    for square in free_squares:
        free_squares_values.append(board[square[0]][square[1]])
    return free_squares_values

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    winning_strokes = [
        #horizontal
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        #vertical
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        #diagonal
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
    ]
    
    for stroke in winning_strokes:
        match_count = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == sign and (i, j) in stroke:
                    match_count += 1
        
        if match_count == 3:
            display_board(board)
            if sign == "O":
                print("The winner is user!")
            if sign == "X":
                print("The winner is computer!")
            exit()
                    
    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    while True:
        computer_move = randrange(1, 10)
        
        if computer_move in make_list_of_free_fields(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == computer_move:
                        board[i][j] = "X"
                        display_board(board)
                        print("Computer moves to", computer_move)
                        if victory_for(board, "X") == None:
                            return enter_move(board)


#start game
display_board(board)
enter_move(board)
