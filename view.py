import codecs
from support import *

def get_view_on(file):
    return codecs.open(templates_folder() + path_matcher(file) + ".html", 'r')
