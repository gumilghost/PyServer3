import threading
import socket
import sys

from config import config
from ScriptList import scripts
from CommandList import commands

from Core.ServerSocket import ServerSocket
from Core.Client import Client
from Core.ClientConncetion import ClientConnection
from Core.Tools import DateTools


class Server:
    _CLIENTS = []
    _SOCKET = None

    def __init__(self):
        for i in range(0, config['slots']):
            self._CLIENTS.append(None)

        try:
            self._SOCKET = ServerSocket.create()
        except Exception as e:
            print(e)
            sys.exit(0)

        for script in scripts:
            script.on_server_init(self)

        print('Nasłuchiwanie {}:{}'.format(config['host'], config['port']))

    def __del__(self):
        for script in scripts:
            script.on_server_exit(self)

        for client in self._CLIENTS:
            if client is None:
                continue

            client.disconnect()

        for i in range(0, config['slots']):
            self._CLIENTS[i] = None

        if self._SOCKET is not None:
            self._SOCKET.close()

    def _get_free_slot(self):
        for identifier, client in enumerate(self._CLIENTS):
            if client is None:
                return identifier
        else:
            raise Exception("Brak wolnych slotów")

    def remove_client(self, client):
        print('[{}] Utracono połączenie [{}]{}'.format(DateTools.get_date(), client.identifier, client.name))
        self._CLIENTS[client.identifier] = None

    def disconnect_client(self, client):
        for script in scripts:
            script.on_client_disconnect(client, self)

        msg = '[{}] Rozłączono {}:{} jako [{}]{}'.format(
            DateTools.get_date(),
            client.connection.ip,
            client.connection.port,
            client.identifier,
            client.name
        )
        print(msg)

        client.connection.close()
        self._CLIENTS[client.identifier] = None

    def message_to_all(self, message):
        for client in self._CLIENTS:
            if client is None:
                continue

            client.msg_push(message)

    def get_online_count(self):
        online = 0

        for client in self._CLIENTS:
            if client is None:
                continue

            online += 1

        return online

    def message_to_all_without(self, message, without):
        for client in self._CLIENTS:
            if client is None:
                continue

            if client.identifier == without:
                continue

            client.msg_push(message)

    def open_connection(self):
        while True:
            try:
                conn, address = self._SOCKET.accept()
                ip = address[0]
                port = address[1]

                client_identifier = self._get_free_slot()

                self._CLIENTS[client_identifier] = Client(client_identifier, ClientConnection(conn, ip, port))

                x = threading.Thread(target=self.handle_client, args=(self._CLIENTS[client_identifier], ))
                x.start()
            except Exception as e:
                print(e)
                break

    def handle_client(self, client):
        msg = '[{}] Połączono {}:{} jako [{}]{}'.format(
            DateTools.get_date(),
            client.connection.ip,
            client.connection.port,
            client.identifier,
            client.name
        )
        print(msg)

        for script in scripts:
            script.on_client_connect(client, self)

        while True:
            try:
                response = client.connection.reciv_data()

                if response is None:
                    self.remove_client(client)
                    break

                if response == '':
                    continue

                if response[0] == '/':
                    result = False

                    for command in commands:
                        if '/' + command.trigger == response:
                            result = command.execute(client, self, [])
                            break
                    else:
                        client.msg_push('[SERVER] Nieznana komenda')

                    if result is True:
                        break
                else:
                    for script in scripts:
                        script.on_client_text(client, self, response)
            except Exception as e:
                # self.disconnect_client(client)
                # print('[{}] Rozłączono {} ({})'.format(DateTools.get_date(), client.identifier, e))
                print('[{}] Błąd: {}'.format(DateTools.get_date(), e))
                break
