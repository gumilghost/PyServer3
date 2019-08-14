from Core.Virtual import AbstractCommand


class Id(AbstractCommand):
    trigger = 'id'

    def execute(self, client, server, args):
        msg = '[SERVER] Twoje ID: {}'.format(client.identifier)
        client.msg_push(msg)
