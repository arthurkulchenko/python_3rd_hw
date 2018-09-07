from jinja2 import Environment, FileSystemLoader, select_autoescape
from support import *

env = Environment(
    loader=FileSystemLoader(templates_folder()),
    autoescape=select_autoescape(['html', 'xml'])
)
