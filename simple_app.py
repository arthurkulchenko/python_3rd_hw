from models import *
from response import generate_response

errors = DevelopmentErrors()

def application(environ, start_response):
    response = generate_response(environ)
    start_response(response.status, response.headers)
    if len(errors.list) == 0:
        body = response.body
    else:
        body = errors.list
    return ["\n".join(body)]
