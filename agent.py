import http.client
import mimetypes


class agent:
    def __init__(self):
        self.board = []
        self.termination = False
        self.state = ''

    def get_board_string(self, gameId):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
            'x-api-key': '21be1b176c5d8c7bc09c',
            'userid': '843',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=boardString&gameId={}".format(gameId), payload, headers)
        res = conn.getresponse()
        data = res.read()
        decoded_data = data.decode("utf-8")
        print(decoded_data)
        splitted_data = decoded_data.split('"')
        board_string = splitted_data[3]
        self.board = board_string.split('\\n')[:-1]
        print(self.board)
        self.state = splitted_data[-2]
        print(self.state)

    def get_board_map(self, gameId):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
            'x-api-key': '21be1b176c5d8c7bc09c',
            'userid': '843',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=boardMap&gameId={}".format(gameId), payload, headers)
        res = conn.getresponse()
        data = res.read()
        decoded_data = data.decode("utf-8")
        print(decoded_data)
        splitted_data = decoded_data.split('"')
        self.state = splitted_data[-2]
        print(self.state)

    def get_moves(self, gameId, move_count):
        conn = http.client.HTTPSConnection("www.notexponential.com")
        boundary = ''
        payload = ''
        headers = {
            'x-api-key': '21be1b176c5d8c7bc09c',
            'userid': '843',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("GET", "/aip2pgaming/api/index.php?type=moves&gameId=87&count=20", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


    def make_move(self, move):
        # unsolved problem: {"code":"FAIL","message":"No POST supported for action type: "}
        conn = http.client.HTTPSConnection("www.notexponential.com")
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=teamId;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("1191")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=move;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("6,8")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=type;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("move")
        dataList.append('--' + boundary)
        dataList.append('Content-Disposition: form-data; name=gameId;')

        dataList.append('Content-Type: {}'.format('multipart/form-data'))
        dataList.append('')

        dataList.append("87")
        dataList.append('--' + boundary + '--')
        dataList.append('')
        body = '\r\n'.join(dataList)
        payload = body
        headers = {
            'x-api-key': '21be1b176c5d8c7bc09c',
            'userid': '843',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


def test():
    closeAI = agent()
    closeAI.get_board_string(87)
    closeAI.get_board_map(87)
    closeAI.get_moves(87, 20)
    closeAI.make_move((6,8))


test()
