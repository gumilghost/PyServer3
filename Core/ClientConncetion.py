from Core.Tools import DateTools


class ClientConnection:
    _CONNECTION = None
    alive = True
    ip = ''
    port = 1234

    def __init__(self, conn, ip, port):
        self._CONNECTION = conn
        self.ip = ip
        self.port = port

    def reciv_data(self):
        try:
            data = self._CONNECTION.recv(1024)
        except Exception as e:
            self.alive = False
            print('[{}] Błąd pakietu: {}'.format(DateTools.get_date(), e))
            return None

        if not data:
            return None

        return data.decode("utf-8").replace("\r", "").replace("\n", "")

    def send(self, msg):
        self._CONNECTION.send(msg)

    def close(self):
        if self.alive is True:
            self._CONNECTION.close()

        self.alive = False
