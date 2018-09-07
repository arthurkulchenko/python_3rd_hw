from view            import get_view_on
from routes          import *
from models          import Response
from headers         import headers
from http_statuses   import set_status

def generate_response(environ, env):
    if route_does_exist(environ['PATH_INFO']):
    	if needs_redirection(environ['PATH_INFO']):
    		status = set_status('moved permanentley')
    	else:
            # result = main_programm_exec(environ)
            status = set_status('ok')
            body = get_view_on(environ['PATH_INFO'], 'it is', 'working')
    else:
        status = set_status('not found')
        body = get_view_on('404')
    return Response(status, headers, body)
