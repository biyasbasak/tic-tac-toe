import random
import sys


class Game:
    def __init__(self, n, player):
        self.size = n
        self.target = int(n / 2)
        self.player = 'X' if player == 'X' else 'O'
        self.opponent = 'O' if player == 'X' else 'X'
        self.current_player = 'X'  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        self.move_count = n ** n
        self.scores = {
            "X": 10,
            "O": -10,
            "Draw": 0
        }
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize

    def score_selection(self):
        if self.player == 'O':
            self.scores = {
                "X": -10,
                "O": 10,
                "Draw": 0
            }

    def check_winner(self):
        def valid(x, y):
            return 0 <= x < self.size and 0 <= y < self.size

        def check_rows():
            winner = None
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j]:
                        first_elem = self.board[i][j]
                        count = 0
                        for k in range(self.target):
                            if valid(i, j + k):
                                if self.board[i][j + k] != first_elem:
                                    break
                                else:
                                    count += 1
                            else:
                                break
                        if count >= self.target:
                            winner = first_elem
                            return winner
            return winner

        def check_columns():
            winner = None
            for j in range(self.size):
                for i in range(self.size):
                    if self.board[i][j]:
                        first_elem = self.board[i][j]
                        count = 0
                        for k in range(self.target):
                            if valid(i + k, j):
                                if self.board[i + k][j] != first_elem:
                                    break
                                else:
                                    count += 1
                            else:
                                break
                        if count >= self.target:
                            winner = first_elem
                            return winner
            return winner

        def check_diagonal_a():
            winner = None
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j]:
                        first_elem = self.board[i][j]
                        count = 0
                        for k in range(self.target):
                            if valid(i + k, j + k):
                                if self.board[i + k][j + k] != first_elem:
                                    break
                                else:
                                    count += 1
                            else:
                                break
                        if count >= self.target:
                            winner = first_elem
                            return winner
            return winner

        def check_diagonal_b():
            winner = None
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j]:
                        first_elem = self.board[i][j]
                        count = 0
                        for k in range(self.target):
                            if valid(i + k, j - k):
                                if self.board[i + k][j - k] != first_elem:
                                    break
                                else:
                                    count += 1
                            else:
                                break
                        if count >= self.target:
                            winner = first_elem
                            return winner
            return winner

        winner = check_columns() or check_rows() or check_diagonal_a() or check_diagonal_b()
        if winner:
            return winner

        flag = 'Draw'
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    flag = None
                    break
        return flag

    def flip_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def best_possible_move(self):
        print("Computing best move for {}...".format(self.current_player))
        best_score = -sys.maxsize
        best_move = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    self.board[i][j] = self.current_player
                    score = self.minimax(0, False)
                    if score > best_score:
                        best_move = (i, j)
                        best_score = score
                    self.board[i][j] = None
        return best_move

    def minimax(self, depth, isMax):
        winner = self.check_winner()
        score = 0
        if winner:
            score = self.scores[winner]
            return score
        if isMax:
            maxScore = -sys.maxsize
            if score < self.alpha:
                return self.alpha
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.player
                        score = self.minimax(depth+1, False)
                        maxScore = max(score, maxScore)
                        self.board[i][j] = None
            self.alpha = max(maxScore, self.alpha)
            return maxScore
        else:
            minScore = sys.maxsize
            if self.beta < score:
                return self.beta
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.opponent
                        score = self.minimax(depth+1, True)
                        minScore = min(score, minScore)
                        self.board[i][j] = None
            self.beta = max(minScore, self.beta)
            return minScore

    def make_move(self, move):
        print(move)
        self.board[int(move[0])][int(move[1])] = self.current_player
        self.move_count = self.move_count - 1
    # recursively calls itself after every move

    def play(self):
        self.score_selection()
        if self.current_player == self.player:
            best_move = self.best_possible_move()
            self.make_move(best_move)
        else:
            print("Enter opponent's move")
            move = input()
            move = tuple(move.split(","))
            self.make_move(move)
        winner = self.check_winner()
        if winner and winner != 'Draw':
            print("And the winner is {}".format(winner))
            self.display_board()
            return
        elif winner == 'Draw':
            print('Draw')
            self.display_board()
            return
        self.flip_player()
        self.play()

    def display_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    print(self.board[i][j], end=' ')
                else:
                    print('-', end=' ')
            print()


print("Input the size of the game:")
board_size = int(input())

print("Am I X or O ?")

player = input()

board = Game(board_size, player)

board.play()