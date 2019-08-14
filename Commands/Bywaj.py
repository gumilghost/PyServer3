from Core.Virtual import AbstractCommand


class Bywaj(AbstractCommand):
    trigger = 'bywaj'

    def execute(self, client, server, args):
        server.disconnect_client(client)

        return True
