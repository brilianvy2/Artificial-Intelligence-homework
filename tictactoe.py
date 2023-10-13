import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
    
    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("-" * 9)
    
    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def is_full(self):
        return ' ' not in self.board
    
    def terminal_node(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return True, self.board[combo[0]]

        if ' ' not in self.board:
            return True, 'Tie'
        
        return False, None
    
    def expand_state(self):
        return [i for i in range(9) if self.board[i] == ' ']
    
    def minimax(self, depth, is_max_player):
        terminal, result = self.terminal_node()

        if terminal:
            if result == 'X':
                return 10 - depth
            elif result == 'O':
                return depth - 10
            else:
                return 0

        if is_max_player:
            max_eval = -math.inf
            for pos in self.expand_state():
                self.board[pos] = 'X'
                eval = self.minimax(depth + 1, False)
                self.board[pos] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for pos in self.expand_state():
                self.board[pos] = 'O'
                eval = self.minimax(depth + 1, True)
                self.board[pos] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def get_best_move(self):
        best_move = None
        best_eval = -math.inf

        for pos in self.expand_state():
            self.board[pos] = 'X'
            eval = self.minimax(0, False)
            self.board[pos] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = pos

        return best_move

def main():
    game = TicTacToe()
    while True:
        game.display_board()

        if game.is_full():
            print("It's a tie!")
            break

        if ' ' not in game.board:
            print("The board is full. It's a tie!")
            break

        # Human player's move
        while True:
            try:
                position = int(input("Enter position (0-8): "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue

            if 0 <= position <= 8:
                if game.make_move(position, 'O'):
                    break
                else:
                    print("Cell already taken. Try again.")
            else:
                print("Invalid input. Position must be between 0 and 8.")

        terminal, result = game.terminal_node()
        if terminal:
            game.display_board()
            if result == 'O':
                print("You win!")
            elif result == 'X':
                print("AI wins!")
            else:
                print("It's a tie!")
            break

        # AI's move using minimax
        ai_move = game.get_best_move()
        game.make_move(ai_move, 'X')

        terminal, result = game.terminal_node()
        if terminal:
            game.display_board()
            if result == 'O':
                print("You win!")
            elif result == 'X':
                print("AI wins!")
            else:
                print("It's a tie!")
            break

if __name__ == "__main__":
    main()

