import random
import sys
import agent as dm

class Game:
    def __init__(self, n, player):
        self.size = n
        self.target = 3 if n == 3 or n == 4 else int(n / 2)
        self.player = player
        self.opponent = "O" if player == 'X' else 'X'
        self.current_player = 'X'  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        # self.board = [['X', 'X', 'O'], ['O', 'O', None], ['X', None, None]]
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

        flag = 'tie'
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == None:
                    flag = None
                    break

        if (flag == 'tie'):
            return 'tie'
        return None

    def flip_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def best_possible_move(self):
        res = self.minimax((0, 0), 0, True, -sys.maxsize, sys.maxsize)
        return res[0]

    def minimax(self, init_move, depth, isMax, alpha, beta):
        score = 0
        move = init_move
        # this works but not good
        if depth == 3:
            winner = self.check_winner()
            if winner:
                score = self.scores[winner]
                return (move, score)
            else:
                return (move, 0)
        if isMax:
            maxScore = -sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.player
                        res = self.minimax((i, j), depth+1, False, alpha, beta)
                        self.board[i][j] = None
                        if res[1] > maxScore:
                            move = (i, j)
                            maxScore = res[1]
                            alpha = max(alpha, maxScore)
                            if beta <= alpha:
                                break
            return (move, maxScore)
        else:
            minScore = sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.opponent
                        res = self.minimax((i, j), depth+1, True, alpha, beta)
                        self.board[i][j] = None
                        if (res[1] < minScore):
                            move = (i, j)
                            minScore = min(res[1], minScore)
                            beta = min(beta, minScore)
                            self.board[i][j] = None
                            if beta <= alpha:
                                break
            return (move, minScore)

    def make_move(self, move):
        print(move)
        self.board[move[0]][move[1]] = self.current_player
        # print(self.board)
    # OLD Code 
    # def play(self):
    #     if self.current_player == self.player:
    #         best_move = self.best_possible_move()
    #         self.make_move(best_move)
    #     else:
    #         print("Enter opponent's move")
    #         move = input()
    #         move = tuple(map(int, move.split(",")))
    #         self.make_move(move)
    #         # print(move)
    #     winner = self.check_winner()
    #     if winner and winner != 'tie':
    #         print(f"And the winner is {winner}")
    #         print(self.board)
    #         return
    #     elif winner == 'tie':
    #         print('It is a tie')
    #         print(self.board)
    #         return
    #     self.flip_player()
    #     self.play()

    def play(self):
        if self.current_player == self.player:
            best_move = self.best_possible_move()
            self.make_move(best_move)
            while True:
                gameMove = gameAgent.make_move(best_move, gameId)
                if gameMove['code'] == "OK":
                    print("Move ID: ", gameMove['moveId'])
                    gameAgent.get_board_string(gameId)
                    break
                else:
                    print(gameMove)
        else:
            while True:
                gameBoardMap = gameAgent.get_board_map(gameId)
                # print(gameBoardMap[-31])
                # print("\n" + gameBoardMap[-39:-36])
                if gameBoardMap[-31] == self.opponent:
                    move = gameBoardMap[-39:-36]
                    break
                # else:
                #     print(gameBoardMap)
            # print("Enter opponent's move")
            # move = input()
            move = tuple(map(int, move.split(",")))
            self.make_move(move)
            gameAgent.get_board_string(gameId)
        winner = self.check_winner()
        if winner and winner != 'tie':
            print(f"And the winner is {winner}")
            print(self.board)
            # self.display_board()
            return
        elif winner == 'tie':
            print('It is a tie')
            print(self.board)
            # self.display_board()
            return
        self.flip_player()
        self.play()


gameId = None
bSize = None
target = None
while True:
    gameAgent = dm.agent()
    print("Enter the Opponent Team ID:")
    oppoTeamId = input()
    print("Enter the board size:")
    bSize = input()
    print("Enter target:")
    target = input()
    gameIdText = gameAgent.create_game("1191", oppoTeamId, bSize, target)
    if gameIdText['code'] == "OK":
        gameId = gameIdText['gameId']
        print("Game ID: " + str(gameId))
        break
    else:
        print("Invalid Team Id")
        continue

player = "O"

board = Game(int(bSize), player)

board.play()


# print("Input the size of the game")
# board_size = int(input())

# print("Am I X or O ?")

# player = input()

# board = Game(board_size, player)

# board.play()
