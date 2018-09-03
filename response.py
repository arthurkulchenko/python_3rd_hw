from view          import get_view_on
from routes        import route_does_exist
from models        import Response
from headers       import headers
from http_statuses import set_status

def generate_response(environ, env):
    if route_does_exist(environ['PATH_INFO']): 
        # result = main_programm_exec(environ)
        status = set_status('ok')
        body = get_view_on(environ['PATH_INFO'], 'variables', 'here')
    else:
        status = set_status('not found')
        body = get_view_on('404')
    return Response(status, headers, body)
