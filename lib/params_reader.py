import re

def income_params(query_string):
    if len(query_string) is not 0:
        array = re.split('[&]', query_string)
        nested_array = map(inner_splitting, array)
        array_with_dicts = map(transform_to_dict, nested_array)
        return array_with_dicts


def inner_splitting(element):
    return re.split('[=]', element)


def transform_to_dict(element):
    return {element[0]: element[1]}
