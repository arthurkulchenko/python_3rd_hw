import os
import re

def get_current_dir_path(path_with_file=os.path.realpath(__file__)):
    exclusion_regex = "[\/][\w]+['.'][\D]+"
    dir_path = re.split(exclusion_regex, path_with_file)[0]
    return dir_path
    # https://duckduckgo.com/?q=%D0%BA%D0%B0%D0%BA+%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C+%D0%B8%D0%BC%D1%8F+%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F+%D0%B2+python&t=osx&ia=qa


def templates_folder():
	return get_current_dir_path() + '/templates'


def path_matcher(path):
	if path == '/':
	    return '/index'
	else:
	    return path
