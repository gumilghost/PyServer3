from Core.Virtual import AbstractScript


class Chat(AbstractScript):
    def on_client_text(self, client, server, message):
        server.message_to_all('[{}]{}: {}'.format(client.identifier, client.name, message))
