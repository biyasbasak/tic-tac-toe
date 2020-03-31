import random
import sys
import agent as dm


class Game:
    def __init__(self, n, player):
        self.size = n
        self.player = player
        self.opponent = "O" if player == "X" else "X"
        self.current_player = "O"  # initial player is X
        self.board = [[None for x in range(n)] for x in range(n)]
        self.move_count = n * n
        self.scores = {
            "X": 10,
            "O": -10,
            "tie": 0
        }
        self.alpha = -sys.maxsize
        self.beta = sys.maxsize

    def scoreSelection(self):
        if self.player == "O":
            self.scores = {
                "X": -10,
                "O": 10,
                "tie": 0
            }

    def check_winner(self):
        # check rows for winner
        def check_rows():
            winner = None
            for i in range(len(self.board)):
                count = 0
                if (winner):
                    break
                first_elem = self.board[i][0]
                for j in range(len(self.board[i])):
                    if first_elem == 'X' and self.board[i][j] == 'X':
                        count = count + 1
                        if count == self.size:
                            winner = 'X'
                            break
                    elif first_elem == 'O' and self.board[i][j] == 'O':
                        count = count + 1
                        if count == self.size:
                            winner = 'O'
                            break
                    else:
                        count = 0
            return winner
        # check columns for winner

        def check_columns():
            winner = None
            for i in range(len(self.board)):
                count = 0
                if winner:
                    break
                first_elem = self.board[0][i]
                for j in range(len(self.board[i])):
                    if first_elem == 'X' and self.board[j][i] == 'X':
                        count = count + 1
                        if count == self.size:
                            winner = 'X'
                            break
                    elif first_elem == 'O' and self.board[j][i] == 'O':
                        count = count + 1
                        if count == self.size:
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
                if first_elem == 'X' and self.board[i][i] == 'X':
                    count = count + 1
                    if count == self.size:
                        winner = 'X'
                        break
                elif first_elem == 'O' and self.board[i][i] == 'O':
                    count = count + 1
                    if count == self.size:
                        winner = 'O'
                        break
                else:
                    count = 0
            if winner:
                return winner
            else:
                count = 0
                for i in range(len(self.board)):
                    if last_elem == 'X' and self.board[i][len(self.board) - 1 - i] == 'X':
                        count = count + 1
                        if count == self.size:
                            winner = 'X'
                            break
                    elif last_elem == 'O' and self.board[i][len(self.board) - 1 - i] == 'O':
                        count = count + 1
                        if count == self.size:
                            winner = 'O'
                            break
                    else:
                        count = 0
            return winner

        winner = check_rows()
        if winner:
            return winner
        winner = check_columns()
        if winner:
            return winner
        winner = check_diagonals()
        if winner:
            return winner
        flag = 'tie'
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
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
        if winner:
            scoreW = self.scores[winner]
            return scoreW
        if isMax:
            maxScore = -sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.player
                        score = self.minimax(depth + 1, False)
                        maxScore = max(score, maxScore)
                        self.board[i][j] = None
                        if self.beta > maxScore:
                            self.alpha = max(self.alpha, maxScore)
                            return maxScore
                        # if maxScore >= self.beta:
                        #     return maxScore
                        # if self.alpha >= self.beta:
                        #     break
                        # if maxScore > self.alpha:
                        #     self.alpha = maxScore

            return maxScore
        else:
            minScore = sys.maxsize
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.opponent
                        score = self.minimax(depth + 1, True)
                        minScore = min(score, minScore)
                        self.board[i][j] = None
                        if self.alpha < minScore:
                            self.beta = min(self.beta, minScore)
                            return minScore
                        # if minScore <= self.alpha:
                        #     return minScore
                        # if self.beta <= self.alpha:
                        #     break
                        # if minScore < self.beta:
                        #     self.beta = minScore

            return minScore

    def make_move(self, move):
        # if self.board[int(move[0])][int(move[1])] is None:
        print(move)
        self.board[int(move[0])][int(move[1])] = self.current_player
        self.move_count = self.move_count - 1
        # else:
        #     print("Invalid Move")
    # recursively calls itself after every move

    def play(self):
        self.scoreSelection()
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
            move = tuple(move.split(","))
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

    def display_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
            print()


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
