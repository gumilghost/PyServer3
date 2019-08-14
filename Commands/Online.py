from Core.Virtual import AbstractCommand
from config import config


class Online(AbstractCommand):
    trigger = 'online'

    def execute(self, client, server, args):
        online = server.get_online_count()
        client.msg_push('[SERVER] {}/{}'.format(online, config['slots']))
