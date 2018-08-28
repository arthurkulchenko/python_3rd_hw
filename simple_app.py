def application(environ, start_response):
    lines = ["%s: %r" % (key, value) for key, value in environ.items()]
    if environ['PATH_INFO'] == '/':
    	result = "1"
    else:
    	result = "2"
    start_response("200 OK", [("Content-Type", "text/plain")])
    return ["\n".join([result])]
