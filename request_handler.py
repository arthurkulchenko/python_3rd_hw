# import requests
from request_parser import parse

def handle_request(request):
	return parse(request)
    # client_connection, client_address = server_socket.accept()
    # raw_request = client_connection.recv(1024)
    # response = application(parse_request(raw_request), start_response)
    # client_connection.sendall(response)
    # client_connection.close()
