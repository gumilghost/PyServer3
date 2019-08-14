class Client:
    identifier = 0
    name = 'User'
    connection = None

    def __init__(self, identifier, conn):
        self.identifier = identifier
        self.connection = conn

    def msg_push(self, message):
        self.connection.send("{}\n".format(message).encode())

    def disconnect(self):
        self.connection.close()
