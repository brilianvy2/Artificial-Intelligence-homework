## Problem: Tic-Tac-Toe game
# 'x' = 1 
# 'o' = -1
# empty = 0
# state: [[0,0,1],[0,-1,0],[0,0,0]]
# 'x' starts first
# The one who makes a row, a column, 
# or a diagonal of the same type wins

class TicTacToe():
    # initialize game with some state
    def __init__(self, state=[[0,0,0],[0,0,0],[0,0,0]]):
        self.state = state
    def best_move(self):
        best_score = -float("inf")
        best_move = None
        for (row, col) in self.expand_state(self.state):
            if self.try_move(self.state, row, col, 1):
                score = self.minimax(self.state, 0, False)
                self.try_move(self.state, row, col, 0)  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
        return best_move

    def minimax(self, state, depth, is_maximizing):
        result = self.terminal_node(state)

        if result["gameover"]:
            return result["result"]

        if is_maximizing:
            best_score = -float("inf")
            for (row, col) in self.expand_state(state):
                if self.try_move(state, row, col, 1):
                    score = self.minimax(state, depth + 1, False)
                    self.try_move(state, row, col, 0)  # Undo the move
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for (row, col) in self.expand_state(state):
                if self.try_move(state, row, col, -1):
                    score = self.minimax(state, depth + 1, True)
                    self.try_move(state, row, col, 0)  # Undo the move
                    best_score = min(score, best_score)
            return best_score

# make a real move: set val to the cell
# with coordinates [row, col]
def make_move(self, row, col, val):
        made_move = False
        if (isinstance(row, int)) and (row>=0) and (row<=2):
            if (isinstance(col, int)) and (col>=0) and (col<=2):
                if self.state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        self.state[row][col] = val
                        made_move = True

        return made_move

# try a move: set val to the cell
# with coordinates [row, col]
def try_move(state, row, col, val):
        if (isinstance(row, int)) and (row>=0) and (row<=2):
            if (isinstance(col, int)) and (col>=0) and (col<=2):
                if state[row][col] == 0:
                    if (val == -1) or (val == 1):
                        state[row][col] = val
                        
        return state

# check if the terminal node
def terminal_node(state):
        # result of the game
        # win1 = +10, win2 = -10, tie=0
        result = 0
        isGameOver = False
    
        # check if there is an empty cell
        emptyCells = False
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    emptyCells = True

        # check rows if there is a winner
        isWinner = False
        for i in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for j in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True 
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        # check cols if there is a winner
        for j in range(3):
            sum_p1 = 0
            sum_p2 = 0
            for i in range(3):
                if state[i][j] == 1:
                    sum_p1 += 1
                if state[i][j] == -1:
                    sum_p2 += -1
            if (sum_p1 == 3) or (sum_p2 == -3):
                isWinner = True 
                if (sum_p1 == 3):
                    result = 10
                if (sum_p2 == -3):
                    result = -10

        # check diagonals if there is a winner
        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][i] == 1:
                sum_p1 += 1
            if state[i][i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True 
            if (sum_p1 == 3):
               result = 10
            if (sum_p2 == -3):
               result = -10
            
        sum_p1 = 0
        sum_p2 = 0
        for i in range(3):
            if state[i][2-i] == 1:
                sum_p1 += 1
            if state[i][2-i] == -1:
                sum_p2 += -1
        if (sum_p1 == 3) or (sum_p2 == -3):
            isWinner = True 
            if (sum_p1 == 3):
               result = 10
            if (sum_p2 == -3):
               result = -10

        isGameOver = isWinner or not emptyCells
        return {"gameover": isGameOver, "result": result}
                
# find the children of the given state
# returns the coordinates (x,y) of empty cells
def expand_state(state):
    children = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                child = [i,j]
                children.append(child)
    return children


# setup the game
state = [[0, 1, 1],[-1,0,1],[0,1,-1]]
x,y = terminal_node(state)
print(x,y)
ch = expand_state(state)
print(ch)
