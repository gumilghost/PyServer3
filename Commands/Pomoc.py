from Core.Virtual import AbstractCommand


class Pomoc(AbstractCommand):
    trigger = 'pomoc'

    def execute(self, client, server, args):
        desc = [
            '[SERVER] Dostępne komendy:\n',
            '[SERVER] /bywaj - rozłącza z serwerem\n',
            '[SERVER] /id - wyświetla twoje id\n',
            '[SERVER] /online - wyświetla ilość użytkowników online',
        ]
        client.msg_push(''.join(desc))
