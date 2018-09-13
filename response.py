from headers import headers
from http_statuses import set_status
from support_routes import route_does_exist
from response_model import Response
from view import get_view_on
from params_reader import income_params

def generate_response(environ):
    if route_does_exist(environ['PATH_INFO']): 
        resolved_params = income_params(environ['QUERY_STRING'])
        status = set_status("ok")
        params = {'params': environ['QUERY_STRING'], 'go': resolved_params}
        body = get_view_on(environ['PATH_INFO'], **params)
    else:
        status = set_status("not found")
        body = get_view_on('/404')
    return Response(status, headers, body)
