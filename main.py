import random
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)

class Game:
    def __init__(self, n, player):
        self.size = n
        self.target = int(n / 2)
        self.player = player
        self.opponent = "O" if player == 'X' else 'X'
        self.current_player = 'X'  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        self.scores = {
            "X": 10,
            "O": -10,
            "tie": 0
        } if player == 'X' else {
            "X": -10,
            "O": 10,
            "tie": 0
        }
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize

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

<<<<<<< HEAD
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
=======
        winner = check_rows() or check_columns() or check_diagonals()
>>>>>>> first iteration of alpha beta pruning
        if winner:
            return winner

        flag = 'tie'
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    flag = None
                    break
<<<<<<< HEAD
        return flag   # check rows for winner
=======
        if (flag == 'tie'):
            return 'tie'
        return None

    def flip_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def best_possible_move(self):
        best_score = -sys.maxsize
        best_move = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    self.board[i][j] = self.current_player
                    score = self.minimax(0, False, -sys.maxsize, sys.maxsize)
                    print(score)
                    if score > best_score:
                        best_move = (i, j)
                        best_score = score
                    self.board[i][j] = None
        return best_move

    def minimax(self, depth, isMax, alpha, beta):
        score = 0
        print(depth)
        if depth == self.size:
            winner = self.check_winner()
            if winner:
                score = self.scores[winner]
                return score
            else:
                return 0
        if isMax:
            maxScore = -sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.player
                        score = self.minimax(depth+1, False, alpha, beta)
                        maxScore = max(score, maxScore)
                        alpha = max(alpha, maxScore)
                        self.board[i][j] = None
                        if beta <= alpha:
                            break
            return maxScore
        else:
            minScore = sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.opponent
                        score = self.minimax(depth+1, True, alpha, beta)
                        minScore = min(score, minScore)
                        beta = min(beta, minScore)
                        self.board[i][j] = None
                        if beta <= alpha:
                            break
            return minScore
>>>>>>> first iteration of alpha beta pruning

    def make_move(self, move):
        print(move)
        self.board[move[0]][move[1]] = self.current_player
        print(self.board)
    # recursively calls itself after every move

    def play(self):
        if self.current_player == self.player:
            best_move = self.best_possible_move()
            self.make_move(best_move)
        else:
            print("Enter opponent's move")
            move = input()
            move = tuple(map(int, move.split(",")))
            self.make_move(move)
            # print(move)
        winner = self.check_winner()
        if winner and winner != 'tie':
            print(f"And the winner is {winner}")
            print(self.board)
            return
        elif winner == 'tie':
            print('It is a tie')
            print(self.board)
            return
        self.flip_player()
        self.play()

    def display_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()


print("Input the size of the game")
board_size = int(input())

print("Am I X or O ?")

player = input()

board = Game(board_size, player)

board.play()
