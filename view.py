from template_engine import env
from support_routes import path_matcher

def get_view_on(file, **args):
    template = env.get_template(path_matcher(file) + ".html")
    return template.render(args).encode('utf-8')
