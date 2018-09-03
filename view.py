# import codecs
from template_engine import env
from support import *

def get_view_on(file, *args):
    # return codecs.open(templates_folder() + path_matcher(file) + ".html", 'r')
    file = templates_folder() + path_matcher(file) + ".html"
    # template = env.get_template(file)
    template = env.get_template('index.html')
    return template.render(the=args[0], go=args[1])
