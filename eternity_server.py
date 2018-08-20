import socket
from request_handler import *

def server_forever():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 3000))
    server_socket.listen(1)
    while True:
        client_connection, client_address = server_socket.accept()
        request = client_connection.recv(1024)
        print request
        print '---------------------------'
        response = handle_request(request)
        print response
        print '---------------------------'
        # client_connection.sendall("response")
        client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
        client_connection.close()


server_forever()
