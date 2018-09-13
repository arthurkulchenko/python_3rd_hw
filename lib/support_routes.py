'''
    Helper methods for templates and routes
'''

import os, sys, re
from os.path import isfile, join
from routings import routes
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

env = Environment(
    loader=FileSystemLoader(os.getcwd() + '/lib/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def get_view_on(file, **args):
    template = env.get_template(file)
    return template.render(args).encode('utf-8')


def resourse_exist(resourse):
    if route_exist(resourse):
        return template_exist(resourse + '.html')


def template_exist(template):
    template = unslashing(template)
    if template in templates_list():
        return template


def templates_list():
    t = os.getcwd() + '/lib/templates'
    return [f for f in os.listdir(t) if isfile(join(t, f))]


def route_exist(route):
    return [r[1] for r in routes if route == r[0]][0]


def unslashing(data):
    return re.search('[a-z]+[.][\D]+', data).group()
