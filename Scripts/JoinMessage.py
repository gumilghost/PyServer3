from Core.Virtual import AbstractScript


class JoinMessage(AbstractScript):
    def on_client_connect(self, client, server):
        msg = '[SERVER] Użytkownik [{}] {} połączony'.format(client.identifier, client.name)
        server.message_to_all_without(msg, client.identifier)

        msg2 = '[SERVER] Witaj na serwerze {}\n[SERVER] Wpisz /pomoc aby wyświetlić dostepne komendy'.format(
            client.name
        )
        client.msg_push(msg2)
