import random
import sys


class Game:
    def __init__(self, n, player):
        self.size = n
        self.player = player
        self.current_player = 'X'  # initial player is X
        self.board = [[0 for x in range(n)] for x in range(n)]
        self.move_count = n ** n
        self.scores = {
            "X": 10,
            "O": -10,
            "tie": 0
        }

    def is_move_available(self):
        if (self.moveCount == 0):
            return False
        else:
            return True

    def check_winner(self):
        # check rows for winner
        def check_rows():
            count = 0
            first_elem = None
            winner = None
            for i in range(len(self.board)):
                if (winner):
                    break
                first_elem = self.board[i][0]
                for j in range(len(self.board[i])):
                    if (first_elem == 'X' and self.board[i][j] == 'X'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'X'
                            break
                    elif (first_elem == 'O' and self.board[i][j] == 'O'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'O'
                            break
                    else:
                        count = 0
            return winner
        # check columns for winner

        def check_columns():
            count = 0
            winner = None
            for i in range(len(self.board)):
                if (winner):
                    break
                first_elem = self.board[i][0]
                for j in range(len(self.board[i])):
                    if (first_elem == 'X' and self.board[j][i] == 'X'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'X'
                            break
                    elif (first_elem == 'O' and self.board[j][i] == 'O'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'O'
                            break
                    else:
                        count = 0
            return winner

        def check_diagonals():
            count = 0
            winner = None
            first_elem = self.board[0][0]
            last_elem = self.board[0][self.size - 1]
            for i in range(len(self.board)):
                if (first_elem == 'X' and self.board[i][i] == 'X'):
                    count = count + 1
                    if (count == self.size):
                        winner = 'X'
                        break
                elif (first_elem == 'O' and self.board[i][i] == 'O'):
                    count = count + 1
                    if (count == self.size):
                        winner = 'O'
                        break
                else:
                    count = 0
            if (winner):
                return winner
            else:
                for i in range(len(self.board)):
                    if (last_elem == 'X' and self.board[i][len(self.board) - 1 - i] == 'X'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'X'
                            break
                    elif (last_elem == 'O' and self.board[i][len(self.board) - 1 - i] == 'O'):
                        count = count + 1
                        if (count == self.size):
                            winner = 'O'
                            break
                    else:
                        count = 0
            return winner

        winner = check_rows()
        if (winner):
            return winner
        winner = check_columns()
        if (winner):
            return winner
        winner = check_diagonals()
        if (winner):
            return winner
        if (self.move_count == 0):
            return 'tie'
        return None
    
    def best_possible_move(self):
        print("minimax algorithm")

    def minimax(self, depth, isMax):
        if (isMax):
            score = self.best_possible_move()
        else:
            score = self.best_possible_move()

    def make_move(self):
        print("----")

    # recursively calls itself after every move
    def play(self):
        if (self.current_player == self.player):
            best_move = self.best_possible_move()
            self.make_move(best_move)
            print(best_move)
        else:
            print("Enter opponent's move")
            move = input()
            make_move(move)
        play()


print("Input the size of the game")
board_size = input()

print("Am I X or O ?")

player = input()

board = Game(board_size, player)

board.play()


# board = Game()
# winner = board.check_winner()
# print(winner)
