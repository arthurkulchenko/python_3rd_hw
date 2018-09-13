import os
from os.path import isfile, join


def templates():
    t = os.getcwd() + '/lib' +'/templates'
    return [f for f in os.listdir(t) if isfile(join(t, f))]


list = templates()
print list

<!-- 			    {% for key, val in params %}
			        <li>{{key}}:{{val}}</li>
			    {% endfor %} -->