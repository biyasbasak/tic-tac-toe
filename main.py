import random
import sys


class Game:
    def __init__(self, n, player):
        self.size = n
        self.player = player
        self.opponent = "O" if player == 'X' else 'X'
        self.current_player = 'X'  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        self.move_count = n ** n
        self.scores = {
            "X": 10,
            "O": -10,
            "tie": 0
        }

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

    def flip_player(self):
        if (self.current_player == 'X'):
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def best_possible_move(self):
        print("minimax algorithm")
        best_score = -sys.maxsize
        best_move = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if (self.board[i][j] == None):
                    self.board[i][j] = self.current_player
                    score = self.minimax(0, True)
                    if (score > best_score):
                        best_move = (i, j)
                    self.board[i][j] = None
        return best_move

    def minimax(self, depth, isMax):
        winner = self.check_winner()
        score = 0
        if (winner):
            score = self.scores[winner]
            return score
        if (isMax):
            maxScore = -sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (self.board[i][j] == None):
                        self.board[i][j] = self.player
                        score = self.minimax(depth+1, False)
                        maxScore = max(score, maxScore)
                        self.board[i][j] = None
            return maxScore
        else:
            minScore = sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if (self.board[i][j] == None):
                        self.board[i][j] = self.opponent
                        score = self.minimax(depth+1, True)
                        minScore = min(score, minScore)
                        self.board[i][j] = None
            return minScore

    def make_move(self, move):
        print(move)
        self.board[int(move[0])][int(move[1])] = self.current_player
        self.move_count = self.move_count - 1
    # recursively calls itself after every move

    def play(self):
        winner = self.check_winner()
        if (winner):
            print(f"And the winner is {winner}")
            print(self.board)
            return
        if (self.current_player == self.player):
            best_move = self.best_possible_move()
            self.make_move(best_move)
            # print(best_move)
        else:
            print("Enter opponent's move")
            move = input()
            move = tuple(move.split(","))
            self.make_move(move)
            # print(move)
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

