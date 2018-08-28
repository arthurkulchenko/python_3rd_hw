# import socket
# from request_parser import parse

def application(environ, start_response):
	# body = b'Hello world!\n'
 #    status = '200 OK'
 #    headers = [('Content-type', 'text/plain')]
 #    start_response(status, headers)
 #    return [body]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello world from a simple WSGI application!']


# def server_forever():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('localhost', 3000))
#     server_socket.listen(1)
#     while True:
#         client_connection, client_address = server_socket.accept()
#         request = client_connection.recv(1024)
#         response = application(environ, start_response)
#         client_connection.sendall(response)
#         # client_connection.sendall(b"HTTP/1.1 200 OK\n\n %s" % parse(request))
#         client_connection.close()


# server_forever()
