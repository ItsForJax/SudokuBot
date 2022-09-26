board = [[7,3,1,8,9,2,5,4,6],
         [2,8,0,5,7,0,0,0,0],
         [0,6,0,1,0,3,0,0,8],
         [8,0,6,9,2,1,7,0,5],
         [1,0,5,0,0,0,0,2,0],
         [9,0,3,7,6,0,8,1,4],
         [6,0,0,0,0,0,3,0,7],
         [0,1,0,0,3,0,0,0,0],
         [0,0,0,2,0,7,4,6,0]]
solved = []

def validate(n,x,y):
    horizontalValid = n not in board[x]
    verticalValid = n not in [board[q][y] for q in range(9)]
    gridValid = n not in [board[q][w] for q in range(x//3*3,x//3*3+3)for w in range(y//3*3,y//3*3+3)]
    return horizontalValid and verticalValid and gridValid


def solve():
    global solved
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1,10):
                    if validate(n,x,y):
                        board[x][y] = n
                        solve()
                        board[x][y] = 0
                return
    solved = [board[x][y] for x in range(9) for y in range(9)]
