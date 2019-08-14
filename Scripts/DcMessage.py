from Core.Virtual import AbstractScript


class DcMessage(AbstractScript):
    def on_client_disconnect(self, client, server):
        msg = '[SERVER] Użytkownik [{}]{} rozłączył się'.format(client.identifier, client.name)

        client.msg_push('[SERVER] Bywaj!')
        server.message_to_all_without(msg, client.identifier)
