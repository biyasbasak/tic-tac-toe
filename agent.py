import requests


class agent:
    def __init__(self):
        self.board = []
        self.termination = False
        self.state = ''
        self.baseURL = "http://www.notexponential.com/aip2pgaming/api/index.php"

    def create_a_game(self, teamId1, teamId2):
        payload={
            "teamId1": teamId1,
            "teamId2": teamId2,
            "type": "game",
            "gameType": "TTT"
        }
        headers ={
            "x-api-key": "21be1b176c5d8c7bc09c",
            "userid": "843",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        response = requests.post(self.baseURL, headers=headers, data=payload)
        print(response.text)

    def get_board_string(self, gameId):
        headers = {
            "x-api-key": "21be1b176c5d8c7bc09c",
            "userid": "843",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "type": "boardString",
            "gameId": gameId
        }
        response = requests.get(self.baseURL, params=payload, headers=headers)
        print(response.text)

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
        print(response.text)

    def get_moves(self, gameId, move_count):
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

    def make_move(self, move,gameID):
        headers = {
            "x-api-key": "90da155fac97298ba06a",
            "userId": "837",
            "User-Agent": "Mozilla / 5.0(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        payload = {
            "teamId": "1191",
            "move": "0,0",
            "type": "move",
            "gameId": gameID
        }
        response = requests.post(self.baseURL, headers=headers, data=payload)
        print(response.text)

# def test():
#     closeAI = agent()
#     closeAI.get_board_string(87)
#     closeAI.get_board_map(87)
#     closeAI.get_moves(87, 20)
#     closeAI.make_move({6, 8},95)
# test()
