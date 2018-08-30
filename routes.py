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
    return [ True for r in routes if (route == r[0] and template_does_exist(route))]


def template_does_exist(path):
    requested = get_current_dir_path() + '/templates' + path_matcher(path)
    # requested = get_current_dir_path() + '/templates'
    exclusion_regex = "['.'][\D]+"
    requested_2 = re.split(exclusion_regex, requested)[0]
    file_path = requested_2 + '.html'
    if os.access(file_path, os.F_OK) is True:
        return True
    else:
        errors.list.append("Template not found")
        return False
        # exception "Template not found"
