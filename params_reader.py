import re

def income_params(query_string):
	array = re.split('[&]', query_string)
	nested_array = map(inner_splitting, array)
	return map(transform_to_dict, nested_array)


def inner_splitting(element):
	return re.split('[=]', element)


def transform_to_dict(element):
	return {element[0]: element[1]}
