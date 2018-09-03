from response import generate_response
from errors import errors
from jinja2 import Environment, PackageLoader, select_autoescape
# from routes        import route_does_exist
# from http_statuses import set_status
# from support import *

env = Environment(
    loader=PackageLoader('init', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


# def get_view_on(file, *args):
#     # return codecs.open(templates_folder() + path_matcher(file) + ".html", 'r')
#     file = templates_folder() + path_matcher(file) + ".html"
#     template = env.get_template(file)
#     return template.render(args)

# def generate_response(environ):
#     if route_does_exist(environ['PATH_INFO']): 
#         # result = main_programm_exec(environ)
#         status = set_status("ok")
#         body = get_view_on(environ['PATH_INFO'], the='variables', go='here')
#     else:
#         status = set_status("not found")
#         body = get_view_on('404')
#     return Response(status, headers, body)


def application(environ, start_response):
    response = generate_response(environ, env)
    start_response(response.status, response.headers)
    # -------------------------------------------------
    if len(errors.list) is not 0:
        response.body = ["%s" % errors.list]
    # -------------------------------------------------
    return response.body
    # return ["\n".join(environ)]
    # return ["/b %s" % environ['wsgi.file_wrapper']]
