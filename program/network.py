import socket
import requests

from system import handle_error


class Client:
    def __init__(self):
        self.SERVER_IP = "localhost"
        self.SERVER_IP = "94.250.249.251"
        self.SERVER_PORT = 9080
        self.sock = socket.socket()

    def send_data(self, message):
        try:
            self.sock.connect((self.SERVER_IP, self.SERVER_PORT))
            self.sock.send(b"Request by JediKnight")
            print("con", self.sock.recv(1024))
            self.sock.send(message)
            data = self.sock.recv(1024)
            return 1, data
        except Exception as err:
            handle_error(err)
            return 0, b""
        finally:
            self.sock.close()

    def receive_server_data(self):
        response = requests.get("https://drive.google.com/uc" \
                                "?id=1LOK5K5Y3NmhWATjk7qu1vGh1dk2rDOZC&authuser=0&export=download",
                                allow_redirects=True)
        if response:
            return response.json()
        else:
            return 0

    def alert_patch(self):
        success, rec_data = self.send_data(b"patch")
        print(success, rec_data)
        if not rec_data or not success:  # No connection
            return 0
        if rec_data == b'Considered':
            return 1
        else:  # Already sent
            return -1

    def send_key(self, key):
        message = b"key " + key.encode("utf-8")
        success, rec_data = self.send_data(message)
        if not success:
            return 0
        if rec_data == b"Correct":
            return 1
        elif rec_data == b"Too many requests":
            return -2
        else:  # Not correct key
            return -1


if __name__ == '__main__':
    s = Client()
    print(s.receive_server_data())
