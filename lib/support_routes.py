import os
import os, sys, re
from os.path import isfile, join
from errors import errors
from template_engine import env
from routings import routes

def get_view_on(file, **args):
    # r = resourse_exist(file)
    template = env.get_template(file)
    return template.render(args).encode('utf-8')

def resourse_exist(resourse):
    if route_exist(resourse):
        return template_exist(resourse + '.html')


def template_exist(template):
    template = unslashing(template)
    if template in templates_list():
        return template
    else:
        return False


def templates_list():
    t = os.getcwd() + '/lib/templates'
    return [f for f in os.listdir(t) if isfile(join(t, f))]


def route_exist(route):
    return [r[1] for r in routes if route == r[0]][0]
    # if route in routes:
    #     return route
    # else:
    #     return False



def unslashing(data):
    return re.search('[a-z]+[.][\D]+', data).group()

# def route_does_exist(route, routes=routes):
#     return [True for r in routes if (route == r[0] and template_does_exist(route))]


# def route_template_matcher(route, routes=routes):
#     return [r[1] for r in routes if route == r[0]][0]


# def template_does_exist(path):
#     # requested = os.getcwd() + '/templates' + path_matcher(path)
#     # requested = os.getcwd() + '/templates' + routes[path]
#     requested = os.getcwd() + '/templates' + route_matcher(path)

#     file_path = re.split("['.'][\D]+", requested)[0] + '.html'
#     if os.access(file_path, os.F_OK) is True:
#         return True
#     else:
#         errors.list.append("Template not found")
#         return False
#         # exception "Template not found"


# def needs_redirection(path):
#     path = ''
#     return False
