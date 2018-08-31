import os
import re

def get_current_dir_path(path_with_file=os.path.realpath(__file__)):
    exclusion_regex = "[\/][\w]+['.'][\D]+"
    dir_path = re.split(exclusion_regex, path_with_file)[0]
    return dir_path


def templates_folder():
	return get_current_dir_path() + '/templates'


def path_matcher(path):
	if path == '/':
	    return '/index'
	else:
	    return path
