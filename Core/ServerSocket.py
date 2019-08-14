from config import config
import socket


class ServerSocket:
    @staticmethod
    def create():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((config['host'], config['port']))
        sock.listen(10)

        return sock
