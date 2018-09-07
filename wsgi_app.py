from response import generate_response

def application(environ, start_response):
    response = generate_response(environ)
    start_response(response.status, response.headers)
    return response.body
