from headers import headers
from http_statuses import set_status
from routes import route_does_exist
from models import Response

def generate_response(environ):
    if route_does_exist(environ['PATH_INFO']): 
        # result = main_programm_exec(environ)
        current_path = environ['PATH_INFO']
        status = set_status("ok")
        body = ['Hello']
    else:
    	status = set_status("not found")
    	body = ['pitty']
    return Response(status, headers, body)
