from headers import headers
from http_statuses import set_status
from support_routes import *
from response_model import Response
from params_reader import income_params
from errors import errors


def generate_response(environ):
    resourse = resourse_exist(environ['PATH_INFO'])
    if resourse:
        resolved_params = income_params(environ['QUERY_STRING'])
        status = set_status("ok")
        params = {'params': environ['QUERY_STRING'], 'processed': resolved_params}
        body = get_view_on(resourse, **params)
    else:
        status = set_status("not found")
        body = get_view_on('404.html', **params)
    return Response(status, headers, body)
