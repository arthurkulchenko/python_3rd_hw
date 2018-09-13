from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

env = Environment(
    loader=FileSystemLoader(os.getcwd() + '/lib/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
