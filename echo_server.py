import websockify.autobind

import asyncio


class EchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('connection from {}'.format(peername))
        self.transport = transport
        #data = open('/srv/www/html/terms/miedit-master/dump','rb').read()
        data = b"3613 PYTHON37"
        self.transport.write(data  )

    def data_received(self, data):
        print('data received: {}'.format(data.decode()))
        self.transport.write(data)

        # close the socket
        self.transport.close()

loop = asyncio.get_event_loop()
coro = loop.create_server(EchoServer, '127.0.0.1', 20080)
server = loop.run_until_complete(coro)
print('serving on {}'.format(server.sockets[0].getsockname()))

try:
    loop.run_forever()
except KeyboardInterrupt:
    print("exit")
finally:
    server.close()
    loop.close()
