from response import generate_response
from errors import errors

def application(environ, start_response):
    response = generate_response(environ)
    start_response(response.status, response.headers)
    # -------------------------------------------------
    if len(errors.list) is not 0:
        response.body = ["%s" % errors.list]
    # -------------------------------------------------
    return response.body
    # return ["\n".join(response.body)]
