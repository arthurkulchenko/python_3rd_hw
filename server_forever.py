import socket


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']


# def handle_request(application):
#     client_connection, client_address = server_socket.accept()
#     raw_request = client_connection.recv(1024)
#     response = application(parse_request(raw_request), start_response)
#     client_connection.sendall(response)
#     client_connection.close()


# def server_forever():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('localhost', 3000))
#     server_socket.listen(1)
#     while True:
#         client_connection, client_address = server_socket.accept()
#         request = client_connection.recv(1024)
#         print(request)
#         # handle_request(application())
#         client_connection.sendall(b"HTTP/1.1 200 OK\n\nHello!")
#         client_connection.close()

# server_forever()
# def hello():
# 	return [b'Hello world from a simple WSGI application!']

