import random
import sys
import agent as dm


class Game:
    def __init__(self, n, player, t):
        self.size = n
        self.target = int(t)
        self.player = player
        self.opponent = "O" if player == 'X' else 'X'
        self.current_player = 'O'  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        # self.board = [['X', 'X', 'O'], ['O', 'O', None], ['X', None, None]]
        self.scores = {
            "X": 10000000,
            "O": -10000000,
            "tie": 0
        } if player == 'X' else {
            "X": -10000000,
            "O": 10000000,
            "tie": 0
        }
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize
        self.move_counter = 0
        self.best_move = (0, 0)

    def calculate(self, line):
        total = 0
        score = 1
        first = '-'
        for i in range(len(line)):
            if line[i] == '-':
                if first == 'X':
                    total += score
                elif first == 'O':
                    total -= score
                score = 1
                first = line[i]
            else:
                if first == '-':
                    first = line[i]
                elif first == line[i]:
                    score *= 10
                else:
                    if first == 'X':
                        total += score
                    elif first == 'O':
                        total -= score
                    score = 1
                    first = line[i]
        if first == 'X':
            total += score
        elif first == 'O':
            total -= score
        return total

    def evaluate(self, move, current_player):
        x = move[0]
        y = move[1]
        row = []
        col = []
        d1 = []
        d2 = []
        for i in range(self.size):
            row.append(self.board[x][i])
            col.append(self.board[i][y])
            if 0 <= y - x + i < self.size:
                d1.append(self.board[i][y - x + i])
            if 0 <= x + y - i < self.size:
                d2.append(self.board[i][x + y - i])
        row_score = self.calculate(row)
        col_score = self.calculate(col)
        d1_score = self.calculate(d1)
        d2_score = self.calculate(d2)
        total_score = row_score + col_score + d1_score + d2_score
        if current_player == 'O':
            total_score = -total_score
        return total_score

    def evaluation(self, current_player):
        total_score = 0
        for i in range(self.size):
            for j in range(self.size):
                total_score += self.evaluate((i, j), current_player)
        return total_score

    def valid(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def check_winner(self):

        def check_rows():
            winner = None
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j]:
                        first_elem = self.board[i][j]
                        count = 0
                        for k in range(self.target):
                            if self.valid(i, j + k):
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
                            if self.valid(i + k, j):
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
                            if self.valid(i + k, j + k):
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
                            if self.valid(i + k, j - k):
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
        if winner and winner != '-':
            return winner

        flag = 'tie'
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    flag = None
                    break

        if flag == 'tie':
            return 'tie'
        return None

    def flip_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def best_possible_move(self):
        res = self.minimax(0, True, -sys.maxsize, sys.maxsize)
        return self.best_move

    def impossible(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.valid(x + i, y + j) and self.board[x+i][y+j] is not None:
                    return False
        return True

    def minimax(self, depth, isMax, alpha, beta):
        score = 0
        # this works but not good
        if depth == 3:
            winner = self.check_winner()
            if winner:
                score = self.scores[winner]
                return score
            else:
                if isMax:
                    return self.evaluation('X')
                else:
                    return self.evaluation('O')
        else:
            winner = self.check_winner()
            # print(f"called{winner}")
            if winner:
                score = self.scores[winner]
                return score
        if isMax:
            maxScore = -sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        if self.impossible(i, j):
                            continue
                        self.board[i][j] = self.player
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = None
                        if score > maxScore:
                            if depth == 0:
                                self.best_move = (i, j)
                            maxScore = max(score, maxScore)
                            alpha = max(alpha, maxScore)
                            if beta <= alpha:
                                break
            return maxScore
        else:
            minScore = sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        if self.impossible(i, j):
                            continue
                        self.board[i][j] = self.opponent
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = None
                        if score < minScore:
                            if depth == 0:
                                self.best_move = (i, j)
                            minScore = min(score, minScore)
                            beta = min(beta, minScore)
                            if beta <= alpha:
                                break
            return minScore

    # def minimax2(self, depth, isMax, alpha, beta):
    #     best_score = -sys.maxsize if isMax is True else sys.maxsize
    #     move = (-1, -1)
    #     depth_evaluator = 3 if self.move_counter < 120 else 4
    #     depth_evaluator = 6 if self.move_counter > 130 else depth_evaluator
    #     # this works but not good
    #     if depth == depth_evaluator:
    #         winner = self.check_winner()
    #         # print(f"called{winner}")
    #         if winner:
    #             score = self.scores[winner]
    #             return (move, score)
    #         else:
    #             return (move, 0)
    #     else:
    #         winner = self.check_winner()
    #         # print(f"called{winner}")
    #         if winner:
    #             score = self.scores[winner]
    #             return (move, score)

    #     for i in range(len(self.board)):
    #         for j in range(len(self.board[i])):
    #             if self.board[i][j] is None:
    #                 self.board[i][j] = self.player if isMax is True else self.opponent
    #                 if isMax:
    #                     res = self.minimax2(depth + 1, False, alpha, beta)
    #                     if res[1] > best_score:
    #                         move = (i, j)
    #                         best_score = res[1] - depth * 10
    #                         alpha = max(alpha, best_score)
    #                         self.board[i][j] = None
    #                         if beta <= alpha:
    #                             break
    #                 else:
    #                     res = self.minimax2(depth + 1, True, alpha, beta)
    #                     if (res[1] < best_score):
    #                         move = (i, j)
    #                         best_score = res[1] + depth * 10
    #                         beta = min(beta, best_score)
    #                         self.board[i][j] = None
    #                         if beta <= alpha:
    #                             break

    #                 self.board[i][j] = None

        # return (move, best_score)

    def make_move(self, move):
        self.board[move[0]][move[1]] = self.current_player
        self.move_counter += 1
        print(move)
        # for line in self.board:
        #     print(line)
        # print(self.board)

    # # OLD Code
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

board = Game(int(bSize), player, target)

board.play()


# print("Input the size of the game")
# board_size = int(input())

# print("Input the target size")
# target = int(input())

# print("Am I X or O ?")

# player = input()

# board = Game(board_size, player, target)

# board.play()