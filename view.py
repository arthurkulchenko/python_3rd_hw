# import codecs
# from template_engine import env
# template = env.get_template('mytemplate.html')
from support import *
# file = template.render(the='variables', go='here')

def get_view_on(env, file, *args):
    # return codecs.open(templates_folder() + path_matcher(file) + ".html", 'r')
    # file = templates_folder() + path_matcher(file) + ".html"
    file = "index.html"
    template = env.get_template(file)
    # the = args[0]
    # go = args[1]
    return template.render(the=args[0], go=args[1])