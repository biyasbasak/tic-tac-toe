import requests


class agent:
    def __init__(self):
        self.board = []
        self.termination = False
        self.state = ''
        self.baseURL = "http://www.notexponential.com/aip2pgaming/api/index.php"

    def get_board_string(self, gameId):
        headers = {
            'x-api-key': '21be1b176c5d8c7bc09c',
            'userid': '843',
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "boardString",
            "gameId": gameId
        }
        response = requests.get(self.baseURL, params=payload, headers=headers)
        r = response.json()
        print(r["output"])

    def get_board_map(self, gameId):
        headers = {
            "x-api-key": "21be1b176c5d8c7bc09c",
            "userid": "843",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "boardMap",
            "gameId": gameId
        }
        response = requests.get(self.baseURL, params=payload, headers=headers)
        # print(response.text)
        return response.text

    def get_moves(self, gameId, move_count):
        # useless
        headers = {
            "x-api-key": "21be1b176c5d8c7bc09c",
            "userid": "843",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "moves",
            "gameId": gameId,
            "count": move_count
        }
        response = requests.get(self.baseURL, params=payload, headers=headers)
        print(response.text)

    def get_games(self):
        headers = {
            "x-api-key": "21be1b176c5d8c7bc09c",
            "userid": "843",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "myGames"
        }
        response = requests.get(self.baseURL, params=payload, headers=headers)
        print(response.text)

    def make_move(self, move, gameID):
        headers = {
            "x-api-key": "90da155fac97298ba06a",
            "userId": "837",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "teamId": "1191",
            "move": str(move[0]) + ',' + str(move[1]),
            "type": "move",
            "gameId": gameID
        }
        response = requests.post(self.baseURL, headers=headers, data=payload)
        # print(response.text)
        return response.json()

    def create_game(self, teamId1, teamId2, boardSize, target):
        headers = {
            "x-api-key": "90da155fac97298ba06a",
            "userId": "837",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "game",
            "teamId1": teamId1,
            "teamId2": teamId2,
            "gameType": "TTT",
            "boardSize": boardSize,
            "target": target
        }
        response = requests.post(self.baseURL, headers=headers, data=payload)
        return response.json()
        # print(response.text)
        # split = response.text.split('"')
        # gameID = int(split[-1][1:-3])
        # return gameID


# def test():
#     closeAI = agent()
#     # opponent = 1191
#     # new_game = closeAI.create_game(1191, opponent)
#     game = 196
#     closeAI.get_games()
#     closeAI.get_board_string(game)
#     closeAI.get_board_map(game)
#     closeAI.make_move((6, 8), game)
#     closeAI.get_moves(game, 20)

