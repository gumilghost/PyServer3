class AbstractCommand:
    trigger = ''

    def execute(self, client, server, args):
        pass


class AbstractScript:
    def on_server_init(self, server):
        pass

    def on_server_exit(self, server):
        pass

    def on_client_disconnect(self, client, server):
        pass

    def on_client_connect(self, client, server):
        pass

    def on_client_text(self, client, server, message):
        pass
