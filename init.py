from errors import errors
from response import generate_response
from template_engine import env


def application(environ, start_response):
    response = generate_response(environ, env)
    start_response(response.status, response.headers)
    # -------------------------------------------------
    if len(errors.list) is not 0:
        response.body = errors.list
    # -------------------------------------------------
    return ["%s" % response.body]
