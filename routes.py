import os
import re
from support import *
from errors import errors

routes = [
    ('/', 'index'),
    ('/index', 'index'),
    ('/about', 'about')
]


def path_matcher(path):
	if path == '/':
	    return '/index'
	else:
	    return path


def route_does_exist(route, routes=routes):
    return [True for r in routes if (route == r[0] and template_does_exist(route))]


def template_does_exist(path):
    requested = templates_folder() + path_matcher(path)
    file_path = re.split("['.'][\D]+", requested)[0] + '.html'
    if os.access(file_path, os.F_OK) is True:
        return True
    else:
        errors.list.append("Template not found")
        return False
        # exception "Template not found"
