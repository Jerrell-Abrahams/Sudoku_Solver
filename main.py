board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]



# Function that prints the board.
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(bo[i][j])

            else:
                print(str(bo[i][j]) + " ", end="")
    print("**********************************************")


def is_available(num):
    if num == 0:
        return True
    else:
        return False


def validate_board(row, column, num, bo):
    #Row
    for i in range(len(bo[0])):
        if bo[row][i] == num:
            return False

    # Column
    for i in range(len(bo)):
        if bo[i][column] == num:
            return False

    # 3x3 Grid
    for i in range((row // 3)*3, (row // 3)*3 + 3):
        for j in range((column // 3) * 3, (column // 3)*3 + 3):
            if bo[i][j] == num:
                return False

    return True


def number_validator(bo, row, column):
    for num in range(1, 10):
        if validate_board(bo=bo, row=row, column=column, num=num):
            bo[row][column] = num
            solver(bo)
            bo[row][column] = 0


def solver(bo):
    for row in range(len(bo)):
        for column in range(len(bo[0])):
            if bo[row][column] == 0:
                number_validator(bo, row, column)
                return False
    print("Found Solution")
    print_board(bo)



print_board(board)
solver(board)


